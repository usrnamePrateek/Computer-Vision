from modules.ig import ImageSegmentation
import argparse

parser = argparse.ArgumentParser()
default_image_path = 'data/mountain.jpeg'

# Add command-line arguments
parser.add_argument("--image-path", help="path of the image you would like to use for Image segmentation, default: /data/mountain.jpeg")

args = parser.parse_args()

if __name__ == "__main__":
    print("running image segmentation....")

    if args.image_path is None:
        print("no image path provided using the default image....")
        ImageSegmentation(default_image_path).runProcess()
    else:
        print(f"using image path {args.image_path} for the process")
        ImageSegmentation(args.image_path).runProcess()

    print("stopped the process.")
