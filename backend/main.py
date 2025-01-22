from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace '*' with your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve React frontend
app.mount("/", StaticFiles(directory="build", html=True), name="static")

# Example API route
@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI!"}

