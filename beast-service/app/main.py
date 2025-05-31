from fastapi import FastAPI
from app.api.beasts import router as beast_router

app = FastAPI()
app.include_router(beast_router)

