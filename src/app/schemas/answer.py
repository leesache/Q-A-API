from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class AnswerContent(BaseModel):
    text: str

class AnswerId(BaseModel):
    id: int

class AnswerUser(BaseModel):
    user_id: str

class AnswerCreate(AnswerContent, AnswerUser):
    pass

class AnswerDelete(AnswerId):
    pass

class Answer(AnswerContent, AnswerId, AnswerUser):
    question_id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

