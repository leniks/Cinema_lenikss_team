from fastapi import FastAPI, Request
from app.routers.movies_router import router as movies_router
from app.routers.users_router import router as router_users
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )



@app.get("/")
def home_page():
    return {"message": "Your Cinema"}


app.include_router(movies_router)
app.include_router(router_users)