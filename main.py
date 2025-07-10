import logging
import sys
import os
from loguru import logger

from fastapi import FastAPI
from app.company.controller.company_controller import router as company_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="FastAPI Layered Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS, # 허용할 오리진 목록
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
    max_age=3600, # Preflight 요청 결과 캐시 시간 (초)
)

app.include_router(company_router)