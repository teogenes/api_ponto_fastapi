# pylint: disable=C0116 E0401 w0611
import datetime
from sqlalchemy import Column, Integer, Time
from core.configs import settings


class GradeModel(settings.DBBaseModel):
    """_summary_"""
    __tablename__ = 'tb_ponto_grade'

    id_grade: int = Column(Integer, primary_key=True, autoincrement=True)
    in1: datetime.time = Column(Time)
    out1: datetime.time = Column(Time)
    in2: datetime.time = Column(Time)
    out2: datetime.time = Column(Time)
