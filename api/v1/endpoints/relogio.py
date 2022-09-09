# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.relogio_schema import RelogioSchema, TimeSchema
from schemas.grade_schema import GradeSchema
from core.deps import get_session
from repositories.relogio_repository import get_horas_exatas_repository
from repositories.relogio_repository import get_registros_dia_repository
from repositories.grade_repository import get_grade_pessoal_repository
from repositories.relogio_repository import calcula_grade_validacao_repository

router = APIRouter()


@router.get('/horas-exatas', summary="Hora Atual",response_model=TimeSchema,status_code=status.HTTP_200_OK)
async def get_horas_exatas(db_con: AsyncSession = Depends(get_session)):
    """Endpoint para resgatar a hora exata do server(DB)"""
    tempo_exato: TimeSchema = await get_horas_exatas_repository(db_con)
    return tempo_exato


@router.get('/registros-dia/{codigo}/{grade_id}', summary="Histórico de registro de ponto do dia",response_model=List[RelogioSchema], status_code=status.HTTP_200_OK)
async def get_registros_dia(codigo: int, grade_id: int = 1,
                            db_con: AsyncSession = Depends(get_session)):
    """
    Endpoint resgata o histórico do dia atual das batidas(registros) de ponto
    - **codigo**: esté é o Codigo do ponto do usuário
    - **grade_id**: esté é o Codigo da grade do usuário
    """
    relogios: List[RelogioSchema] = await get_registros_dia_repository(codigo, db_con)
    grade: GradeSchema = await get_grade_pessoal_repository(db_con, grade_id)
    if relogios:
        relogios_com_grade = calcula_grade_validacao_repository(relogios, grade)
        return relogios_com_grade
    raise HTTPException(detail='Usuário não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
