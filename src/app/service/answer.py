from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_answer import get_answer, create_answer, delete_answer
from app.crud.crud_question import get_question
from app.schemas.answer import Answer, AnswerCreate

from app.core.exceptions import NotFoundException, BadRequestException, InternalServerErrorException
from app.core.logger import get_logger


logger = get_logger(__name__)

class AnswerService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def service_get_answer(self, answer_id: int) -> Answer:
        try:
            answer = await get_answer(self.session, answer_id)
            if not answer:
                raise NotFoundException(f"Answer with id {answer_id} not found")
            return answer
        except NotFoundException as e:
            logger.info(f"Answer with id {answer_id} not found")
            raise NotFoundException(f"Answer with id {answer_id} not found") from e
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e

    async def service_create_answer(self, question_id: int, answer: AnswerCreate) -> Answer:
        try:
            question = await get_question(self.session, question_id)
            if not question:
                logger.info(f"Question with id {question_id} not found")
                raise NotFoundException(f"Question with id {question_id} not found")
            return await create_answer(self.session, answer, question_id)
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e

    async def service_delete_answer(self, answer_id: int) -> int:
        try:
            deleted = await delete_answer(self.session, answer_id)
            if deleted <= 0:
                logger.info(f"Answer with id {answer_id} not found")
                raise NotFoundException(f"Answer with id {answer_id} not found")
            return deleted
        except BadRequestException as e:
            logger.warning(f"Bad request: {e}")
            raise BadRequestException(f"Bad request: {e}") from e
        except InternalServerErrorException as e:
            logger.error(f"Internal server error: {e}")
            raise InternalServerErrorException(f"Internal server error: {e}") from e