# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from schemas.grade_schema import GradeSchema
from models.grade_model import GradeModel


async def get_grade_pessoal_repository(db_con: AsyncSession, grade_id: int = 1) -> GradeSchema:
    """Função resgata a grade especifica por id"""
    async with db_con as session:
        query = select(GradeModel).filter(GradeModel.id_grade == grade_id)
        result = await session.execute(query)
        grade: GradeSchema = result.scalar_one_or_none()

        return grade