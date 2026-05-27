from fastapi import APIRouter
from schemas.sentence import Sentence

router = APIRouter()

fake_database = []


@router.get("/sentences")
def get_sentences():
    return fake_database


@router.post("/sentences")
def create_sentence(sentence: Sentence):
    fake_database.append(sentence)
    return {
        "message": "Sentence added successfully",
        "data": sentence
    }