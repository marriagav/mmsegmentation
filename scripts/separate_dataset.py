#HERE
import os
import random
import cv2
from PIL import Image
import numpy as np

def rgb_to_limited_grayscale(image_path, output_path):
    # Define the masks with tolerance
    masks = {
        "urban_land": (0, 255, 255),
        "agriculture_land": (255, 255, 0),
        "rangeland": (255, 0, 255),
        "forest_land": (0, 255, 0),
        "water": (0, 0, 255),
        "barren_land": (255, 255, 255),
        "unknown": (0, 0, 0),
    }
    
    # Tolerance value
    tolerance = 20

    def is_within_tolerance(pixel, target, tolerance):
        return all(target[i] - tolerance <= pixel[i] <= target[i] + tolerance for i in range(3))

    # Open the image
    img = Image.open(image_path).convert("RGB")
    
    # Convert the image data to a numpy array
    img_array = np.array(img)
    
    # Create an empty array for the grayscale image
    grayscale_array = np.zeros((img_array.shape[0], img_array.shape[1]), dtype=np.uint8)
    
    # Map each class to a grayscale value
    class_to_grayscale = {
        "urban_land": 0,
        "agriculture_land": 1,
        "rangeland": 2,
        "forest_land": 3,
        "water": 4,
        "barren_land": 5,
        "unknown": 6,
    }
    
    # Iterate over each pixel in the image
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            pixel = img_array[i, j]
            assigned = False
            for cls, target in masks.items():
                if is_within_tolerance(pixel, target, tolerance):
                    grayscale_array[i, j] = class_to_grayscale[cls]
                    assigned = True
                    break
            if not assigned:
                grayscale_array[i, j] = class_to_grayscale["unknown"]
    
    # Convert the numpy array back to a PIL image
    limited_grayscale_img = Image.fromarray(grayscale_array)
    
    # Save the transformed image
    limited_grayscale_img.save(output_path)

def send_to_correct(file, train_set=True):
    final_path = "train/" if train_set else "val/"
    if 'mask' in file:
        path = f'../data/deep_globe/ann_dir/{final_path}' + file
        rgb_to_limited_grayscale("train_resized/" + file, path)
        # os.rename("train_resized/"+file,path)
    else:
        path = f'../data/deep_globe/img_dir/{final_path}' + file
        print(path)
        os.rename("train_resized/"+file,f'../data/deep_globe/img_dir/{final_path}' + file)

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