from fastapi import APIRouter

from api.api_v1.fastapi_users_router import fastapi_users
from api.dependencies.authentication import auth_backend

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
