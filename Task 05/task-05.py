print ("""
==========================================================================

Author : Akshay Sannakki                                Date : 2024-11-06

Email ID : akshaysannakki@gmail.com                 License : MIT License

==========================================================================
# Disclaimer : For educational purposes only.
==========================================================================
""")

import scapy.all as scapy
from pynput import keyboard
import threading
import sys

# Flag to indicate when to stop sniffing
stop_sniffing_flag = False

def packet_callback(packet):
    """
    Callback function to process captured packets.

    Args:
        packet: The captured network packet.
    """
    if packet.haslayer(scapy.IP):  # Check if the packet contains an IP layer
        src_ip = packet[scapy.IP].src  # Get the source IP
        dst_ip = packet[scapy.IP].dst  # Get the destination IP
        protocol = packet[scapy.IP].proto  # Get the protocol (e.g., TCP, UDP)
        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):  # If the packet contains a payload
            try:
                payload = packet[scapy.Raw].load  # Extract the raw payload
                print(f"Payload: {payload.decode('utf-8', 'ignore')}")  # Attempt to decode the payload
            except UnicodeDecodeError:
                print("Unable to decode payload.")  # In case decoding fails

def on_press(key):
    """
    Function to handle key press events.
    Stops the sniffing when the 'ESC' key is pressed.

    Args:
        key: The key object captured by the listener.
    """
    global stop_sniffing_flag
    if key == keyboard.Key.esc:
        print("\n'ESC' key pressed. Stopping packet sniffing...")
        stop_sniffing_flag = True
        return False  # Stop the listener

def start_sniffing(filter: str = "tcp"):
    """
    Starts sniffing packets on the network.

    Args:
        filter (str): The packet filter to apply (e.g., "tcp", "udp").
    """
    print(f"Sniffing packets with filter: {filter}")
    try:
        # Start sniffing with the provided filter (e.g., 'tcp')
        scapy.sniff(filter=filter, store=False, prn=packet_callback, stop_filter=lambda x: stop_sniffing_flag)
    except Exception as e:
        print(f"An error occurred while sniffing: {e}")  # Catch and print any errors

if __name__ == "__main__":
    # Start the listener for the ESC key press in a separate thread
    listener = keyboard.Listener(on_press=on_press)
    listener_thread = threading.Thread(target=listener.start)
    listener_thread.daemon = True  # Daemonize thread to exit when the main program exits
    listener_thread.start()

    # Start packet sniffing
    start_sniffing()
