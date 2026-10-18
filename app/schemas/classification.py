from typing import Literal

from pydantic import BaseModel, Field, StrictStr, field_validator


class ClassificationRequest(BaseModel):
    text: StrictStr

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("text must be a non-empty string")

        return value


class ClassificationResponse(BaseModel):
    category: Literal[
        "TECHNOLOGY",
        "SPORT",
        "ART",
        "CAREER",
        "SOCIAL",
        "OTHER",
    ]
    confidence: float = Field(ge=0, le=1)