from crud_app import __version__
from crud_app.run import app
# from fastapi.testclient import TestClient
from starlette.testclient import TestClient

client=TestClient(app)
def test_version():
    assert __version__ == "0.1.0"

def test_hello():
    response = client.get("/hello")
    assert response.status_code==200