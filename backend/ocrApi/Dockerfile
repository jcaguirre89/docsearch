FROM tiangolo/uvicorn-gunicorn:python3.7
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    && apt-get clean \
    && apt-get autoremove

EXPOSE 80

COPY ./app /app
WORKDIR /app/

RUN pip3 install -r requirements.txt
