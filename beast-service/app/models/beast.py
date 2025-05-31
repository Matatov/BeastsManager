from enum import Enum

from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date

class Characteristic(Enum):
	strength = "Strength"
	dexterity = "Dexterity"
	constitution = "Constitution"
	intelligence = "Intelligence"
	wisdom = "Wisdom"
	charisma = "Charisma"

class Skill(Enum):
	acrobatics = "Acrobatics"
	animal_handling = "Animal Handling"
	Arcana = "Arcana"
	Athletics = "Athletics"
	Deception = "Deception"
	History = "History"
	insight = "Insight"
	intimidation = "Intimidation"
	investigation = "Investigation"
	medicine = "Medicine"
	nature = "Nature"
	perception = "Perception"
	performance = "Performance"
	persuasion = "Persuasion"
	religion = "Religion"
	sleight_of_hand = "Sleight of Hand"
	survival = "Survival"


class Beast(BaseModel):
	id: int
	name: str
	armor_class: int
	armor_desc: Optional[str] = None
	hp: int
	hp_random: Optional[str] = None
	strength: int
	dexterity: int
	constitution: int
	intelligence: int
	wisdom: int
	charisma: int
	save_throws: Optional[List[str]] = None
	skills: Optional[List[str]] = None
	damage_immune: Optional[str] = None
	condition_immune: Optional[str] = None
	senses: Optional[List[str]] = None
	languages: Optional[List[str]] = None
	cr: int
	proficiency_bonus: int
	actions: Optional[List[str]] = None
	bonus_actions: Optional[List[str]] = None
	reactions: Optional[List[str]] = None
	legendary_actions: Optional[List[str]] = None
	layer_actions: Optional[List[str]] = None
	description: Optional[str] = None
