"""_summary_"""
import datetime
from typing import Optional
from pydantic import BaseModel as SCBaseModel

class RelogioSchemaBase(SCBaseModel):
    """_summary_"""
    cd_num: int

    class Config:
        """_summary_"""
        orm_mode = True

class RelogioSchema(RelogioSchemaBase):
    """_summary_"""
    dt_data: datetime.date
    dt_hora: datetime.time
    valid:bool

class RelogioSchemaUp(SCBaseModel):
    """_summary_"""
    cd_num: int
    lat: Optional[float]
    lon: Optional[float]
    dist: Optional[float]
    home_office: Optional[bool]

    class Config:
        """_summary_"""
        orm_mode = True


class TimeSchema(SCBaseModel):
    """_summary_"""
    data: str
    hora: str
