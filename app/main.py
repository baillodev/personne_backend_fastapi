from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.personnes import router as personnes_router

app = FastAPI(title="Personne API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(personnes_router)