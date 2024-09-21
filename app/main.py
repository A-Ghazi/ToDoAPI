from fastapi import FastAPI
from app.database import engine, Base
from app.routes import todos

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)