from fastapi import APIRouter

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
