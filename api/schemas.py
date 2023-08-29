from pydantic import BaseModel
from datetime import date

class CreateReport(BaseModel):

    start_date: date
    end_date: date
    status: str = "Generated"
    path: str = None

class GenerateReport(BaseModel):
    start_date: str
    end_date: str
