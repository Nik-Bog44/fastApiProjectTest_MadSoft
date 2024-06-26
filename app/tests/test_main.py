from unittest.mock import patch

from starlette.testclient import TestClient
from app.main import app

# Определяем тестовый клиент для FastAPI
client = TestClient(app)


@patch('app.crud.create_meme')  # Мокируем функцию create_meme
def test_create_meme(mock_create_meme):
    # Задаем поведение мокированной функции create_meme
    mock_create_meme.return_value = {
        "id": 1,
        "title": "Funny Meme",
        "description": "This is a funny meme",
        "image_url": "http://minio:9000/bucketname/filename"
    }

    # Отправляем POST-запрос к /memes с данными мема
    meme_data = {
        "id": 1,
        "title": "Funny Meme",
        "description": "This is a funny meme",
        "image_url": "http://minio:9000/bucketname/filename"
    }
    response = client.post("/memes", json=meme_data)

    # Проверяем, что возвращается ожидаемый JSON с данными мема
    expected_json = {
        "id": 1,
        "title": "Funny Meme",
        "description": "This is a funny meme",
        "image_url": "http://minio:9000/bucketname/filename"
    }
    assert response.json() == expected_json
