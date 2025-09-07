from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.question import QuestionCreate, Question
from app.service.question import QuestionService
from app.core.limiter import limiter

router = APIRouter()


@router.post("/questions/", response_model=Question)
@limiter.limit("5/second")
async def create_new_question(
    question: QuestionCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new question"""
    return await QuestionService(db).service_create_question(question)
