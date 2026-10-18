from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.classify_routes import create_classify_router
from app.services.fake_classifier import FakeClassifier
from app.services.inference_service import InferenceService


app = FastAPI(
    title="CampusHub AI Service",
    version="1.0.0",
    description="FakeClassifier ile çalışan deneme API'si.",
)

classifier = FakeClassifier()
service = InferenceService(classifier)

app.include_router(create_classify_router(service))


@app.exception_handler(RequestValidationError)
async def validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={
            "error": "VALIDATION_ERROR",
            "message": "Request body must contain a non-empty string field: text",
        },
    )