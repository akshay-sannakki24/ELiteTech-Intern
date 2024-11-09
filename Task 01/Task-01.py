# ===============================================================================================================
# Date : 20214-11-06
# Email : akshaysannakki@gmail.com
# License : MIT License
# Description : This Python script implements a basic Caesar cipher, which is a simple encryption technique 
#               where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. 
#               This project demonstrates how to encrypt and decrypt messages using the Caesar cipher algorithm.
# ===============================================================================================================
# Disclaimer : For educational purposes only.
# ===============================================================================================================


def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypted message
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    
    # Decrypted message
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted message:", decrypted_message)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result
if __name__ == "__main__":
    main()