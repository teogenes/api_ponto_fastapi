# pylint: disable=C0116 E0401 w0611 C0301
"""_summary_"""
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.security import AuthHandler
from models.ponto_model import PontoModel
from schemas.seguranca_schema import RegistroSchemaUp


async def registro_usuario_repository(registro: RegistroSchemaUp, db_con: AsyncSession, auth_handler: AuthHandler):
    """Função para cadastrar o usuario no sistema de ponto mobile"""
    async with db_con as session:
        query = select(PontoModel).filter(PontoModel.nu_ponto == registro.nu_ponto)
        result = await session.execute(query)
        ponto_up: PontoModel = result.scalars().unique().one_or_none()

        if ponto_up:

            if ponto_up.cel_id is not None:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail='Erro, Celular já cadastrado no sistema!')

            ponto_up.cel_id = auth_handler.gerar_hash_senha(registro.cel_id)
            await session.commit()
            return ponto_up.__dict__

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Erro, Usuario não cadastrado no sistema RH!')


async def login_repository(registro: RegistroSchemaUp, db_con: AsyncSession, auth_handler: AuthHandler):
    """Função para fazer login no sistema RH mobile"""
    async with db_con as session:
        query = select(PontoModel).filter(PontoModel.nu_ponto == registro.nu_ponto)
        result = await session.execute(query)
        ponto: PontoModel = result.scalars().unique().one_or_none()

        if ponto:
            if ponto.cel_id is None:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail='Erro, Não a Celular cadastrado no sistema!')

            valida_login = auth_handler.verificar_senha(registro.cel_id, ponto.cel_id)

            if valida_login:
                token = auth_handler.encode_token(ponto.nu_ponto)
                return token
            
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail='Erro, Dados de acesso incorretos!')
            
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Erro, Usuario não cadastrado no sistema RH!')
