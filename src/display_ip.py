import socket
import requests
import json
import urllib.request
import sys
from typing import List

def get_ip_info(ip_address: str = '') -> None:
    """Fetches and displays IP information from the ipinfo.io service."""
    url = f'https://ipinfo.io/{ip_address}/json' if ip_address else 'https://ipinfo.io/json'
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            for key, value in data.items():
                print(f"{key:<15} ->\t{value}")
    except urllib.error.URLError as e:
        print(f"Failed to retrieve IP information: {e}")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and fetch IP info."""
    if args:
        ip_address = requests.get(args[0]).text.strip()
        get_ip_info(ip_address)
    else:
        get_ip_info()

if __name__ == "__main__":
    main(sys.argv[1:])
	
