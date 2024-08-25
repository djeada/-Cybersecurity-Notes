import requests
import json
import sys
import re
import uuid

def get_mac_info(mac_address: str = '') -> None:
    """Fetches and displays information about a given MAC address."""
    if not mac_address:
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    
    url = f'https://api.macvendors.com/{mac_address}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        print(f"MAC Address: {mac_address}")
        print(f"Vendor: {response.text}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching MAC information: {e}")

def main(args: list[str]) -> None:
    """Main function to handle command-line arguments and fetch MAC address info."""
    if args:
        get_mac_info(args[0])
    else:
        get_mac_info()

if __name__ == "__main__":
    main(sys.argv[1:])
