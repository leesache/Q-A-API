from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.answer import AnswerCreate, Answer
from app.service.answer import AnswerService
from app.core.limiter import limiter

router = APIRouter()


@router.post("/questions/{question_id}/answers/", response_model=Answer)
@limiter.limit("5/second")
async def create_answer_for_question(
    question_id: int,
    answer: AnswerCreate,
    db: AsyncSession = Depends(get_db)
):
    """Add an answer to a specific question"""
    return await AnswerService(db).service_create_answer(question_id, answer)
