from fastapi import FastAPI
from app.database import engine, Base
from app.routes import todo

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do API")

app.include_router(todo.router)


@app.get("/")
def read_root():
    return {"message": "To-Do API is running"}
