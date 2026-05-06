from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "To-Do API is running"}
