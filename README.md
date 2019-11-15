[WIP]

## About
This project allows users to upload files and then search through them

## Running locally
```
git clone git@github.com:jcaguirre89/docsearch.git
cd docsearch
docker-compose up --build
```

now go to `localhost:5001` for the OCR API

## (Planned) Tech stack
- An ElasticSearch or PostgreSQL database with the indexed files to provide fast search
- A data pipeline that receives uploaded files, sends the raw binary to S3, and 
also performs OCR with the Tesseract API and then uploads to the ES engine
- A React front-end that allows users to upload files, make a search and display results.

## Milestones
- [x] Tesseract OCR API
- [ ] Persistent data store to index and search documents (Postgres or Elasticsearch)
- [ ] Front end
- [ ] Data pipeline to connect services
