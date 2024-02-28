from fastapi import APIRouter

from .category import routes as category_routes
from .post import routes as post_routes
from .comment import routes as comment_routes


def get_apps_router():
    router = APIRouter()
    router.include_router(category_routes.get_context_router())
    router.include_router(post_routes.get_context_router())
    router.include_router(comment_routes.get_context_router())
    return router
