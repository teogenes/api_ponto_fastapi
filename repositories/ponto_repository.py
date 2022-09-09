# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.security import AuthHandler
from models.ponto_model import PontoModel
from models.relogio_model import RelogioModel
from schemas.ponto_schema import PontoSchemaPessoa
from schemas.relogio_schema import RelogioSchemaUp


async def get_pessoal_repository(codigo: int, db_con: AsyncSession):
    """Função para resgatar os dados pessoais e de segurança de ponto do servidor"""
    async with db_con as session:
        query = select(PontoModel).filter(PontoModel.nu_ponto == codigo)
        result = await session.execute(query)
        ponto: PontoSchemaPessoa = result.scalar_one_or_none()

        return ponto


async def set_ponto_repository(pessoa: RelogioSchemaUp, db_con: AsyncSession, auth_handler:AuthHandler):
    """Função para registra a patida de ponto do servidor"""
    nova_patida = RelogioModel(**pessoa.__dict__)
    async with db_con as session:
        try:
            session.add(nova_patida)
            await session.commit()
            return nova_patida
        except Exception as execinte:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, \
                detail='Erro na patida de ponto') from execinte
