"""
RSA Cryptographic Functions
============================

This module provides a set of functions to perform RSA encryption and decryption, including 
modular exponentiation, the Extended Euclidean algorithm, and message signing and verification.

Mathematical Background
-----------------------

### Modular Exponentiation

Given a base \( b \), an exponent \( e \), and a modulus \( m \), the goal is to efficiently compute:

\[
b^e \mod m
\]

This is achieved using the method of **exponentiation by squaring**, which reduces the number of multiplicative operations 
by breaking down the exponentiation process. The process can be described as:

\[
\text{result} = 1 \quad \text{(initially)}
\]
\[
b = b \mod m
\]
\[
\text{while } e > 0:
\]
\[
\quad \text{if } e \mod 2 = 1:
\]
\[
\quad \quad \text{result} = (\text{result} \times b) \mod m
\]
\[
\quad e = \left\lfloor \frac{e}{2} \right\rfloor
\]
\[
\quad b = (b \times b) \mod m
\]

The final value of `result` is the desired output \( b^e \mod m \).

### Extended Euclidean Algorithm

Given two integers \( a \) and \( b \), the Extended Euclidean algorithm finds integers \( x \) and \( y \) 
such that:

\[
ax + by = \gcd(a, b)
\]

The greatest common divisor \( \gcd(a, b) \) can be expressed as a linear combination of \( a \) and \( b \) 
using the Extended Euclidean algorithm, which also provides a way to compute the multiplicative inverse 
modulo \( \phi(N) \) in the context of RSA.

### RSA Key Generation and Message Signing

1. **RSA Key Components**: Choose two large prime numbers \( p \) and \( q \), then compute:

\[
N = p \times q
\]

\[
\phi(N) = (p-1) \times (q-1)
\]

2. **Public and Private Keys**: Choose an integer \( e \) (public exponent) such that \( 1 < e < \phi(N) \) 
and \( \gcd(e, \phi(N)) = 1 \). Then, compute the private exponent \( d \) as the modular inverse of \( e \) 
mod \( \phi(N) \):

\[
d \times e \equiv 1 \pmod{\phi(N)}
\]

This is computed using the Extended Euclidean algorithm.

3. **Message Signing**: To sign a message \( M \), compute the signature:

\[
S = M^e \mod N
\]

4. **Message Verification**: To verify a signature, compute:

\[
M' = S^d \mod N
\]

If \( M' = M \), the signature is valid.

Example Usage
-------------

Given two prime numbers \( p = 101 \) and \( q = 761 \), the module can generate an RSA key pair, sign a 
message, and verify the signature as follows:

```python
p, q = 101, 761
N = p * q
e = 3
message = 32

encoded_message, private_key = sign_message(message, N, e, p, q)
is_valid = verify_message(message, encoded_message, private_key, N)

print(f"Was the message encoded correctly? {is_valid}")
"""

from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def mod_exp(base: int, exp: int, mod: int) -> int:
    """Performs modular exponentiation."""
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod

    return result


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Performs the extended Euclidean algorithm."""
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_gcd(b, a % b)
        return y, x - (a // b) * y, gcd


def sign_message(message: int, modulus: int, public_exponent: int, p: int, q: int) -> Tuple[int, int]:
    """Signs a message using RSA-like algorithm."""
    phi = (p - 1) * (q - 1)
    _, private_exponent, _ = extended_gcd(public_exponent, phi)
    private_exponent %= phi

    signature = mod_exp(message, public_exponent, modulus)
    return signature, private_exponent


def verify_signature(original_message: int, signature: int, private_exponent: int, modulus: int) -> bool:
    """Verifies the signed message."""
    decoded_message = mod_exp(signature, private_exponent, modulus)
    return decoded_message == original_message


def main() -> None:
    p, q = 103, 787
    modulus = p * q
    public_exponent = 7
    message = 42

    signature, private_exponent = sign_message(message, modulus, public_exponent, p, q)
    is_valid = verify_signature(message, signature, private_exponent, modulus)

    print(f"Was the message signed and verified correctly? {is_valid}")

    # Verify using an external library
    private_key = rsa.RSAPrivateNumbers(
        p=p,
        q=q,
        d=private_exponent,
        dmp1=private_exponent % (p - 1),
        dmq1=private_exponent % (q - 1),
        iqmp=pow(q, -1, p),
        public_numbers=rsa.RSAPublicNumbers(public_exponent, modulus)
    ).private_key()

    public_key = private_key.public_key()

    signature_external = public_key.encrypt(
        message.to_bytes((message.bit_length() + 7) // 8, 'big'),
        padding.PKCS1v15()
    )

    verified_external = private_key.decrypt(
        signature_external,
        padding.PKCS1v15()
    )

    print(f"Was the external library verification successful? {verified_external == message.to_bytes((message.bit_length() + 7) // 8, 'big')}")


if __name__ == "__main__":
    main()
