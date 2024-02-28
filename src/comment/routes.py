from fastapi import APIRouter

from src.comment import comment_controller


def get_context_router():
    router = APIRouter()
    router.include_router(comment_controller.router)
    return router

