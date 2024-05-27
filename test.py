import os
from rembg import remove
from PIL import Image

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Check if the file is an image
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            continue

        # Open the image
        with Image.open(input_path) as input_image:
            input_data = input_image.tobytes()

            # Process the image to remove background
            output_data = remove(input_data)

            # Convert output data back to an image
            output_image = Image.frombytes(input_image.mode, input_image.size, output_data)

            # Save the processed image
            output_image.save(output_path)

        print(f"Processed {filename}")

# Specify your input and output folders
input_folder = 'path/to/your/input/folder'
output_folder = 'path/to/your/output/folder'

process_images(input_folder, output_folder)
