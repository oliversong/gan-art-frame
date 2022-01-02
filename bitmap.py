from PIL import Image
import os

def resize_image(im):
    # resize from 960 × 1568 pixels
    # to 448 x whatever
    return im.resize((448, 1286))

def crop_image(im):
    # crop from center to 448 x 600 ratio
    return im.crop((0, 343, 448, 943))

def make_bitmap():
    im = Image.open(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'raw.jpg'
        )
    )
    resized = resize_image(im)
    cropped = crop_image(resized)
    cropped.save('bitmap.bmp', 'BMP')
