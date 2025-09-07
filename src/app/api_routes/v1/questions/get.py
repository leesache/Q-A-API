from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.question import Question
from app.service.question import QuestionService
from app.core.limiter import limiter

router = APIRouter()


@router.get("/questions/", response_model=List[str])
@limiter.limit("5/second")
async def get_all_questions(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    """Get all questions (returns only text for performance)"""
    return await QuestionService(db).service_get_questions()


@router.get("/questions/{question_id}", response_model=Question)
@limiter.limit("5/second")
async def get_question_by_id(
    request: Request,
    question_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific question with all its answers"""
    return await QuestionService(db).service_get_question(question_id)
