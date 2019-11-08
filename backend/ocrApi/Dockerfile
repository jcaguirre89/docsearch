FROM tiangolo/uvicorn-gunicorn:python3.7
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y poppler-utils \
    && apt-get clean \
    && apt-get autoremove

EXPOSE 80

COPY ./app /app
WORKDIR /app/

RUN pip3 install -r requirements.txt
