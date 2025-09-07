from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.answer import Answer
from app.service.answer import AnswerService

router = APIRouter()


@router.get("/answers/{answer_id}", response_model=Answer)
async def get_answer_by_id(
    answer_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific answer by ID"""
    return await AnswerService(db).service_get_answer(answer_id)

