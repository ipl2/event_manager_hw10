from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from app.utils.security import validate_password_complexity
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re

# pydantic v2 is being used so i changed everything to follow that hence field_validator, model_validator

from app.utils.nickname_gen import generate_nickname

class UserRole(str, Enum):
    ANONYMOUS = "ANONYMOUS"
    AUTHENTICATED = "AUTHENTICATED"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"

def validate_url(url: Optional[str]) -> Optional[str]:
    if url is None:
        return url
    url_regex = r'^https?:\/\/[^\s/$.?#].[^\s]*$'
    if not re.match(url_regex, url):
        raise ValueError('Invalid URL format')
    return url

# adding a max length to nickname, lengths to first/lastname
# bio now also has lengths to it
class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")

    nickname: Optional[str] = Field(
        None, min_length=3, max_length=30, 
        pattern=r'^[\w-]+$', example=generate_nickname()
        )
    first_name: Optional[str] = Field(None, min_length=1, max_length=30, example="John")
    last_name: Optional[str] = Field(None, min_length=1, max_length=30, example="Doe")
    bio: Optional[str] = Field(None, min_length=1, max_length=500, example="Experienced software developer specializing in web applications.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] =Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")

    @field_validator('profile_picture_url', 'linkedin_profile_url', 'github_profile_url', mode='before')
    @classmethod
    def validate_urls(cls, v):
        return validate_url(v)

# must provide a string for these fields
    @field_validator('nickname', 'first_name', 'last_name', 'bio', mode='before')
    @classmethod
    def strip_and_validate_empty(cls, v):
        if v is not None:
            v = v.strip()
            if len(v) == 0:
                raise ValueError("Field cannot be an empty string.")
        return v
    
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")
    # adds more complexity checks for passwords
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        return validate_password_complexity(v)

# new class added to include new behavior of validating password when reset
class UserPasswordReset(BaseModel):
    password: str = Field(..., example="NewSecure*Password123")

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        return validate_password_complexity(v)


class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example="john_doe123")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] =Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")

    @model_validator(mode='after')
    @classmethod
    def check_at_least_one_value(cls, values):
        if not any(
            getattr(values, field) is not None
            for field in ['email', 'nickname', 'first_name', 'last_name', 'bio',
                      'profile_picture_url', 'linkedin_profile_url', 'github_profile_url']):
            raise ValueError("At least one field must be provided for update")
        return values

class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=generate_nickname())    
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    is_professional: Optional[bool] = Field(default=False, example=True)

class LoginRequest(BaseModel):
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")

class UserListResponse(BaseModel):
    items: List[UserResponse] = Field(..., example=[{
        "id": uuid.uuid4(), "nickname": generate_nickname(), "email": "john.doe@example.com",
        "first_name": "John", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "last_name": "Doe", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "profile_picture_url": "https://example.com/profiles/john.jpg", 
        "linkedin_profile_url": "https://linkedin.com/in/johndoe", 
        "github_profile_url": "https://github.com/johndoe"
    }])
    total: int = Field(..., example=100)
    page: int = Field(..., example=1)
    size: int = Field(..., example=10)
