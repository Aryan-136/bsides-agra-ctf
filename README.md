# :triangular_flag_on_post: BSides Agra CTF - Exploit Framework & Technical Writeups

[![Security](https://img.shields.io/badge/Domain-Cybersecurity%20%2F%20CTF-red?style=for-the-badge&logo=kalilinux&logoColor=white)](https://bsidesagra.in)
[![Python](https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scapy](https://img.shields.io/badge/Network%20Forensics-Scapy-F38020?style=for-the-badge&logo=wireshark&logoColor=white)](https://scapy.net)
[![Burp Suite](https://img.shields.io/badge/Web%20Auditing-Burp%20Suite-FF6633?style=for-the-badge&logo=portswigger&logoColor=white)](https://portswigger.net)

A curated repository of offensive security writeups, exploit proof-of-concepts, and network forensic analysis scripts developed for challenges solved during the **BSides Agra CTF** cybersecurity competition.

---

## :open_file_folder: Challenge Writeups Index

| Category | Challenge Name | Target Vulnerability | Exploit Artifact |
| :--- | :--- | :--- | :--- |
| **Web Security** | `TokenForge` | JWT `alg: none` Signature Confusion | [`web/jwt-token-forge`](web/jwt-token-forge) |
| **Network Forensics** | `SilentEchoes` | ICMP Data Exfiltration Tunneling | [`network/icmp-exfil-analysis`](network/icmp-exfil-analysis) |

---

## :toolbox: Tooling & Methodology

- **Web Exploitation**: Burp Suite Professional, OWASP ZAP, Python `requests`, JSON Web Token cryptographic tools.
- **Network Traffic Analysis**: Wireshark, TShark, Scapy packet dissection, PCAP stream reassembly.
- **Reconnaissance & Enumeration**: Nmap, Sublist3r, FFUF directory fuzzing.

---

## :warning: Disclaimer
All scripts, writeups, and proof-of-concepts in this repository are published strictly for educational and defense-in-depth security training purposes under responsible disclosure guidelines.