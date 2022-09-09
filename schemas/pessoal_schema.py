"""_summary_"""
from typing import Optional

from pydantic import BaseModel as SCBaseModel

class PessoalSchema(SCBaseModel):
    """_summary_"""
    id_pessoal: Optional[int] = None
    nm_nome: str

    class Config:
        """_summary_"""
        orm_mode = True
