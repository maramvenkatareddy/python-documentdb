from pydantic import BaseModel
from typing import Optional, List

class Item(BaseModel):
    CloudTechnology: str
    description: Optional[str] = None
    MarketValue: float

class ItemInDB(Item):
    id: str
