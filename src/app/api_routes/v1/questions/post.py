from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.crud.crud_question import create_question
from app.schemas.question import QuestionCreate, Question

router = APIRouter()


@router.post("/questions/", response_model=Question)
async def create_new_question(
    question: QuestionCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new question"""
    new_question = await create_question(db, question=question)
    return new_question
