import io
import os

import requests
from PIL import Image

# Secret API key for ClipDrop
API_KEY = 'place_api_key_here'

# define a global variable to store the filename
global filename
global filename_extension
global image_file_object

def get_image_filename():
    global filename
    global filename_extension
    print("Please type the name of a jpg file you would like processing")
    filename = input("Enter a filename: ")
    filename_extension = f"{filename}.jpg"
    print("The current filename is:", filename_extension)

def load_image():
    global filename_extension
    global image_file_object
    # Load image file with pillow
    # and convert to byte array
    with Image.open(filename_extension) as input:
        image_file_object = image_to_byte_array(input)

def image_to_byte_array(image:Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

def process_image_depth():
    # ClipDrop API request depth estimation
    r = requests.post('https://clipdrop-api.co/portrait-depth-estimation/v1',
                      files=
                      {
                          'image_file': ('portrait.jpg', image_file_object, 'image/jpeg'),
                      },
                      headers=
                      {
                          'x-api-key': API_KEY
                      })
    if (r.ok):
        # r.content contains the bytes of the returned image
        image = Image.open(io.BytesIO(r.content))

        filename_depth = f"{filename}_Depth.jpg"
        image.save(filename_depth)
        print(f'Saved Depth Map')
    else:
        r.raise_for_status()

def process_image_normal():
    # ClipDrop API request surface normal estimation
    n = requests.post('https://clipdrop-api.co/portrait-surface-normals/v1',
                      files=
                      {
                          'image_file': ('portrait.jpg', image_file_object, 'image/jpeg'),
                      },
                      headers=
                      {
                          'x-api-key': API_KEY
                      })
    if (n.ok):
        # n.content contains the bytes of the returned image
        image_n = Image.open(io.BytesIO(n.content))

        filename_normal = f"{filename}_Normal.jpg"
        image_n.save(filename_normal)
        print(f'Saved Normal Map')
    else:
        n.raise_for_status()


def main():
    while True:
        get_image_filename()

        if os.path.exists(filename_extension) and os.path.isfile(filename_extension):
            break
        else:
            print("Filename is incorrect, please try again")

    load_image()
    print(filename_extension, "has been converted to byte array")

    print(f'Starting ClipDrop API Requests for', filename_extension)
    process_image_depth()
    process_image_normal()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
