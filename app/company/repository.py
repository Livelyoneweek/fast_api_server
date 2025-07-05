from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.company.entity import Company

class CompanyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, company: Company) -> Company:
        self.session.add(company)
        await self.session.flush()
        return company

    async def find_all(self) -> list[Company]:
        result = await self.session.execute(select(Company))
        return result.scalars().all()
