"""
Retrieve and process image with the tesseract API
"""
import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import cv2
import numpy as np


def parse_image(filename):
    """ convert image with tesseract """
    image = get_image_from_file(filename)
    image = process_image(image)
    return pytesseract.image_to_string(image)


def process_image(image):
    """ Perform image processing """
    print('Processing image...')
    ret,img = cv2.threshold(np.array(image), 125, 255, cv2.THRESH_BINARY)
    return img

def get_image_from_url(url):
    """ open image as PIL object """
    img = Image.open(BytesIO(requests.get(url).content)).convert('L')
    return img

def get_image_from_file(filename):
    """ open image as PIL object from file system """
    return Image.open(filename).convert('L')


if __name__ == '__main__':
    print('parsing')
    parsed = parse_image('sample.png')
    print(parsed)
