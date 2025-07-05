from fastapi import FastAPI
from app.company.controller.company_controller import router as company_router

app = FastAPI(title="FastAPI Layered Demo")
app.include_router(company_router)