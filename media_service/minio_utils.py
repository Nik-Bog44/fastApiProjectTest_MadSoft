from minio import Minio
import os

MINIO_URL = os.getenv("MINIO_URL", "localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")

client = Minio(MINIO_URL,
               access_key=MINIO_ACCESS_KEY,
               secret_key=MINIO_SECRET_KEY,
               secure=False)


def upload_file(bucket_name: str, file_name: str, file_data: bytes):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    client.put_object(bucket_name, file_name, file_data, len(file_data))
    return f"{MINIO_URL}/{bucket_name}/{file_name}"


def get_file_url(bucket_name: str, file_name: str) -> str:
    return f"{MINIO_URL}/{bucket_name}/{file_name}"
