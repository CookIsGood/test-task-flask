from pydantic import BaseModel


class AnimalOut(BaseModel):
    id: int
    name: str
    type: str
    speed: int
