import ssl
import socket
import sys
import datetime
from typing import List

def get_ssl_certificate_info(domain: str, port: int = 443) -> None:
    """Fetches and displays SSL certificate information for the given domain."""
    context = ssl.create_default_context()

    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()

    print(f"SSL Certificate Information for {domain}:\n")

    subject = dict(x[0] for x in cert['subject'])
    issuer = dict(x[0] for x in cert['issuer'])
    
    print(f"Subject: {subject.get('commonName', 'N/A')}")
    print(f"Issuer: {issuer.get('commonName', 'N/A')}")
    print(f"Valid From: {cert['notBefore']}")
    print(f"Valid Until: {cert['notAfter']}")
    
    current_time = datetime.datetime.utcnow()
    expiry_time = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    
    days_until_expiry = (expiry_time - current_time).days
    print(f"Days Until Expiry: {days_until_expiry} days")
    
    print(f"Serial Number: {cert.get('serialNumber', 'N/A')}")
    print(f"Algorithm: {cert.get('signatureAlgorithm', 'N/A')}\n")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and retrieve SSL certificate info."""
    domain = args[0] if args else 'www.example.com'  # Default to example.com for demo purposes

    print(f"Retrieving SSL certificate information for {domain}...\n")
    get_ssl_certificate_info(domain)

if __name__ == "__main__":
    main(sys.argv[1:])
