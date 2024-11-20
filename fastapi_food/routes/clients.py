from fastapi import APIRouter, HTTPException
from fastapi_food.models import Client
from fastapi_food.database import SessionLocal

router = APIRouter()

@router.get("/clients")
def get_clients():
    db = SessionLocal()
    clients = db.query(Client).all()
    return clients

@router.post("/clients")
def create_client(client: Client):
    db = SessionLocal()
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.put("/clients/{client_id}")
def update_client(client_id: int, client: Client):
    db = SessionLocal()
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client.name = client.name
    db_client.email = client.email
    db.commit()
    db.refresh(db_client)
    return db_client
