from pydantic import BaseModel
from typing import Optional

class Personne(BaseModel):
    id: Optional[int]
    nom: str
    prenom: str
    age: int
    photo: Optional[str]

class PersonneDelete(BaseModel):
    id: int
