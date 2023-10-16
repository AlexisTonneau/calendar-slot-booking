from fastapi import FastAPI, Depends
import uvicorn as uvicorn
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from uvicorn.config import LOGGING_CONFIG
import os

from app.config.service_loader import init_services
from app.config.database import Base, engine, SessionLocal
from app.models.slot_input import SlotInput

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

services = init_services()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def get_slots(db: Session = Depends(get_db)):
    return services.booking_service.get_all_slots(db)


@app.post("/")
async def create_slot(slot: SlotInput, db: Session = Depends(get_db)):
    return services.booking_service.create_slot(db, slot)


@app.delete("/{slot_id}")
async def delete_slot(slot_id: int, db: Session = Depends(get_db)):
    return services.booking_service.delete_slot(db, slot_id)

if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')) or 9000)
