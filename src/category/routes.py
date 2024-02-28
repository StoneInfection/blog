from fastapi import APIRouter

from src.category import categories_controller


def get_context_router():
    router = APIRouter()
    router.include_router(categories_controller.router)
    return router

