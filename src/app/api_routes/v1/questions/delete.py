from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.service.question import QuestionService
from app.core.limiter import limiter

router = APIRouter()


@router.delete("/questions/{question_id}")
@limiter.limit("5/second")
async def delete_question_by_id(
    request: Request,
    question_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a question by ID (and all its answers)"""
    await QuestionService(db).service_delete_question(question_id)
    return {"message": f"Question with id {question_id} deleted successfully"}
