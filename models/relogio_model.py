# pylint: disable=C0116 E0401
"""_summary_"""
import datetime
from sqlalchemy import Column, Integer, Date, Time, String, Boolean, Float
from core.configs import settings


class RelogioModel(settings.DBBaseModel):
    """_summary_"""
    __tablename__ = 'tb_ponto_dados_relogio'
    cd_num: int = Column(Integer, primary_key=True)
    dt_data: datetime.date = Column(Date, primary_key=True)
    dt_hora: datetime.time = Column(Time, primary_key=True)
    lat: float = Column(Float, default=0.0)
    lon: float = Column(Float, default=0.0)
    dist: float = Column(Float, default=0.0)
    home_office: bool = Column(Boolean, default=False)
    __valid: bool = False

    @property
    def valid(self):
        """_summary_"""
        return self.__valid

    @valid.setter
    def valid(self, valid: bool):
        self.__valid = valid
