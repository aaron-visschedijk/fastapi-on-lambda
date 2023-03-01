from fastapi.testclient import TestClient

from ..app.v1 import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API v1 is live!"}