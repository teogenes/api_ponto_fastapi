# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.configs import settings


class PessoalModel(settings.DBBaseModel):
    """_summary_"""
    __tablename__ = 'tb_pessoal'

    id_pessoal: int = Column(Integer, primary_key=True, autoincrement=False)
    nm_nome: str = Column(String(256))
    digital = relationship("PontoModel", back_populates='pessoa', uselist=False,lazy='joined', primaryjoin="PontoModel.id_pessoal == PessoalModel.id_pessoal")
