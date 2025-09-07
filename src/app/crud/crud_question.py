from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete

from app.schemas.question import QuestionCreate, Question
from app.models.question import Question as QuestionModel
from app.crud.crud_answer import get_answers_by_question_id

#GET /questions/ — список всех вопросов
# Не совсем понял нужно ли возвращать полную сущность или только text
# Сделал так чтобы возвращалась только text, потому что в проде SELECT * не стоит использовать
async def get_questions(session: AsyncSession):
    result = await session.execute(select(QuestionModel.text))
    return result.scalars().all()

#POST /questions/ — создать новый вопрос
async def create_question(session: AsyncSession, question: QuestionCreate) -> Question:
    new_question = QuestionModel(**question.model_dump())
    session.add(new_question)
    
    try:
        await session.commit()
    except SQLAlchemyError:
        await session.rollback()
        raise
    
    await session.refresh(new_question)
    
    return Question(
        id=new_question.id,
        text=new_question.text,
        created_at=new_question.created_at,
        answers=[]
    )

#GET /questions/{id} — получить вопрос и все ответы на него
async def get_question(session: AsyncSession, question_id: int):
    result = await session.execute(select(QuestionModel).filter(QuestionModel.id == question_id))
    question = result.scalar_one_or_none()
    if question:
        answers = await get_answers_by_question_id(session, question_id)
        question_dict = {
            "id": question.id,
            "text": question.text,
            "created_at": question.created_at,
            "answers": answers
        }
        return Question.model_validate(question_dict)
    return None

# DELETE /questions/{id} — удалить вопрос (вместе с ответами)
async def delete_question(session: AsyncSession, question_id: int):
    result = await session.execute(
        delete(QuestionModel).where(QuestionModel.id == question_id)
    )
    deleted_count = result.rowcount
    
    if deleted_count > 0:
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise
        
    return deleted_count