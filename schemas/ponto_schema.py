"""_summary_"""
from typing import Optional, List

from pydantic import BaseModel as SCBaseModel

from .pessoal_schema import PessoalSchema
from .grade_schema import GradeSchema

class PontoSchemaBase(SCBaseModel):
    """_summary_"""
    nu_ponto: int
    template_digital: str
    block: bool
    arquiva:bool
    home_office: bool
    grade: List[GradeSchema]

    class Config:
        """_summary_"""
        orm_mode = True


class PontoSchemaPessoa(PontoSchemaBase):
    """_summary_"""
    pessoa: Optional[PessoalSchema]


class PontoSchemaBatida(SCBaseModel):
    """_summary_"""
    codigo: int
    