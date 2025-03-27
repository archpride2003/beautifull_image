from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found!")
            return
        
        # Open and convert the image to an RGB format
        img = Image.open(input_path).convert("RGB")
        pixels = np.array(img, dtype=np.uint8)  # Convert image to NumPy array
        
        # Ensure key is applied in a valid way (e.g., bit-wise XOR on every pixel channel)
        encrypted_pixels = pixels ^ np.uint8(key)
        
        # Convert array back to an image and save it
        encrypted_img = Image.fromarray(encrypted_pixels, mode="RGB")
        encrypted_img.save(output_path)
        
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"Error encrypting image: {e}")


def decrypt_image(input_path, output_path, key):
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found!")
            return

        # Open and convert the image to RGB format
        img = Image.open(input_path).convert("RGB")
        pixels = np.array(img, dtype=np.uint8)
        
        # Apply key using XOR to decrypt
        decrypted_pixels = pixels ^ np.uint8(key)
        
        # Convert array back to an image and save it
        decrypted_img = Image.fromarray(decrypted_pixels, mode="RGB")
        decrypted_img.save(output_path)
        
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"Error decrypting image: {e}")


# File paths
input_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\input_image.jpg"
encrypted_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\encrypted_image.jpg"
decrypted_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\decrypted_image.jpg"

# Encryption key (must be small enough to fit within byte range 0-255)
key = 123

# Encrypt and decrypt
encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
