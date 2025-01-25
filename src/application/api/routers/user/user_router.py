from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.application.api.routers.user.user_schemas import UserRegistrationIN, UserRegistrationOUT
from src.application.di import dependency_injector
from src.application.use_cases.user.register.user_register_uc import RegisterUserUC

router = APIRouter(tags=["User"], prefix="/users")


@router.post("/register", status_code=HTTPStatus.CREATED)
async def register(
    data: UserRegistrationIN,
    registration_use_case: RegisterUserUC = Depends(  # noqa: B008
        lambda: dependency_injector.get(RegisterUserUC)
    ),
) -> UserRegistrationOUT:
    """Process a user registration."""
    user = await registration_use_case.register(data.to_dto())
    return UserRegistrationOUT.model_validate(user, from_attributes=True)


__all__ = ["router"]
