import hashlib
import sys
from typing import Optional

def calculate_file_hash(file_path: str, hash_algorithm: str = 'sha256') -> str:
    """Calculates the hash of a file using the specified hash algorithm."""
    hash_func = getattr(hashlib, hash_algorithm)()
    
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {file_path} - {e}")
        sys.exit(1)

def verify_file_integrity(file_path: str, known_hash: str, hash_algorithm: str = 'sha256') -> bool:
    """Verifies the integrity of a file by comparing its hash to a known hash."""
    calculated_hash = calculate_file_hash(file_path, hash_algorithm)
    return calculated_hash == known_hash

def main(args: Optional[list] = None) -> None:
    """Main function to handle command-line arguments and perform hash calculation and verification."""
    if args is None or len(args) < 1:
        print("Usage: python file_hash_checker.py <file_path> [known_hash]")
        sys.exit(1)

    file_path = args[0]
    known_hash = args[1] if len(args) > 1 else None

    print(f"Calculating {hash_algorithm} hash for {file_path}...\n")
    calculated_hash = calculate_file_hash(file_path)

    print(f"Calculated Hash: {calculated_hash}")

    if known_hash:
        print(f"Known Hash:      {known_hash}")
        if verify_file_integrity(file_path, known_hash):
            print("File integrity verified: The hashes match.")
        else:
            print("File integrity verification failed: The hashes do not match.")
    else:
        print("No known hash provided for verification.")

if __name__ == "__main__":
    main(sys.argv[1:])
