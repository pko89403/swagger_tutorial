from pydantic import BaseModel 


class HistoryItem(BaseModel):
    data: str

class PredictItem(BaseModel):
    carat_weight: str 
    cut: str 
    color: str
    clarity: str 
    polish: str
    symmetry: str 
    report: str