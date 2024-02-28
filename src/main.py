import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.database.project_config import settings
from src.routes import get_apps_router


def get_application() -> FastAPI:
    application = FastAPI(
        title="БЛОГ",
        debug=settings.DEBUG,
        version="0.1.0"
    )
    application.include_router(get_apps_router())

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)

