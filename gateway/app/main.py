from fastapi import FastAPI
from app.api import beasts

app = FastAPI()


app.include_router(beasts.router, prefix="/api/beasts", tags=["Beasts"])