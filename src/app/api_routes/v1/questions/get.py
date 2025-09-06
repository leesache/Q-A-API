from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.crud.crud_question import get_questions, get_question
from app.schemas.question import Question

router = APIRouter()


@router.get("/questions/", response_model=List[str])
async def get_all_questions(
    db: AsyncSession = Depends(get_db)
):
    """Get all questions (returns only text for performance)"""
    questions = await get_questions(db)
    return questions


@router.get("/questions/{question_id}", response_model=Question)
async def get_question_by_id(
    question_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific question with all its answers"""
    question = await get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
