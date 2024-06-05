#HERE
import os
import random
from PIL import Image

def compress_images():
    # Create the destination directory if it doesn't exist
    if not os.path.exists('./test_resized'):
        os.makedirs('./test_resized')
        
    for i, file in enumerate(os.listdir('test')):
        # Open the image
        img = Image.open(os.path.join('test', file))
        
        # Resize the image
        img = img.resize((256, 256), Image.LANCZOS)
        
        # Convert to RGB if necessary
        # if img.mode != 'RGB':
        #     img = img.convert('RGB')
        
        # Construct the new filename with .jpg extension
        # new_filename = os.path.splitext(file)[0] + '.jpg'
        
        # Save the image in JPEG format
        img.save(os.path.join('test_resized', file))
        
        num_channels = len(img.getbands())
        print("CHANELS",num_channels)

        print(f"Processed {file}: size {img.size}")
