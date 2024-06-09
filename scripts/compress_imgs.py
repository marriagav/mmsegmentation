#HERE
import os
import random
from PIL import Image

def compress_images():
    # Create the destination directory if it doesn't exist
    if not os.path.exists('./train_resized'):
        os.makedirs('./train_resized')
        
    for i, file in enumerate(os.listdir('train')):
        # Open the image
        img = Image.open(os.path.join('train', file))
        
        # Resize the image
        img = img.resize((256, 256), Image.LANCZOS)
        
        # Convert to RGB if necessary
        # if img.mode != 'RGB':
        #     img = img.convert('RGB')
        
        # Construct the new filename with .jpg extension
        # new_filename = os.path.splitext(file)[0] + '.jpg'
        
        # Save the image in JPEG format
        img.save(os.path.join('train_resized', file))
        
        num_channels = len(img.getbands())
        print("CHANELS",num_channels)

        print(f"Processed {file}: size {img.size}")
