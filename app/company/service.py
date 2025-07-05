from app.company.dto import CompanyCreate, CompanyRead
from app.company.entity import Company
from app.company.repository import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository):
        self.repo = repo

    async def create(self, dto: CompanyCreate) -> CompanyRead:
        entity = Company(name=dto.name, address=dto.address)
        saved = await self.repo.save(entity)
        return CompanyRead.model_validate(saved)

    async def get_all(self) -> list[CompanyRead]:
        data = await self.repo.find_all()
        return [CompanyRead.model_validate(c) for c in data]
