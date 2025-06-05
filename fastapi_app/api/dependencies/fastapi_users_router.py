from fastapi_users import FastAPIUsers

from core.models.user import User
from core.types.user_id import UserIDType
from .user_manager import get_user_manager
from .backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [authentication_backend],
)
