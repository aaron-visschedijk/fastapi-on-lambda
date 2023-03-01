from fastapi.testclient import TestClient

from ..app.v1.authentication import endpoints as auth

client = TestClient(auth)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Auth module is live!"}
