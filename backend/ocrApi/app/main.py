from fastapi import FastAPI, File, UploadFile
from ocr import parse_pdf, parse_image, get_image_from_bytes

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello World!"
    return {"message": message}


@app.post("/upload-file/")
async def upload_image(file: bytes = File(...)):
    image = get_image_from_bytes(file)
    parsed = parse_image(image)
    return {"parsed": parsed}


@app.post("/upload-pdf/")
async def upload_pdf(file: bytes = File(...)):
    parsed = parse_pdf(file)
    return {"parsed": parsed}
