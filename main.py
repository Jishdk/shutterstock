import cv2
import os
import glob

# Function to convert PNG to JPEG
def png_to_jpeg(png_file_path, jpeg_file_path):
    img = cv2.imread(png_file_path, cv2.IMREAD_UNCHANGED)
    cv2.imwrite(jpeg_file_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Function to upscale image to a minimum of 4MP
def upscale_to_4mp(jpeg_file_path, upscaled_file_path):
    img = cv2.imread(jpeg_file_path)
    target_pixels = 4 * 10**6
    height, width = img.shape[:2]
    current_pixels = height * width
    scale_factor = (target_pixels / current_pixels) ** 0.5
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(upscaled_file_path, resized_img)

# Directory where the PNG images are located
directory = "C:/Users/jishn/OneDrive/Bureaublad/Documenten 2023/Shutterstock"

# Process all PNG images in the directory
for png_file_path in glob.glob(os.path.join(directory, '*.png')):
    base_name = os.path.basename(png_file_path)
    file_name_without_ext = os.path.splitext(base_name)[0]

    # Paths for the new JPEG and upscaled images
    jpeg_file_path = os.path.join(directory, file_name_without_ext + '.jpeg')
    upscaled_file_path = os.path.join(directory, file_name_without_ext + '_4MP.jpeg')

    # Convert PNG to JPEG and then upscale to 4MP
    png_to_jpeg(png_file_path, jpeg_file_path)
    upscale_to_4mp(jpeg_file_path, upscaled_file_path)
