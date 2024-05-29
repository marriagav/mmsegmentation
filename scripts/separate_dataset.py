#HERE
import os
import random

def send_to_correct(file, train_set=True):
    final_path = "train/" if train_set else "val/"
    if 'mask' in file:
        path = f'../data/deep_globe/ann_dir/{final_path}' + file
        print(path)
        os.rename("train_resized/"+file,path)
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

    for i,file in enumerate(os.listdir('train_resized')):
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