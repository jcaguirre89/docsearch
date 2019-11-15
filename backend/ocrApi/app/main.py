from fastapi import FastAPI, File, BackgroundTasks, Form, UploadFile
from ocr import convert_pdf_to_image, parse_image, get_image_from_bytes


app = FastAPI()


def parse_pdf(file: bytes, lang: str):
    """ turn pdf into image and call tesseract API """
    print('Starting to parse pdf')
    out = {}
    images = convert_pdf_to_image(file)
    for idx, image in enumerate(images):
        print(f"Parsing page {idx}")
        out[f"page {idx}"] = parse_image(image, lang)
    return out


def parse_file(input_file: bytes, lang: str):
    """ route to approriate parsing function """
    print(f'Parsing file {input_file.filename}')
    file_content = input_file.file.read()
    extension = input_file.filename.split('.')[-1]
    if extension.lower() in ['jpg', 'jpeg', 'png']:
        print('image file')
        image = get_image_from_bytes(file_content)
        parsed = parse_image(image, lang)
        print(parsed)
        return {'parsed': parsed}
    elif extension.lower() in ['pdf']:
        print('PDF file')
        # TODO: check if file is searcheable or not
        parsed = parse_pdf(file_content, lang)
        print(parsed)
        return {'parsed': parsed}
    else:
        return {'message': 'invalid file extension'}


@app.get("/")
async def read_root():
    message = f"Hello World!"
    return {"message": message}


@app.post("/upload/")
async def upload(
    background_tasks: BackgroundTasks,
    file_input: UploadFile = File(...),
    lang: str = Form("eng"),
):
    """ Main entrypoint for file uploads """
    # TODO: figure out file extension and call appropriate task
    parsed = background_tasks.add_task(parse_file, file_input, lang)
    return {"message": 'Upload Successful!'}


@app.post("/upload-file/")
async def upload_image(file: bytes = File(...)):
    image = get_image_from_bytes(file)
    parsed = parse_image(image)
    return {"parsed": parsed}


@app.post("/upload-pdf/")
async def upload_pdf(file: bytes = File(...)):
    parsed = parse_pdf(file)
    return {"parsed": parsed}
