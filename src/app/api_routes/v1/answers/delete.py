from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db
from app.crud.crud_answer import delete_answer, get_answer
from app.core.logger import get_logger


logger = get_logger(__name__)

router = APIRouter()


@router.delete("/answers/{answer_id}")
async def delete_answer_by_id(
    answer_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete an answer by ID"""
    
    answer = await get_answer(db, answer_id=answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    try:
        deleted_count = await delete_answer(db, answer_id=answer_id)
    except SQLAlchemyError as e:
        logger.error(f"Database error deleting answer with id {answer_id}")
        raise HTTPException(status_code=500, detail="Failed to delete answer") from e
    
    logger.info(f"Answer with id {answer_id} deleted successfully")
    return {"message": f"Answer with id {answer_id} deleted successfully"}
