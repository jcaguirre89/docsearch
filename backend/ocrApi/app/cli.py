import sys
import requests
import pytesseract
from PIL import Image
from io import BytesIO
from ocr import get_image_from_file, process_image


if __name__ == "__main__":
    """Tool to test the raw output of pytesseract with a given input URL"""
    sys.stdout.write(
        """
===OOOO=====CCCCC===RRRRRR=====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RR===RR====\n
==OO==OO===CC=======RRRRRR=====\n
==OO==OO===CC=======RR==RR=====\n
==OO==OO===CC=======RR== RR====\n
===OOOO=====CCCCC===RR====RR===\n\n
"""
    )
    sys.stdout.write("A simple OCR utility\n")
    filename = input("What is the name of the image you would like to analyze?\n")
    image = get_image_from_file(filename)
    image = process_image(image)
    print(image)
    sys.stdout.write("The raw output from tesseract with no processing is:\n\n")
    sys.stdout.write("-----------------BEGIN-----------------\n")
    sys.stdout.write(pytesseract.image_to_string(image, lang='eng') + "\n")
    sys.stdout.write("------------------END------------------\n")
