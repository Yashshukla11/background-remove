import os
from rembg import remove
from PIL import Image

def process_images(input_folder):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Only process files with valid image extensions
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            continue

        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)

            # Create the output filename
            base, ext = os.path.splitext(filename)
            output_filename = f"{base}_edited{ext}"
            output_path = os.path.join(input_folder, output_filename)

            # Save the edited image
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)

        print(f"Processed {filename}")

# Specify your input folder here
input_folder = 'path/to/your/input/folder'
process_images(input_folder)
