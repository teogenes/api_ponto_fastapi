# pylint: disable=C0116 E0401 w0611 C0301
"""_summary_"""
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from core.security import AuthHandler
from repositories.seguranca_repository import registro_usuario_repository, login_repository
from schemas.seguranca_schema import RegistroSchemaUp, RegistroSchemaResponse

auth_handler = AuthHandler()
router = APIRouter()


@router.post('/cadastrar-usuario', response_model=RegistroSchemaResponse)
async def cadastrar_usuario(registro: RegistroSchemaUp, db_con: AsyncSession = Depends(get_session)):
    """Endpoint para cadastrar o usuario no sistema de ponto mobile"""
    return await registro_usuario_repository(registro, db_con, auth_handler)


@router.post('/login', summary="endpoint de teste com segurança")
async def login(auth_details: RegistroSchemaUp, db_con: AsyncSession = Depends(get_session)):
    """Endpoint para fazer login no sistema RH mobile"""
    token = await login_repository(auth_details, db_con, auth_handler)
    return JSONResponse(content={"access_token":token, "token_type": "bearer"}, status_code=status.HTTP_200_OK)


@router.post('/protected', summary="endpoint de teste com segurança", deprecated=True)
def protected(nu_ponto=Depends(auth_handler.auth_wrapper)):
    return {'codigo': nu_ponto}
