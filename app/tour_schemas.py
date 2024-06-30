from pydantic import BaseModel, Field
from datetime import date

class TourBase(BaseModel):
    start_date: date
    end_date: date
    price: float = Field(..., gt=0)
    country: str = Field(..., max_length=50)
    hotel_class: str = Field(..., max_length=20)
    description: str = Field(None, max_length=255)

class TourCreate(TourBase):
    pass

class Tour(TourBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
