# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import AuthHandler
from schemas.ponto_schema import PontoSchemaPessoa
from schemas.relogio_schema import RelogioSchemaUp
from core.deps import get_session
from repositories.ponto_repository import get_pessoal_repository, set_ponto_repository


auth_handler = AuthHandler()
router = APIRouter()


@router.get('/{codigo}', summary="Retorna Dados Pessoais", response_model=PontoSchemaPessoa, status_code=status.HTTP_200_OK)
async def get_pessoal(codigo: int, db_conn: AsyncSession = Depends(get_session)):
    """
    Endpoint para resgatar os dados pessoais e de segurança de ponto do servidor
    - **Codigo**: esté é o Codigo do ponto do usuário
    """

    ponto: PontoSchemaPessoa = await get_pessoal_repository(codigo, db_conn)
    if ponto:
        return ponto
    raise HTTPException(detail='Usuário não encontrado.',
                        status_code=status.HTTP_404_NOT_FOUND)


@router.post('/set-ponto', summary="Registra patida de Ponto",response_model=RelogioSchemaUp, status_code=status.HTTP_201_CREATED)
async def set_ponto(pessoa: RelogioSchemaUp, db_conn: AsyncSession = Depends(get_session)):
    """Endpoint para registra a patida de ponto do servidor"""

    nova_patida = await set_ponto_repository(pessoa, db_conn, auth_handler)
    return nova_patida
