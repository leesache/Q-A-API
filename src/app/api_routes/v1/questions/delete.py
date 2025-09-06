from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.crud.crud_question import delete_question, get_question

router = APIRouter()


@router.delete("/questions/{question_id}")
async def delete_question_by_id(
    question_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a question by ID (and all its answers)"""
    
    # Check if question exists
    question = await get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Delete the question
    deleted_count = await delete_question(db, question_id=question_id)
    
    return {"message": f"Question with id {question_id} deleted successfully"}
