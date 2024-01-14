from fastapi import FastAPI
from .schemas import schema
from .utility.database import engine, session_local
from .models import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/")
def create(blog: schema.Blog):
    return blog
