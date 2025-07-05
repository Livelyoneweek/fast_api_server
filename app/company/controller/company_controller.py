from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.company.service.company_service import CompanyService
from app.company.repository.company_repository import CompanyRepository
from app.company.dto.company_dto import CompanyCreate, CompanyRead

router = APIRouter(prefix="/companies", tags=["Company"])

def get_service(session: AsyncSession = Depends(get_session)):
    repo = CompanyRepository(session)
    return CompanyService(repo)

@router.post("/", response_model=CompanyRead, status_code=201)
async def create_company(
    dto: CompanyCreate,
    svc: CompanyService = Depends(get_service),
):
    return await svc.create(dto)

@router.get("/", response_model=list[CompanyRead])
async def list_companies(svc: CompanyService = Depends(get_service)):
    return await svc.get_all()
