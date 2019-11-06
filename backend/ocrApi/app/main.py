from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    message = f"Hello!"
    return {"message": message}
