import socket
import sys
from typing import List

def scan_port(ip_address: str, port: int) -> str:
    """Attempts to connect to a specified port on a given IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                try:
                    sock.sendall(b'Hello\r\n')
                    banner = sock.recv(1024).decode().strip()
                    return f"Port {port}: OPEN - {banner}"
                except socket.timeout:
                    return f"Port {port}: OPEN - No response"
                except Exception as e:
                    return f"Port {port}: OPEN - Error: {e}"
            else:
                return f"Port {port}: CLOSED"
    except socket.error as e:
        return f"Port {port}: ERROR - {e}"

def scan_common_ports(ip_address: str) -> None:
    """Scans common ports on the given IP address."""
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3389: "RDP",
    }

    print(f"Scanning common ports on {ip_address}...\n")
    for port, service in common_ports.items():
        result = scan_port(ip_address, port)
        print(result)

def main(args: List[str]) -> None:
    """Main function to handle command-line arguments and perform port scanning."""
    ip_address = args[0] if args else '127.0.0.1'  # Default to localhost for demo purposes
    
    try:
        scan_common_ports(ip_address)
    except Exception as e:
        print(f"Error during scanning: {e}")

if __name__ == "__main__":
    main(sys.argv[1:])
