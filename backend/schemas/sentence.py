from pydantic import BaseModel


class Sentence(BaseModel):
    korean: str
    english: str