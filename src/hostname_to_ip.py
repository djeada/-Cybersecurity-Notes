import socket
import sys
from typing import List

def get_ip_from_hostname(hostname: str = '') -> None:
    """Fetches and displays the IP address for a given hostname."""
    try:
        if not hostname:
            hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror as e:
        print(f"Error resolving hostname '{hostname}': {e}")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and fetch IP address info."""
    if args:
        get_ip_from_hostname(args[0])
    else:
        get_ip_from_hostname()

if __name__ == "__main__":
    main(sys.argv[1:])
