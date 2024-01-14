from fastapi import FastAPI
from typing import Optional
from .models import Item
from blog.models import Blog


app = FastAPI()

# @app.get("/")
# def index():
#     return {"blog_list": []}


@app.post("/")
def create(blog: Blog):
    return blog


@app.get("/about")
def about():
    return {"page": "about page"}


@app.get("/blog/{id}")
def blog_by_id(id: int):
    return {"blog": id}


@app.get("/")
def get_first_n_blogs(
    limit: int = 20, published: bool = True, sort: Optional[str] = None
):
    if published:
        return {"data": f"first {limit} published blogs from blog_list"}
    return {"data": f"first {limit} unpublished blogs from blog_list"}


@app.post("/")
def create_blog(item: Item):
    return item
