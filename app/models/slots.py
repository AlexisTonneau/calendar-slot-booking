from sqlalchemy import Column, Integer, String, Date

from app.config.database import Base


class Slot(Base):
    __tablename__ = "slot"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
