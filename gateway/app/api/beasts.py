from fastapi import APIRouter, Request
import httpx
from app.config import BEAST_SERVICE_URL

router = APIRouter()


@router.get("/")
async def list_beasts():
	async with httpx.AsyncClient() as client:
		response = await client.get(f"{BEAST_SERVICE_URL}/beasts")
		return response.json()


@router.get("/{beast_id}")
async def get_beast(beast_id: int):
	async with httpx.AsyncClient() as client:
		response = await client.get(f"{BEAST_SERVICE_URL}/beasts/{beast_id}")
		return response.json()


@router.post("/")
async def create_beast(request: Request):
	data = await request.json()
	async with httpx.AsyncClient() as client:
		response = await client.post(f"{BEAST_SERVICE_URL}/beasts", json=data)
		return response.json()
