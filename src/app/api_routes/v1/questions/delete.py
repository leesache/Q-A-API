from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.service.question import QuestionService

router = APIRouter()


@router.delete("/questions/{question_id}")
async def delete_question_by_id(
    question_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a question by ID (and all its answers)"""
    await QuestionService(db).service_delete_question(question_id)
    return {"message": f"Question with id {question_id} deleted successfully"}
