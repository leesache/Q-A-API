from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_question import get_question, get_questions, create_question, delete_question
from app.schemas.question import Question, QuestionCreate

from app.core.exceptions import NotFoundException, BadRequestException, InternalServerErrorException
from app.core.logger import get_logger


logger = get_logger(__name__)

class QuestionService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def service_get_question(self, question_id: int) -> Question:
        try:
            question = await get_question(self.session, question_id)
            if not question:
                logger.info(f"Question with id {question_id} not found")
                raise NotFoundException(f"Question with id {question_id} not found")
            return question
        except NotFoundException as e:
            logger.info(f"Question with id {question_id} not found")
            raise NotFoundException(f"Question with id {question_id} not found") from e
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e

    async def service_get_questions(self) -> list[str]:
        try:
            return await get_questions(self.session)
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e

    async def service_create_question(self, question: QuestionCreate) -> Question:
        try:
            return await create_question(self.session, question)
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e

    async def service_delete_question(self, question_id: int) -> int:
        try:
            deleted = await delete_question(self.session, question_id)
            if deleted <= 0:
                logger.info(f"Question with id {question_id} not found")
                raise NotFoundException(f"Question with id {question_id} not found")
            return deleted
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e