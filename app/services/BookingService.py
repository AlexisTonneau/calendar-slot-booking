from sqlalchemy.orm import Session

from app.models.slot_input import SlotInput
from app.models.slots import Slot


class BookingService:

    def __init__(self) -> None:
        pass

    def create_slot(self, db: Session, payload: SlotInput):
        slot = Slot(name=payload.name, end=payload.end, start=payload.start)
        db.add(slot)
        db.commit()
        db.refresh(slot)
        return slot

    def get_all_slots(self, db: Session):
        return db.query(Slot).all()

    def delete_slot(self, db: Session, slot_id: str):
        slot_to_remove = db.query(Slot).filter(Slot.id == slot_id).first()
        db.delete(slot_to_remove)
        db.commit()

