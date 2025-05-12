from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Docker app running on port 8000!"}
