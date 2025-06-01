from sqlalchemy import Column, Integer, String, Float, JSON, Text, UUID
from app.db.base import Base
import uuid

class BeastDB(Base):
	__tablename__ = "beasts"

	id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
	name = Column(String, nullable=False)

	armor_class = Column(Integer, nullable=False)
	armor_desc = Column(String, nullable=True)

	hp = Column(Integer, nullable=False)
	hp_random = Column(String, nullable=True)

	strength = Column(Integer, nullable=False)
	dexterity = Column(Integer, nullable=False)
	constitution = Column(Integer, nullable=False)
	intelligence = Column(Integer, nullable=False)
	wisdom = Column(Integer, nullable=False)
	charisma = Column(Integer, nullable=False)

	save_throws = Column(JSON, nullable=True)
	skills = Column(JSON, nullable=True)

	damage_immune = Column(JSON, nullable=True)
	condition_immune = Column(JSON, nullable=True)

	senses = Column(JSON, nullable=True)
	languages = Column(JSON, nullable=True)

	cr = Column(Integer, nullable=False)
	proficiency_bonus = Column(Integer, nullable=False)

	actions = Column(JSON, nullable=True)
	bonus_actions = Column(JSON, nullable=True)
	reactions = Column(JSON, nullable=True)
	legendary_actions = Column(JSON, nullable=True)
	layer_actions = Column(JSON, nullable=True)

	description = Column(Text, nullable=True)
