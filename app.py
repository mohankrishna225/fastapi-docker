from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():

return { "Hello World": "Welcome to MLOps Training" }

