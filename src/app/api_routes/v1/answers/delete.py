from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.service.answer import AnswerService
from app.core.logger import get_logger


logger = get_logger(__name__)

router = APIRouter()


@router.delete("/answers/{answer_id}")
async def delete_answer_by_id(
    answer_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete an answer by ID"""
    deleted_count = await AnswerService(db).service_delete_answer(answer_id)
    return {"message": f"Answer with id {answer_id} deleted successfully"}
