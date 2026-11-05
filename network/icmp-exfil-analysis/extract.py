#!/usr/bin/env python3
"""
BSides Agra CTF - Network Forensics
Challenge: SilentEchoes (ICMP Tunnel Exfiltration)
Extracts covert data payloads embedded within ICMP Echo Request packets.
"""
from scapy.all import rdpcap, ICMP

def extract_icmp_covert_data(pcap_file: str):
    print(f"[*] Parsing pcap file: {pcap_file}")
    packets = rdpcap(pcap_file)
    extracted_bytes = bytearray()

    for pkt in packets:
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 8: # Echo Request
            payload = bytes(pkt[ICMP].payload)
            if payload:
                # Covert byte placed in the first byte of payload
                extracted_bytes.append(payload[0])

    try:
        decoded_text = extracted_bytes.decode('utf-8', errors='ignore')
        print("[+] Extracted Covert Stream:")
        print(decoded_text)
    except Exception as e:
        print(f"[!] Error decoding bytes: {e}")

if __name__ == "__main__":
    extract_icmp_covert_data("capture.pcap")