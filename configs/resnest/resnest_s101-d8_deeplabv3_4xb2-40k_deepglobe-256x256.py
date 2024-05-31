# HERE
_base_ = '../deeplabv3/deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py'
model = dict(
    pretrained='open-mmlab://resnest101',
    backbone=dict(
        type='ResNeSt',
        stem_channels=128,
        radix=2,
        reduction_factor=4,
        avg_down_stride=True))
