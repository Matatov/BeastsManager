import uuid
from http.client import HTTPException

from fastapi import APIRouter, Query
from fastapi.params import Depends
from uuid import UUID
from sqlalchemy.orm import Session

from ..db.beast import BeastDB
from ..db.session import get_db
from ..models.beast import Beast



router = APIRouter()


@router.get("/beasts", response_model=list[Beast])
def get_beasts(db: Session = Depends(get_db)):
    beasts = db.query(BeastDB).all()
    return beasts


@router.get("/beasts/{beast_id}", response_model=None)
def get_beast(beast_id: UUID, db: Session = Depends(get_db)):
    beast = db.query(BeastDB).filter(BeastDB.id == str(beast_id)).first()
    return beast

@router.post("/beasts", response_model=Beast, status_code=201)
def insert_beast(beast: Beast, db: Session = Depends(get_db)):
    db_beast = BeastDB(
        id=str(uuid.uuid4()),
        **beast.model_dump(exclude={"id"})
    )
    db.add(db_beast)
    db.commit()
    db.refresh(db_beast)
    return db_beast

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
    pass

# @router.update("/beasts/{beast_id}")
# def update_beast(beast_id: int, db: Session = Depends(get_db)):
#     pass

#     results = fake_beasts
#
#     if name:
#         results = [b for b in results if name.lower() in b.name.lower()]
#     if armor_class:
#         results = [b for b in results if armor_class == armor_class]
#     if strength:
#         results = [b for b in results if strength == b.strength]
#     if dexterity:
#         results = [b for b in results if dexterity == b.dexterity]
#     if constitution:
#         results = [b for b in results if constitution == b.constitution]
#     if intelligence:
#         results = [b for b in results if intelligence == b.intelligence]
#     if wisdom:
#         results = [b for b in results if wisdom == b.wisdom]
#     if charisma:
#         results = [b for b in results if charisma == b.charisma]
#     if cr:
#         results = [b for b in results if cr == b.cr]
#
#     return results