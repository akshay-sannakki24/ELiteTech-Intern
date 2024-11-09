# Network Packet Sniffer
This Python script uses the `scapy` library to sniff network packets.

Display information about them, including source and destination IP addresses, protocols used, and any TCP/UDP payloads.


## Features
1. Captures and analyzes packets in real-time.
2. Displays source and destination IP addresses along with the protocol type.
3. Attempts to decode and display TCP and UDP payloads.
4. Ignores non-decodable payloads gracefully.


## Requirements
- Python 3.x
- `scapy` library


### Installation
To install the required library, use the following pip command:
- pip install scapy


## Note
Running this script may require administrative privileges due to the need to capture network packets.


## Usage
1. Clone or download this repository to your local machine.
2. Open the terminal or command prompt and navigate to the project directory.
3. Run the script using Python:
   - python packet_sniffer.py
4. The script will start capturing packets and display information in the console.


## Code Explanation

### 1. packet_callback(packet)
- This function is triggered for each captured packet.
- It checks if the packet has an IP layer and extracts the source IP, destination IP, and protocol.
- If the packet contains TCP or UDP layers, it attempts to extract and decode the payload, printing it to the console.
- It handles exceptions gracefully if the payload cannot be decoded.

### 2. start_sniffing()
- This function initiates the packet sniffing process using scapy.sniff().
- The store=False parameter prevents the packets from being stored in memory, and prn=packet_callback specifies the callback function to process each captured packet.


## Important Note
Packet sniffing can capture sensitive information and may violate privacy laws and policies. Use this tool responsibly and only on networks where you have permission to monitor traffic.
Ensure you run this script with the necessary permissions (e.g., as an administrator) for it to function correctly.


## License
This project is open-source and available under the MIT License.
