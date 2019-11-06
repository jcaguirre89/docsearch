## About
This project allows users to upload files and then search through them

## Tech stack
- An ElasticSearch database with the indexed files to provide fast search
- A data pipeline that receives uploaded files, sends the raw binary to S3, and 
also performs OCR with the Tesseract API and then uploads to the ES engine
- A React front-end that allows users to upload files, make a search and display results.
