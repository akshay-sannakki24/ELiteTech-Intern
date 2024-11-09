# Image Encryption and Decryption Using RGB Channel Swapping
This Python script demonstrates a simple method for encrypting and decrypting images by swapping the red and blue channels of the image. 

The encryption process is based on a simple transformation that can be reversed, making it suitable for demonstration purposes in image processing.


## Features
- Encrypts an image by swapping its red and blue RGB channels.
- Decrypts the image by reversing the encryption process (swapping red and blue channels back).
- Works with any `.jpg` image file.
- Uses the Python `Pillow` (PIL) library for image processing.


## Requirements
- Python 3.x
- `Pillow` library


## Installation
To install the required library, use the following pip command:
pip install pillow


## Usage
1. Clone or download this repository to your local machine.
2. Ensure you have an image file (e.g., input.jpg) for testing.
3. Modify the paths to the input and output image files as required in the script.
4. Run the script using Python:
   - python image_encryption.py
5. The script will:
   - Encrypt the input image by swapping the red and blue channels.
   - Save the encrypted image as encrypted_image.jpg.
   - Decrypt the encrypted image by swapping the channels back and save the result as decrypted_image.jpg.


## Example
1. Input Image: input.jpg
2. Encrypted Image: encrypted_image.jpg (Channels swapped)
3. Decrypted Image: decrypted_image.jpg (Original image restored)


## Code Explanation
### Functions
  1. encrypt_image(input_path, output_path, key=None):
     - Opens the image at input_path.
     - Swaps the red and blue channels for each pixel in the image.
     - Saves the modified image at output_path.
  2. decrypt_image(input_path, output_path, key=None):
     - Opens the encrypted image at input_path.
     - Reverses the encryption by swapping the red and blue channels back.
     - Saves the restored image at output_path.


## Example Flow
1. Encryption: The red and blue channels of each pixel are swapped to encrypt the image.
2. Decryption: The red and blue channels are swapped back to restore the original image.


## License
This project is open-source and available under the MIT License.
