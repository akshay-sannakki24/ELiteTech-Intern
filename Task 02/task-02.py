# ===============================================================================================
# Author : Akshay Sannakki
# Date : 2024-11-06
# Email : akshaysannakki@gmail.com
# License : MIT License
# Description : This Python script demonstrates a simple method for encrypting and 
#               decrypting images by swapping the red and blue channels of the image. 
#               The encryption process is based on a simple transformation that can be reversed, 
#               making it suitable for demonstration purposes in image processing.
# ===============================================================================================
# Disclaimer : For educational purposes only.
# ===============================================================================================


from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    # Open the input image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key=None):
    # Open the encrypted image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels back
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = r"C:\Users\aksha\Desktop\Internship_-_Cyber_Security\PRODIGY_CS-02-main\input.jpg"
encrypted_image = r"C:\Users\aksha\Desktop\Internship_-_Cyber_Security\PRODIGY_CS-02-main\encrypted_image.jpg"
decrypted_image = r"C:\Users\aksha\Desktop\Internship_-_Cyber_Security\PRODIGY_CS-02-main\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
