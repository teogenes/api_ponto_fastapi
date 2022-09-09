# pylint: disable=C0115 C0116 E0401 w0611
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pytz import timezone
from jose import jwt, JWTError
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from core.configs import settings

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=[settings.CRYPTOR], deprecated="auto")
    secret = settings.JWT_SECRET
    algorithm = settings.ALGORITHM


    def gerar_hash_senha(self, senha: str) -> str:
        return self.pwd_context.hash(senha)


    def verificar_senha(self, senha: str, hash_senha: str) -> bool:
        return self.pwd_context.verify(senha, hash_senha)


    def identify_senha(self, hash_senha: str) -> bool:
        return self.pwd_context.identify(hash_senha)


    def _criar_token(self, tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
        payload = {}
        ceara = timezone('America/Fortaleza')
        expira = datetime.now(tz=ceara) + tempo_vida

        payload['type'] = tipo_token
        #payload['exp'] = expira
        payload['iat'] = datetime.now(tz=ceara)
        payload['sub'] = str(sub)
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)


    def encode_token(self, sub: str) -> str:
        return self._criar_token(
            tipo_token = 'access_token',
            tempo_vida= timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            sub = sub
        )


    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm, ])
            return payload['sub']
        except JWTError as ex:
            raise HTTPException(status_code=401, detail='Token inválido!') from ex


    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
