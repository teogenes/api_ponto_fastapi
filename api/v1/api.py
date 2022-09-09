# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from fastapi import APIRouter

from api.v1.endpoints import ponto
from api.v1.endpoints import relogio
from api.v1.endpoints import seguranca
from core.utils import Tags

api_router = APIRouter()

#* ------------------------- Recursos ---------------------------------
api_router.include_router(ponto.router, prefix='/ponto', tags=[Tags.ponto])
api_router.include_router(relogio.router, prefix='/registro', tags=[Tags.registro])
api_router.include_router(seguranca.router, prefix='/seguranca', tags=[Tags.seguranca])
