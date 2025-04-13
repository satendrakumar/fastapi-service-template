import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.api.payment_api import payment_api_router
from src.util.logger import get_logger

log = get_logger(__name__)



app = FastAPI(
    root_path="/v1/api",
    title="FastAPI Service Template",
    description="FastAPI Service Template",
)

app.include_router(payment_api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = await request.json()
    log.error(f"Request Validation Error: {exc.errors()} \n Body: {body}")
    return JSONResponse(
        status_code=422,
        content={"error": exc.errors()},
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=False,
        port=8000
    )
