"""_summary_"""
from pydantic import BaseModel as SCBaseModel

class AutenticacaoSchema(SCBaseModel):
    """_summary_"""
    codigo: int
    password: str

    class Config:
        """_summary_"""
        orm_mode = True


class RegistroSchemaUp(SCBaseModel):
    """_summary_"""
    nu_ponto: int
    cel_id: str

    class Config:
        """_summary_"""
        orm_mode = True


class RegistroSchemaResponse(SCBaseModel):
    """_summary_"""
    nu_ponto: int
