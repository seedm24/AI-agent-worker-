from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to your first FastAPI app on Render!"}
