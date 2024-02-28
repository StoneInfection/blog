from fastapi import APIRouter

from src.post import post_controller


def get_context_router():
    router = APIRouter()
    router.include_router(post_controller.router)
    return router

