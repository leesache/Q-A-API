from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel
from pydantic import ConfigDict

from app.schemas.answer import Answer

class QuestionContent(BaseModel):
    text: str

class QuestionId(BaseModel):
    id: int

class QuestionCreate(QuestionContent):
    pass

class QuestionDelete(QuestionId):
    pass

class QuestionUpdate(QuestionId, QuestionContent):
    pass

class Question(QuestionContent, QuestionId):
    created_at: datetime
    answers: List[Answer] = []
    
    model_config = ConfigDict(from_attributes=True)