from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    try:
        
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found!")
            return
        
        
        img = Image.open(input_path).convert("RGB")
        pixels = np.array(img, dtype=np.uint8) 
        
        
        encrypted_pixels = pixels ^ np.uint8(key)
        
        
        encrypted_img = Image.fromarray(encrypted_pixels, mode="RGB")
        encrypted_img.save(output_path)
        
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"Error encrypting image: {e}")


def decrypt_image(input_path, output_path, key):
    try:
        
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found!")
            return

        
        img = Image.open(input_path).convert("RGB")
        pixels = np.array(img, dtype=np.uint8)
        
        
        decrypted_pixels = pixels ^ np.uint8(key)
        
        
        decrypted_img = Image.fromarray(decrypted_pixels, mode="RGB")
        decrypted_img.save(output_path)
        
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"Error decrypting image: {e}")



input_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\input_image.jpg"
encrypted_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\encrypted_image.jpg"
decrypted_image = r"C:\Users\91759\Documents\OneDrive\Desktop\img\decrypted_image.jpg"


key = 123


encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
