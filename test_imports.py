# test_imports.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()






# Allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Try allowing all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Imports successful!")