from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from db import create_tables
from routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    print("See you soon ;)")


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

@app.get("/")
def go_home():
    return RedirectResponse("api/")
