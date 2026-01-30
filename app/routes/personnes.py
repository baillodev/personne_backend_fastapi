from fastapi import APIRouter, HTTPException
from typing import List
from app.services.personnes_service import create_personne, fetch_personnes, update_personne, remove_personne
from app.models.personne import Personne, PersonneDelete

router = APIRouter(prefix="/personnes", tags=["Personnes"])

@router.post("")
def create_personne_route(payload: Personne):
    try:
        create_personne(payload)
        return {"success": True, "message": "Personne créée"}
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur serveur")

@router.get("", response_model=List[Personne])
def get_personnes():
    try:
        return fetch_personnes()
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur serveur")

@router.put("/{id}")
def update_personne_route(id: int, payload: Personne):
    try:
        update_personne(id, payload)
        return {"success": True, "message": "Personne mise à jour"}
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur serveur")

@router.post("/delete")
def delete_personne(payload: PersonneDelete):
    try:
        remove_personne(payload.id)
        return {"success": True, "message": "Suppression effectuée"}
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur serveur")
