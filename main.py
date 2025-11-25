import uvicorn

if __name__ == "main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)