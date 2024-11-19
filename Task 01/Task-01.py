print ("""
==========================================================================

Author : Akshay Sannakki                                Date : 2024-11-06

Email ID : akshaysannakki@gmail.com                 License : MIT License

==========================================================================
# Disclaimer : For educational purposes only.
==========================================================================
""")

def caesar_cipher(text: str, shift: int, alphabet: str = 'abcdefghijklmnopqrstuvwxyz') -> str:
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The message to encrypt or decrypt.
        shift (int): The shift value (positive for encryption, negative for decryption).
        alphabet (str): The alphabet to use for encryption (default is lowercase letters).

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    result = ""
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            idx = alphabet.index(char.lower())
            new_idx = (idx + shift) % len(alphabet)
            new_char = alphabet[new_idx].upper() if is_upper else alphabet[new_idx]
            result += new_char
        else:
            result += char
    return result


def main():
    try:
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        # Encrypt message
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)

        # Decrypt message
        decrypted_message = caesar_cipher(encrypted_message, -shift)
        print("Decrypted message:", decrypted_message)
    except ValueError:
        print("Invalid input. Shift value must be an integer.")


if __name__ == "__main__":
    main()
