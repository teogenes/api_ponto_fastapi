# pylint: disable=C0115 C0116 E0401 w0611 C0301 R0903
"""_summary_"""
from os import getenv
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    DBBaseModel = declarative_base()

    API_V1_STR: str = getenv('API_V1_STR', '/api/v1')
    DB_URL: str = getenv('DB_URL', 'postgresql+asyncpg://gestaoderh:gestaoderh@172.26.25.45:5432/gestaoderh_v2')

    """
    Gerar JWT_SECRET
    import secrets
    secrets.token_urlsafe(32)
    """
    JWT_SECRET: str = getenv('JWT_SECRET', '102sdsd21d')
    ALGORITHM: str = getenv('ALGORITHM', 'HS256')
    CRYPTOR: str = getenv('CRYPTOR', 'bcrypt') # md5_crypt, sha256_crypt, bcrypt
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES', str(60 * 24 * 7))) # valido por uma semana

    class Config:
        case_sensitive = True


settings = Settings()
