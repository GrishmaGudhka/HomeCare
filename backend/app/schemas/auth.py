from pydantic import BaseModel, EmailStr, Field, ConfigDict


# Data required when registering a new user
class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: str | None = None
    password: str = Field(min_length=8, max_length=128)


# Data required when logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Information returned about a user
# Never include the hashed password in the response
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


# JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"