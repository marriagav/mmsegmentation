#HERE
import os
import random
import cv2
from PIL import Image
import numpy as np

def rgb_to_limited_grayscale(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_img = img.convert("L")
    
    # Convert the image data to a numpy array
    grayscale_array = np.array(grayscale_img)
    
    # Normalize the grayscale values to the range 0 to 1
    normalized_array = grayscale_array / 255.0
    
    # Scale the normalized values to the range 0 to 6
    scaled_array = normalized_array * 6
    
    # Convert the scaled values to integers
    limited_grayscale_array = np.round(scaled_array).astype(np.uint8)
    
    # Convert the numpy array back to a PIL image
    limited_grayscale_img = Image.fromarray(limited_grayscale_array)
    
    for i in range(len(limited_grayscale_array)):
        print(limited_grayscale_array[i])
        
    # Save the transformed image
    limited_grayscale_img.save(output_path)

def send_to_correct(file, train_set=True):
    final_path = "train/" if train_set else "val/"
    if 'mask' in file:
        path = f'../data/deep_globe/ann_dir/{final_path}' + file
        rgb_to_limited_grayscale("train/" + file, path)
        # os.rename("train/"+file,path)
    else:
        path = f'../data/deep_globe/img_dir/{final_path}' + file
        print(path)
        os.rename("train/"+file,f'../data/deep_globe/img_dir/{final_path}' + file)

def separate_dataset():
    dict_map = {}

    if not os.path.exists('../data/deep_globe'):
        os.makedirs('../data/deep_globe')

    if not os.path.exists('../data/deep_globe/ann_dir'):
        os.makedirs('../data/deep_globe/ann_dir')
    
    if not os.path.exists('../data/deep_globe/img_dir'):
        os.makedirs('../data/deep_globe/img_dir')

    if not os.path.exists('../data/deep_globe/ann_dir/train'):
        os.makedirs('../data/deep_globe/ann_dir/train')
    
    if not os.path.exists('../data/deep_globe/ann_dir/val'):
        os.makedirs('../data/deep_globe/ann_dir/val')

    if not os.path.exists('../data/deep_globe/img_dir/val'):
        os.makedirs('../data/deep_globe/img_dir/val')

    if not os.path.exists('../data/deep_globe/img_dir/train'):
        os.makedirs('../data/deep_globe/img_dir/train')

    for i,file in enumerate(os.listdir('train')):
        index = file.split("_")[0]
        if index in dict_map:
            rand_int = dict_map[index]
        else:
            rand_int = random.randint(0, 9)
            dict_map[index] = rand_int
        if rand_int < 8:
            send_to_correct(file)
        else:
            send_to_correct(file, False)

separate_dataset()