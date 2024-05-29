
import os
import random
from PIL import Image

def compress_images():
    for i,file in enumerate(os.listdir('train')):
    # compress the image
        img = Image.open("train/"+file)
        img = img.resize((562, 562), Image.LANCZOS)
        img.save("train_resized/"+file, quality=95)
        print(img.size)
