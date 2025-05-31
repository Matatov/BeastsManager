from http.client import HTTPException

from fastapi import APIRouter, Query

from ..models.beast import Beast

# from app.models.beast import Beast, Characteristic

router = APIRouter()

# Dummy in-memory data
fake_beasts = [
    Beast(
        id=1,
        name="Dire Wolf",
        cr=6,
        armor_class=15,
        hp=100,
        strength=15,
        dexterity=18,
        constitution=15,
        intelligence=10,
        wisdom=12,
        charisma=11,
        proficiency_bonus=4
    ),
    Beast(
        id=2,
        name="Sukkub",
        cr=6,
        armor_class=15,
        hp=100,
        strength=10,
        dexterity=11,
        constitution=15,
        intelligence=18,
        wisdom=14,
        charisma=19,
        proficiency_bonus=4
    ),

]

@router.get("/beasts", response_model=list[Beast])
def get_beasts():
    return fake_beasts


@router.get("/beasts/{beast_id}",response_model=Beast)
def get_beast(beast_id: int):
    for beast in fake_beasts:
        if beast.id == beast_id:
            return beast
    raise HTTPException()


@router.get("/beasts/search", response_model=list[Beast])
def search_beasts(
        name: str = Query(default=None, description="Partial match of name"),
        armor_class: int = Query(default=None, description=""),
        strength: int = Query(default=None, description=""),
        dexterity: int = Query(default=None, description=""),
        constitution: int = Query(default=None, description=""),
        intelligence: int = Query(default=None, description=""),
        wisdom: int = Query(default=None, description=""),
        charisma: int = Query(default=None, description=""),
        cr: int = Query(default=None, description=""),
):
    results = fake_beasts

    if name:
        results = [b for b in results if name.lower() in b.name.lower()]
    if armor_class:
        results = [b for b in results if armor_class == armor_class]
    if strength:
        results = [b for b in results if strength == b.strength]
    if dexterity:
        results = [b for b in results if dexterity == b.dexterity]
    if constitution:
        results = [b for b in results if constitution == b.constitution]
    if intelligence:
        results = [b for b in results if intelligence == b.intelligence]
    if wisdom:
        results = [b for b in results if wisdom == b.wisdom]
    if charisma:
        results = [b for b in results if charisma == b.charisma]
    if cr:
        results = [b for b in results if cr == b.cr]

    return results