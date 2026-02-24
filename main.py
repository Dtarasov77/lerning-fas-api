from fastapi import FastAPI
import uvicorn


app = FastAPI(openapi_version="3.0.0")

@app.get("/")
def func():
    return 'hello world'


if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
