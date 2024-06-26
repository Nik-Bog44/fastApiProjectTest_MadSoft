import uvicorn
from fastapi import FastAPI, File, UploadFile
from minio_utils import upload_file

app = FastAPI()


@app.post("/upload/")
async def create_upload_file(bucket: str, file: UploadFile = File(...)):
    file_data = await file.read()
    file_url = upload_file(bucket, file.filename, file_data)
    return {"file_url": file_url}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)