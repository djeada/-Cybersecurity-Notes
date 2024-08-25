import requests
import sys
import time
from typing import List

def check_website_status(url: str) -> None:
    """Checks the status and response time of a given website."""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = time.time() - start_time

        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")

        if response.status_code == 200:
            print("Website is reachable and functioning correctly.")
        else:
            print("Website returned an error or non-200 status.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach the website: {e}")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and check website status."""
    url = args[0] if args else 'https://www.example.com'  # Default to example.com for demo purposes
    
    check_website_status(url)

if __name__ == "__main__":
    main(sys.argv[1:])
