import os
import sys
import platform
import subprocess
from typing import List

def ping_host(host: str, count: int = 4) -> None:
    """Pings a host and displays the latency for each ping."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    try:
        command = ['ping', param, str(count), host]
        output = subprocess.check_output(command).decode('utf-8')
        
        print(f"Ping results for {host}:\n")
        print(output)
        
        if "Request timed out" in output or "100% packet loss" in output:
            print(f"{host} is unreachable.\n")
        else:
            print(f"{host} is reachable.\n")
            
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {host}: {e}")

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and ping the specified host."""
    host = args[0] if args else '8.8.8.8'  # Default to Google's public DNS server for demo purposes
    
    print(f"Pinging {host}...\n")
    ping_host(host)

if __name__ == "__main__":
    main(sys.argv[1:])
