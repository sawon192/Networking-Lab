# Simple Packet Sniffer using Scapy
# This program captures 10 packets and displays
# basic information about each packet.

from scapy.all import *

packet_number = 0


def analyze(packet):
    global packet_number

    packet_number += 1

    print("\n==========================================")
    print("Packet Number :", packet_number)
    print("==========================================")

    # IP Information
    if packet.haslayer(IP):
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)
        print("TTL            :", packet[IP].ttl)

    # TCP Information
    if packet.haslayer(TCP):
        print("\nTCP Packet")
        print("Source Port      :", packet[TCP].sport)
        print("Destination Port :", packet[TCP].dport)
        print("Sequence Number  :", packet[TCP].seq)
        print("ACK Number       :", packet[TCP].ack)

    # UDP Information
    if packet.haslayer(UDP):
        print("\nUDP Packet")
        print("Source Port      :", packet[UDP].sport)
        print("Destination Port :", packet[UDP].dport)

    # ICMP Information
    if packet.haslayer(ICMP):
        print("\nICMP Packet")
        print("Type :", packet[ICMP].type)
        print("Code :", packet[ICMP].code)

    # Ethernet Information
    if packet.haslayer(Ether):
        print("\nEthernet Frame")
        print("Source MAC      :", packet[Ether].src)
        print("Destination MAC :", packet[Ether].dst)

    print("\nPacket Summary")
    print(packet.summary())

    print("==========================================")


print("Simple Packet Sniffer Started...")
print("Capturing 10 packets...\n")

sniff(count=10, prn=analyze)

print("\nPacket capture finished.")
