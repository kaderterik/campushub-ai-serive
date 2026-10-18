from fastapi import APIRouter

from app.schemas.classification import (
    ClassificationRequest,
    ClassificationResponse,
)
from app.services.inference_service import InferenceService


def create_classify_router(service: InferenceService) -> APIRouter:
    router = APIRouter(prefix="/ai", tags=["Classification"])

    @router.post("/classify", response_model=ClassificationResponse)
    def classify(request: ClassificationRequest) -> ClassificationResponse:
        return service.classify(request.text)

    return router