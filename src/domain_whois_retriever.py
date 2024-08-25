import whois
import sys
from typing import List

def get_whois_info(domain: str) -> None:
    """Fetches and displays WHOIS information for the given domain."""
    try:
        domain_info = whois.whois(domain)
        
        print(f"\nWHOIS Information for {domain}:\n")
        for key, value in domain_info.items():
            print(f"{key:<20}: {value}")
    except Exception as e:
        print(f"Error fetching WHOIS information: {e}")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and fetch WHOIS info."""
    if args:
        get_whois_info(args[0])
    else:
        domain = input("Please enter a domain name: ")
        get_whois_info(domain)

if __name__ == "__main__":
    main(sys.argv[1:])
