"""_summary_"""
import datetime

from pydantic import BaseModel as SCBaseModel

class GradeSchema(SCBaseModel):
    """_summary_"""
    id_grade: int
    in1: datetime.time
    out1: datetime.time
    in2: datetime.time
    out2: datetime.time

    class Config:
        """_summary_"""
        orm_mode = True
