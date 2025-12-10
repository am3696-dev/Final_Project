from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Base Schema
class UserBase(BaseModel):
    username: str
    email: EmailStr

# 2. Create Schema
class UserCreate(UserBase):
    password: str

# 3. Update Profile Schema
class UserProfileUpdate(BaseModel):
    bio: Optional[str] = None
    location: Optional[str] = None

# 4. NEW: Password Change Schema
class UserPasswordChange(BaseModel):
    old_password: str
    new_password: str

# 5. Response Schema
class UserResponse(UserBase):
    id: int
    bio: Optional[str] = None
    location: Optional[str] = None

    class Config:
        from_attributes = True