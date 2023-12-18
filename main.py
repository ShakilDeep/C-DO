from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud, schemas
from .database import SessionLocal, engine
from .middlewares import CustomMiddleware

app = FastAPI()

# Middleware
app.add_middleware(CustomMiddleware)

# CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Add your routes here
```
