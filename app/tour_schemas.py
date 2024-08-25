from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime
from typing import Optional, List

class NewProduct(BaseModel):
    name: str
    description: str
    price: float
    cover_url: str
    quantity: int

class CreatedProduct(NewProduct):
    id: int
    created_at: datetime

class UpdateProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    cover_url: Optional[str] = None
    quantity: Optional[int] = None

class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
    name: str

class BaseUserInfo(BaseModel):
    user_uuid: uuid.UUID
    email: EmailStr
    name: str

class RegisterVisitorRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
