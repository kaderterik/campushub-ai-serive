from fastapi import APIRouter

from app.schemas.classification import (
    ClassificationRequest,
    ClassificationResponse,
    ErrorResponse,
)
from app.services.inference_service import InferenceService


def create_classify_router(service: InferenceService) -> APIRouter:
    router = APIRouter(prefix="/ai", tags=["Classification"])

    @router.post(
    "/classify",
    response_model=ClassificationResponse,
    responses={
        400: {
            "model": ErrorResponse,
            "description": "Invalid request",
        },
        503: {
            "model": ErrorResponse,
            "description": "Model unavailable",
        },
        500: {
            "model": ErrorResponse,
            "description": "Unexpected server error",
        },
    },
    )
    def classify(request: ClassificationRequest) -> ClassificationResponse:
        return service.classify(request.text)

    return router