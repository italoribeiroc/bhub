from typing import List
from pydantic import BaseModel
from .bankData import BankData

class User(BaseModel):
    social_reason: str
    telephone: str
    address: str
    register_date: str
    bank_data: List[BankData]