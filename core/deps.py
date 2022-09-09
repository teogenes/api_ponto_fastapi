# pylint: disable=C0116 E0401 w0611
"""_summary_"""
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def get_session() -> Generator:
    """_summary_"""
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()