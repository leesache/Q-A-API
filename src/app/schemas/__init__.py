# Import all schemas to ensure they are loaded
from .question import Question, QuestionCreate, QuestionDelete, QuestionUpdate
from .answer import Answer, AnswerCreate, AnswerDelete

# Rebuild models to resolve forward references
Question.model_rebuild()
Answer.model_rebuild()
