from typing import Union

from pydantic import BaseModel


class SlotInput(BaseModel):
    id: Union[int, None] = None
    name: str
    start: str
    end: str
