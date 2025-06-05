from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIDType
from api.dependencies.authentication import get_user_manager
from api.dependencies.authentication import auth_backend

fastapi_users = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [auth_backend],
)
