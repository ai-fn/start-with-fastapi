from fastapi.routing import APIRouter


api_router = APIRouter(prefix="/api")


@api_router.get("/")
def home():
    return {"data": "Hello, world!"}
