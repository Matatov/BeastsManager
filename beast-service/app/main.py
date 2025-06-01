from fastapi import FastAPI
from app.api.beasts import router as beast_router
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(beast_router)

