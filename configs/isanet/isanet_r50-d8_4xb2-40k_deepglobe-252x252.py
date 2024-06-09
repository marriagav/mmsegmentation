# HERE
_base_ = [
    '../_base_/models/isanet_r50-d8.py', '../_base_/datasets/deep_globe_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_20k.py'
]
crop_size = (256, 256)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)