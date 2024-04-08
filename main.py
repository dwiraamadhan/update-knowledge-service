from fastapi import FastAPI
from api.knowledge import router as knowledge_router

app = FastAPI()

app.include_router(router= knowledge_router)