# HERE
_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/deep_globe_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (612, 612)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)

# 2448 x 2448