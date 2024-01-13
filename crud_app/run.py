from typing import Union
import uvicorn


from .main import app
from . import __version__

@app.get("/hello")
def read_root():
    return {"Version": __version__}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("crud_app.run:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()