from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.crud.crud_answer import create_answer
from app.crud.crud_question import get_question
from app.schemas.answer import AnswerCreate, Answer

router = APIRouter()


@router.post("/questions/{question_id}/answers/", response_model=Answer)
async def create_answer_for_question(
    question_id: int,
    answer: AnswerCreate,
    db: AsyncSession = Depends(get_db)
):
    """Add an answer to a specific question"""
    
    question = await get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(
            status_code=404, 
            detail=f"Question with id {question_id} not found"
        )
    
    new_answer = await create_answer(db, answer=answer, question_id=question_id)
    return new_answer
