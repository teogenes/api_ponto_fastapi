# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text, String
from sqlalchemy.orm import relationship
from core.configs import settings
from .pessoal_model import PessoalModel
from .grade_model import GradeModel

class PontoModel(settings.DBBaseModel):
    """_summary_"""
    __tablename__ = 'tb_ponto_pessoa'

    id_ponto: int = Column(Integer, primary_key=True, autoincrement=True)
    id_pessoal: int = Column(Integer, ForeignKey('tb_pessoal.id_pessoal'))
    id_grade: int = Column(Integer, ForeignKey('tb_ponto_grade.id_grade'))
    nu_ponto: int = Column(Integer)
    bonus: bool= Column(Boolean, default=False)
    block: bool= Column(Boolean, default=False)
    compensa: bool= Column(Boolean, default=False)
    template_digital: str = Column(Text)
    arquiva: bool = Column(Boolean, default=False)
    home_office: bool = Column(Boolean, default=False)
    cel_id: str = Column(String(100))
    pessoa = relationship("PessoalModel", back_populates='digital', uselist=False, lazy='joined', primaryjoin="PontoModel.id_pessoal == PessoalModel.id_pessoal")
    grade = relationship("GradeModel", uselist=True, lazy='selectin')
