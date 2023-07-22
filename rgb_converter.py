import os
import cv2

def convert_grayscale_to_rgb(input_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            image_path = os.path.join(root, file)
            image = cv2.imread(image_path)
            if len(image.shape) == 2:
                # Convert grayscale to RGB by replicating the single channel
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                # Save the updated RGB image
                cv2.imwrite(image_path, image)

def check_image_dimensions(dataset_folder):
    for root, _, files in os.walk(dataset_folder):
        for file in files:
            image_path = os.path.join(root, file)
            image = cv2.imread(image_path)
            if image is not None:
                height, width, channels = image.shape
                print(f"Image: {file}, Dimensions: {height}x{width}, Channels: {channels}")

# Replace grayscale images in the 'dataset_folder' with RGB versions
dataset_folder = '/path/to/your/dataset_folder'
convert_grayscale_to_rgb(dataset_folder)

# Check dimensions of images in the 'dataset_folder'
check_image_dimensions(dataset_folder)

