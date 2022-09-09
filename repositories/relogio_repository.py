# pylint: disable=C0116 E0401 w0611 C0301
"""_summary_"""
from datetime import timedelta, time
import datetime
from typing import List
from queue import Queue
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy.future import select
from schemas.relogio_schema import TimeSchema, RelogioSchema
from schemas.grade_schema import GradeSchema
from models.relogio_model import RelogioModel


async def get_horas_exatas_repository(db_con: AsyncSession) -> TimeSchema:
    """Função para resgatar a hora exata do server(DB)"""
    async with db_con as session:
        sql = text("SELECT to_char(LOCALTIMESTAMP,'DD/MM/YYYY') \"data\", \
            to_char(LOCALTIMESTAMP,'HH24:MI:SS') HORA")

        result = await session.execute(sql)
        await session.commit()
        resposta = next(result)
        return TimeSchema(data=resposta[0], hora=resposta[1])


async def get_registros_dia_repository(codigo: int, db_con: AsyncSession) -> List[RelogioSchema]:
    """Função resgata o histórico do dia atual das batidas(registros) de ponto"""
    async with db_con as session:
        query = select(RelogioModel)\
            .filter(RelogioModel.cd_num == codigo)\
            .filter(RelogioModel.dt_data == datetime.date.today())\
            .order_by(RelogioModel.dt_hora.asc())

        result = await session.execute(query)
        relogios: List[RelogioSchema] = result.scalars().all()

        return relogios


def converte_timeto_datetime(tempo: time, tolerancia:int = 0, segundo:str = '%S') -> datetime.datetime:
    """_summary_"""
    tempo = [int(x) for x in tempo.strftime(f'%H:%M:{segundo}').split(':')]
    return datetime.datetime(2000, 1, 1, *tempo) + timedelta(minutes=tolerancia)


def list_convertida_datetime(grade: GradeSchema) -> List[datetime.datetime]:
    return [
        converte_timeto_datetime(grade.in1, segundo=59) if grade.in1 else None,
        converte_timeto_datetime(grade.out1) if grade.out1 else None,
        converte_timeto_datetime(grade.in2, segundo=59) if grade.in2 else None,
        converte_timeto_datetime(grade.out2) if grade.out2 else None
    ]


def calcula_grade_validacao_repository(registros: List[RelogioSchema], grade: GradeSchema) -> List[RelogioSchema]:
    """_summary_"""

    grade_list = list_convertida_datetime(grade)

    for regs in registros:
        hora = converte_timeto_datetime(regs.dt_hora)
        valid = [False,False,False,False]

        entradas_tolerancia = Queue(2)
        entradas_tolerancia.put(10)
        entradas_tolerancia.put(0)

        if grade_list[0]:
            tolerancia = entradas_tolerancia.get()
            valid[0] = (grade_list[0] + timedelta(minutes=-15)) <= hora <= (grade_list[0] + timedelta(minutes=tolerancia) )

        if grade_list[1]:
            valid[1] = grade_list[1] <= hora <= (grade_list[1] + timedelta(minutes=15, seconds=59))

        if grade_list[2]:
            tolerancia = entradas_tolerancia.get()
            valid[2] = (grade_list[2] + timedelta(minutes=-15)) <= hora <= (grade_list[2] + timedelta(minutes=tolerancia))

        if grade_list[3]:
            valid[3] = grade_list[3] <= hora <= (grade_list[3] + timedelta(minutes=15, seconds=59))

        if valid[0] or valid[1] or valid[2] or valid[3]:
            regs.valid = True

    return registros
