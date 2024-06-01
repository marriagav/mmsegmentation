from mmseg.apis import MMSegInferencer
import argparse
import os

def predict(model, weights, img_path, out_dir):
    inferencer = MMSegInferencer(model=model, weights=weights)
    result = inferencer(img_path, show=False, out_dir="./output/"+out_dir+"/predictions")
    return result

parser = argparse.ArgumentParser(description='Predict Image')
parser.add_argument(
    '--config',
    type=str,
    help='path of config file')
parser.add_argument(
    '--weights',
    type=str,
    help='path of weights')
parser.add_argument(
    '--img',
    type=str,
    help='path of image')
parser.add_argument(
    '--out',
    type=str,
    help='path of output directory')
args = parser.parse_args()

def main():
    predict(args.config, args.weights, args.img, args.out)
    os.system(f"python analysis_tools/analyze_logs.py {args.out}/scalars.json --keys mIoU mAcc aAcc --legend mIoU mAcc aAcc --out ./output/{args.out}/graphs/iou_acc")
    os.system(f"python analysis_tools/analyze_logs.py {args.out}/scalars.json --keys loss --legend loss --out tools/output/deeplab/graphs/loss --out ./output/{args.out}/graphs/loss")
    os.system(f"python analysis_tools/analyze_logs.py {args.out}/scalars.json --keys decode.acc_seg aux.acc_seg --legend decode.acc_seg aux.acc_seg --out ./output/{args.out}/graphs/acc")

if __name__ == '__main__':
    main()
