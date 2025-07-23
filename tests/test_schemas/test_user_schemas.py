from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest, UserPasswordReset
from uuid import UUID

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == UUID(user_response_data["id"])
    # assert user.last_login_at == user_response_data["last_login_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Tests for UserBase
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)
    
    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)

# tests if bio is short or empty
def test_user_update_bio_empty_string():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdate(bio="  ")  # whitespace only
    assert "Field cannot be an empty string." in str(exc_info.value)


# tests if first name is empty
def test_user_update_first_name_empty_string():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdate(first_name="")
    errors = exc_info.value.errors()
    assert any('Field cannot be an empty string.' in e['msg'] for e in errors)

# tests for invalid characters
def test_user_update_nickname_invalid_pattern():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdate(nickname="!@#bad_nick")
    errors = exc_info.value.errors()
    assert any("String should match pattern" in e['msg'] for e in errors)

# tests for invalid profile
def test_user_update_invalid_profile_url():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdate(profile_picture_url="ftp://example.com/image.jpg")
    assert "Invalid URL format" in str(exc_info.value)

# tests if validation is raised if fields are None
def test_user_update_requires_at_least_one_field():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdate()
    assert "At least one field must be provided for update" in str(exc_info.value)

# tests when fields are valid and passes
def test_user_update_valid_fields():
    update = UserUpdate(
        bio="Developer with 5 years of experience",
        first_name="Isabel",
        profile_picture_url="https://example.com/profile.jpg"
    )
    assert update.bio == "Developer with 5 years of experience"
    assert update.first_name == "Isabel"
    assert update.profile_picture_url == "https://example.com/profile.jpg"

@pytest.mark.parametrize("password", [
    "StrongPass1!",
    "Valid$Pass123",
    "Another#Good9"
])
# tests for different cases for a valid password in reset
def test_user_password_reset_valid(password):
    reset = UserPasswordReset(password=password)
    assert reset.password == password

# tests for different cases for a invalid password in reset
@pytest.mark.parametrize("password", [
    "short",
    "nouppercase1!",
    "NOLOWERCASE1!",
    "NoSpecialChar123",
    "NoNumber!"
])
def test_user_password_reset_invalid(password):
    with pytest.raises(ValidationError) as exc_info:
        UserPasswordReset(password=password)
    assert "Password must" in str(exc_info.value)