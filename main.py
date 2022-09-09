# pylint: disable=C0116 E0401
"""_summary_"""
from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv
from api.v1.api import api_router
from core.utils import Tags
from core.configs import settings

load_dotenv()

app = FastAPI(
    title='API Ponto - Registro de entradas e saídas',
    description="Sistema API de batidas de ponto (ISSEC)",
    version="v0.1.0",
    contact={
        "name": "ISSEC/FASSEC",
        "url": "https://www.issec.ce.gov.br/",
        "email": "zeteo@issec.gov.ce.br",
    },
    openapi_url="/api/v1/ponto_api.json",
    openapi_tags=[
        {
            "name": Tags.ponto.value,
            "description": "Bloco relacionado a batida de ponto.",
        },
        {
            "name": Tags.registro.value,
            "description": "Bloco relacionado ao Historico de ponto.",
        },
        {
            "name": Tags.seguranca.value,
            "description": "Bloco relacionado a segurança do acesso a api.",
        },
    ]
)


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    host:str = getenv('HOST' ,"0.0.0.0")
    porta: int = int(getenv('POST' ,"8000"))
    reload: bool = bool(int(getenv('SERVER_RELOAD' ,"1")))
    debug: bool = bool(int(getenv('SERVER_DEBUG' ,"1")))

    uvicorn.run("main:app", host=host, port=porta, log_level='info', reload=reload, debug=debug)
    #para executar no terminal
    #gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

#! Para teste JWT: https://jwt.io/
