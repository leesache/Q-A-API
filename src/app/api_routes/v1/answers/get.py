from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.answer import Answer
from app.service.answer import AnswerService
from app.core.limiter import limiter

router = APIRouter()


@router.get("/answers/{answer_id}", response_model=Answer)
@limiter.limit("5/second")
async def get_answer_by_id(
    request: Request,
    answer_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific answer by ID"""
    return await AnswerService(db).service_get_answer(answer_id)

