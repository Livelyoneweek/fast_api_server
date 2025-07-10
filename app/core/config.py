from functools import lru_cache
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # .env 로드

class Settings(BaseModel):
    db_host: str = str(os.getenv("DB_HOST"))
    db_port: int = int(os.getenv("DB_PORT", 5432))
    db_name: str = str(os.getenv("DB_NAME"))
    db_user: str = str(os.getenv("DB_USER"))
    db_pass: str = str(os.getenv("DB_PASS"))

    # CORS 오리진을 환경 변수에서 읽어오도록 추가
    # 쉼표로 구분된 문자열을 리스트로 변환합니다
    CORS_ORIGINS: list[str] = [] # 기본값은 빈 리스트

    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_pass}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()
