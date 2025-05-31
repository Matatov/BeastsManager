# from enum import Enum
#
# from pydantic import BaseModel, Field, validator
# from typing import List, Optional
# from datetime import date
#
# class Characteristic(Enum):
# 	strength = "Strength"
# 	dexterity = "Dexterity"
# 	constitution = "Constitution"
# 	intelligence = "Intelligence"
# 	wisdom = "Wisdom"
# 	charisma = "Charisma"
#
# class Skill(Enum):
# 	acrobatics = "Acrobatics"
# 	animal_handling = "Animal Handling"
# 	Arcana = "Arcana"
# 	Athletics = "Athletics"
# 	Deception = "Deception"
# 	History = "History"
# 	insight = "Insight"
# 	intimidation = "Intimidation"
# 	investigation = "Investigation"
# 	medicine = "Medicine"
# 	nature = "Nature"
# 	perception = "Perception"
# 	performance = "Performance"
# 	persuasion = "Persuasion"
# 	religion = "Religion"
# 	sleight_of_hand = "Sleight of Hand"
# 	survival = "Survival"
#
#
# class Beast(BaseModel):
# 	id: int
# 	name: str
# 	armor_class: int
# 	armor_desc: Optional[str]
# 	hp: int
# 	hp_random: Optional[str]
# 	strength: int
# 	dexterity: int
# 	constitution: int
# 	intelligence: int
# 	wisdom: int
# 	charisma: int
# 	save_throws: Optional[List[str]]
# 	skills: Optional[List[str]]
# 	damage_immune: Optional[str]
# 	condition_immune: Optional[str]
# 	senses: Optional[List[str]]
# 	languages: Optional[List[str]]
# 	cr: int
# 	proficiency_bonus: int
# 	actions: Optional[List[str]]
# 	bonus_actions: Optional[List[str]]
# 	reactions: Optional[List[str]]
# 	legendary_actions: Optional[List[str]]
# 	layer_actions: Optional[List[str]]
# 	description: Optional[str]
