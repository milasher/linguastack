from fastapi import FastAPI
from routes.sentences import router as sentences_router

app = FastAPI()

app.include_router(sentences_router)


@app.get("/")
def root():
    return {"message": "LinguaStack backend is running"}