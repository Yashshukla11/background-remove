import os
from rembg import remove
from PIL import Image

def process_images(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

        print(f"Processed {filename}")
input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'
process_images(input_folder, output_folder)
