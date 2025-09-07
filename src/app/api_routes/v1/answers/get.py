from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.crud.crud_answer import get_answer
from app.schemas.answer import Answer

router = APIRouter()


@router.get("/answers/{answer_id}", response_model=Answer)
async def get_answer_by_id(
    answer_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific answer by ID"""
    
    answer = await get_answer(db, answer_id=answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer
