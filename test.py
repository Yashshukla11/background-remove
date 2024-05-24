import os
from rembg import remove
from PIL import Image

def process_images(input_folders, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_folder in input_folders:
        if not os.path.exists(input_folder):
            print(f"Warning: Input folder '{input_folder}' does not exist.")
            continue

        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
                continue

            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)

                with open(output_path, 'wb') as output_file:
                    output_file.write(output_data)

            print(f"Processed {filename} from {input_folder}")

input_folders = ['/Users/yashshukla/Desktop/images', '/Users/yashshukla/Desktop/img']
output_folder = '/Users/yashshukla/Desktop/image'
process_images(input_folders, output_folder)
