"""
Retrieve and process image with the tesseract API
"""
import tempfile
import requests
import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import cv2
import numpy as np
from pdf2image import convert_from_bytes


def convert_pdf_to_image(file: bytes):
    """ Returns a list of Image objects """
    print("Converting PDF to image")
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_bytes(file, output_folder=path)
    return images


def parse_pdf(file: bytes):
    """ Parses pdf file with tesseract """
    out = {}
    images = convert_pdf_to_image(file)
    for idx, image in enumerate(images):
        print(f"Parsing page {idx}")
        out[f"page {idx}"] = parse_image(image)
    return out


def parse_image(image, lang='eng'):
    """ convert PIL Image with tesseract """
    image = process_image(image)
    print(f'language: {lang}')
    return pytesseract.image_to_string(image, lang=lang)


def process_image(image):
    """ Perform image processing """
    print("Processing image...")
    _, img = cv2.threshold(np.array(image), 125, 255, cv2.THRESH_BINARY)
    return img


def get_image_from_url(url):
    """ open image as PIL object """
    img = Image.open(BytesIO(requests.get(url).content)).convert("L")
    return img


def get_image_from_bytes(file: bytes):
    """ open image from file object as PIL object """
    return Image.open(BytesIO(file)).convert("L")


def get_image_from_file(filename):
    """ open image as PIL object from file system """
    return Image.open(filename).convert("L")


if __name__ == "__main__":
    print("parsing")
    parsed = parse_image("sample.png")
    print(parsed)
