# LINKS

* VISUALIZE PACKETS: https://apackets.com/


# Network Packet Filter Notes

## 1. IP Address Filter
- **Filter:** `ip.addr == 192.168.1.1`
- **Example Usage:** Displays all packets involving the IP address 192.168.1.1, including both incoming and outgoing traffic.

## 2. TCP Port Filter
- **Filter:** `tcp.port == 80`
- **Example Usage:** Shows all TCP packets where the source or destination port is 80, commonly used for HTTP traffic.

## 3. Protocol Filter
- **Filter:** `http`
- **Example Usage:** Displays all HTTP packets, useful for analyzing unencrypted traffic.

## 4. Source and Destination Filter
- **Filter:** `ip.src == 192.168.1.1 && ip.dst == 192.168.1.2`
- **Example Usage:** Shows all packets from 192.168.1.1 to 192.168.1.2, useful for tracking specific communication between two devices.

## 5. MAC Address Filter
- **Filter:** `eth.addr == 00:1B:44:11:3A:B7`
- **Example Usage:** Displays all packets involving the Ethernet (MAC) address 00:1B:44:11:3A:B7.

## 6. Conversations Filter
- **Filter:** `(ip.addr == 192.168.1.1 && ip.addr == 10.1.2.3) && (tcp.port == 443)`
- **Example Usage:** Displays traffic between IP addresses 192.168.1.1 and 10.1.2.3 over TCP port 443, commonly for HTTPS traffic.

## 7. Exclude Filter
- **Filter:** `!arp`
- **Example Usage:** Displays all packets except ARP packets, useful for focusing on higher-level protocols.

## 8. TCP Flags Filter
- **Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- **Example Usage:** Shows all TCP SYN packets, useful for analyzing TCP connection setups.

## 9. DNS Queries Filter
- **Filter:** `dns.flags.response == 0`
- **Example Usage:** Displays all DNS query packets, excluding responses, focusing on initial queries.

## 10. Length or Size Filter
- **Filter:** `frame.len > 1000`
- **Example Usage:** Shows packets with a frame length greater than 1000 bytes, useful for identifying larger packets.
