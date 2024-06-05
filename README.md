# DeepGlobe dataset for agriculture field segmentation

## Team: 5

## Team Members:

- Iván Díaz
- Miguel Arriaga
- Pablo Rocha

# Content

- [Local setup](#local-setup)
- [Google Colab setup](#google-colab-setup)

# Local setup

1.  Clone the repository and navigate to the project folder

```bash
git clone git@github.com:marriagav/mmsegmentation.git
cd mmsegmentation
```

2.  Create a virtual environment and install the dependencies

```bash
conda create -name mmseg python=3.10
conda activate mmseg
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
pip install openmim
mim install mmcv==2.1.0
pip install -v -e . && pip install ftfy
```

3.  Download the DeepGlobe dataset and place the `train` folder of the
    dataset under the `scripts` folder so that you have the following
    structure:

<!-- -->

    mmsegmentation
    │
    └───scripts
    │   │
    │   └───train
    │       │
    │       └───x_mask.png
    │       │
    │       └───x_sat.jpg
    │       │
    │       └───...

4.  Run the data preparation script

```bash
cd scripts
python main.py
```

5.  Verify that you now have the following folder structure:

<!-- -->

    mmsegmentation
    │
    └───data
    │   │
    │   └───deep_globe
    │       │
    │       └───ann_dir
    |       |   |
    │       |   └───train
    │       |   |   │
    │       |   |   └───x_mask.png
    │       |   |   │
    │       |   |   └───...
    |       |   |
    │       │   └───val
    │       │       │
    │       │       └───y_mask.png
    │       │       │
    |       |       └───...
    │       └───img_dir
    |       |   |
    │       |   └───train
    │       |   |   │
    │       |   |   └───x_img.jpg
    │       |   |   │
    │       |   |   └───...
    |       |   |
    │       │   └───val
    │       │       │
    │       │       └───y_img.jpg
    │       │       │
    |       |       └───...

6.  Train the models Configs to pick from:

- Deeplab:
  `configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py`
- Unet: `configs/unet/unet-s5-d16_fcn_4xb4-40k_deepglobe-256x256.py`
- ResNet:
  `configs/resnest/resnest_s101-d8_deeplabv3_4xb2-40k_deepglobe-256x256.py`
- DeepLabPlus:
  `configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_deepglobe-256x256.py`
- CGNet: `configs/gcnet/gcnet_r50-d8_4xb2-40k_deeplab-256x256.py`
- IsaNet: `configs/isanet/isanet_r50-d8_4xb2-40k_deepglobe-252x252.py`

From the root folder of the project (`mmsegmentation/`), run the
following command:

```bash
python tools/train.py <path_to_config_file> --work-dir <path_to_work_dir> --resume
```

Note: the --work-dir and --resume flags are optional. The work-dir flag
specifies the directory where the logs and checkpoints will be saved.
The --resume flag is used to resume training from a checkpoint.

Example:

```bash
python tools/train.py configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py --work-dir work_dirs/deeplabv3 --resume
```

7.  To test the models, navigate to the tools folder

```bash
cd tools
```

8.  Create a folder for the model you want to test under the tools
    directory, and add contents to it so that. Additionally create an
    output folder, your structure should look like this (example for
    deeplab):

<!-- -->

    tools
    │
    └───deeplab
    │   │
    │   └───latest.pth
    │   │
    │   └───deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py
    │   │
    │   └───scalars.json
    │
    └───output
    |   |
    |   └───deeplab
    |       |
    |       └───graphs
    |       |
    |       └───predictions

Where:

- `latest.pth` is the latest checkpoint of the model
- `deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py` is the config file
  of the model
- `scalars.json` is the file that contains the metrics of the model

All of these will be generated after training the model under the
work-dir specified in the training command.

9.  Run the prediction script from inside the tools folder

```bash
cd tools
python predict.py --config <config_file> --weights <weights_file> --img <img_to_test> --out <output_folder>
```

Example:

```bash
python predict.py --config deeplab/deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py --weights deeplab/iter_10000.pth --img ../scripts/test/train1499_sat.jpg --out deeplab
```

This will generate a prediction for the image `train1499_sat.jpg` using
the model specified in the
`deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py` config file and the
`iter_10000.pth` checkpoint. The prediction will be saved in the
`deeplab/predictions` folder under the `output` folder.

Additionally, the script will generate a couple of graphs with the
metrics of the model under the `output/deeplab/graphs` folder.

# Google Colab setup

1.  Create a google colab file with the following contents:

```bash
# Install PyTorch
!pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
# Install MMCV
!pip install openmim
!mim install mmcv==2.1.0
import torch
```

2.  Change the colab runtime to use gpu

```bash
torch.cuda.is_available() # -> should return true
```

3.  Create a google drive folder called `models` in the root of your
    google drive account

4.  Add a zip file containing all the model images to the models folder
    inside Google drive so that the structure is:

```bash
/content/drive/MyDrive/models/deep_globe.zip
```

5.  Create a sub folder called `DeepGlobe` inside the models folder:

```bash
/content/drive/MyDrive/models/DeepGlobe
```

6.  Add the following to your colab file:

```bash
from google.colab import drive
drive.mount('/content/drive')

%cd /content
!git clone -b main https://github.com/marriagav/mmsegmentation.git
!pwd
!unzip /content/drive/MyDrive/models/deep_globe.zip -d /content/mmsegmentation/data

%cd /content/mmsegmentation
!pip install -v -e . && pip install ftfy
```

7.  Add the cells to train each model:

```bash
# Model 1:DeepLab
%cd /content/mmsegmentation
!python tools/train.py configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_deep-globe-256x256.py --work-dir /content/drive/MyDrive/models/DeepGlobe/DeepLab --resume

# Model 2:UNet
%cd /content/mmsegmentation
!python tools/train.py configs/unet/unet-s5-d16_fcn_4xb4-40k_deepglobe-256x256.py --work-dir /content/drive/MyDrive/models/DeepGlobe/UNet --resume

# Model 3:ResNet
%cd /content/mmsegmentation
!python tools/train.py configs/resnest/resnest_s101-d8_deeplabv3_4xb2-40k_deepglobe-256x256.py --work-dir /content/drive/MyDrive/models/DeepGlobe/ResNet --resume

# Model 4:DeepLabPlus
%cd /content/mmsegmentation
!python tools/train.py configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_deepglobe-256x256.py --work-dir /content/drive/MyDrive/models/DeepGlobe/DeepLabPlus --resume

# Model 5:CGNet
%cd /content/mmsegmentation
!python tools/train.py configs/gcnet/gcnet_r50-d8_4xb2-40k_deeplab-256x256.py --work-dir /content/drive/MyDrive/models/DeepGlobe/CGNet --resume

# Model 6:IsaNet
%cd /content/mmsegmentation
!python tools/train.py configs/isanet/isanet_r50-d8_4xb2-40k_deepglobe-252x252.py --work-dir /content/drive/MyDrive/models/DeepGlobe/IsaNet --resume
```

8.  This commands will train the models and save the checkpoints on your
    google drive
