from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete

from app.schemas.answer import AnswerCreate, Answer
from app.models.answer import Answer as AnswerModel

async def create_answer(session: AsyncSession, answer: AnswerCreate, question_id: int) -> Answer:
    answer_data = answer.model_dump()
    answer_data['question_id'] = question_id
    
    new_answer = AnswerModel(**answer_data)
    session.add(new_answer)
    
    try:
        await session.commit()
    except SQLAlchemyError:
        await session.rollback()
        raise
    
    await session.refresh(new_answer)
    
    return Answer(
        id=new_answer.id,
        text=new_answer.text,
        question_id=new_answer.question_id,
        user_id=new_answer.user_id,
        created_at=new_answer.created_at
    )


async def get_answer(session: AsyncSession, answer_id: int):
    result = await session.execute(select(AnswerModel).filter(AnswerModel.id == answer_id))
    answer = result.scalar_one_or_none()
    if answer:
        return Answer(
            id=answer.id,
            text=answer.text,
            question_id=answer.question_id,
            user_id=answer.user_id,
            created_at=answer.created_at
        )
    return None


async def get_answers(session: AsyncSession, skip: int = 0):
    result = await session.execute(select(AnswerModel).offset(skip))
    answers = result.scalars().all()
    return [
        Answer(
            id=answer.id,
            text=answer.text,
            question_id=answer.question_id,
            user_id=answer.user_id,
            created_at=answer.created_at
        ) for answer in answers
    ]


async def get_answers_by_question_id(session: AsyncSession, question_id: int):
    result = await session.execute(select(AnswerModel).filter(AnswerModel.question_id == question_id))
    answers = result.scalars().all()
    return [
        Answer(
            id=answer.id,
            text=answer.text,
            question_id=answer.question_id,
            user_id=answer.user_id,
            created_at=answer.created_at
        ) for answer in answers
    ]

async def delete_answer(session: AsyncSession, answer_id: int):
    result = await session.execute(
        delete(AnswerModel).where(AnswerModel.id == answer_id)
    )
    deleted_count = result.rowcount
    
    if deleted_count > 0:
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise
        
    return deleted_count