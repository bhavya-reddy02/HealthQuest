"""Request and response shapes (Pydantic v2)."""
import re
from pydantic import BaseModel, EmailStr, Field, field_validator


# ---- auth ----
class SignupIn(BaseModel):
    username: str = Field(min_length=2, max_length=40)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character.")
        return v


class LoginIn(BaseModel):
    username: str
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    has_profile: bool


# ---- profile ----
class ProfileIn(BaseModel):
    name: str = ""
    age: int | None = Field(default=None, gt=0)
    sex: str = ""
    height_cm: float | None = Field(default=None, gt=0)
    weight_kg: float | None = Field(default=None, gt=0)
    goal: str = "active"
    activity: str = "mid"
    focus: list[str] = []
    conditions: list[str] = []


# ---- quests ----
class CompleteIn(BaseModel):
    quest_id: str


# ---- assistant ----
class ChatIn(BaseModel):
    message: str
    literacy: str | None = "standard"  # "simple" | "standard" | "detailed"


# ---- learning (Phase 3) ----
class QuizSubmitIn(BaseModel):
    answers: dict[str, int]  # { question_id: selected_option_index }
