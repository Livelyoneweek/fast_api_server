# FastAPI Demo – Company 도메인 CRUD

> **목표**  
> 기존 Spring Boot(Controller → Service → Repository) 구조를 **FastAPI + Python 3.12**로 재현한 학습용 프로젝트입니다.

---

## 🏗️ 기술 스택
| 영역 | 라이브러리 · 버전 |
|------|-----------------|
| API 서버 | **FastAPI 0.111** |
| ASGI 서버 | **Uvicorn 0.30** (`--reload`) |
| ORM | **SQLAlchemy 2.0** (async) |
| 데이터베이스 | **PostgreSQL 16-alpine** (Docker) |
| 마이그레이션 | **Alembic 1.13** |
| 모델 검증 | **Pydantic 2.11** |
| 패키지 매니저 | **uv** (`uv venv`, `uv pip`) |

---

## 📂 프로젝트 구조
```text
fastapi-demo/
│  .env                 # DB 접속 정보
│  README.md
│  main.py              # FastAPI 인스턴스
│
├─ app/
│   ├─ core/            # 설정, DB 세션
│   │   ├─ config.py
│   │   └─ database.py
│   └─ company/
│       ├─ controller/
│       │   └─ company_controller.py   # Router
│       ├─ service/
│       │   └─ company_service.py      # 비즈니스 로직
│       ├─ repository/
│       │   └─  company_repository.py  # DB 접근
│       ├─ entity/
│       │   └─ entity.py               # SQLAlchemy 모델
│       ├─ dto/
│       └─  └─ dto.py                  # Pydantic DTO
│
└─ alembic/            # DB 마이그레이션
    ├─ env.py
    └─ versions/
