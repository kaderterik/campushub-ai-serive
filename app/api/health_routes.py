from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "service": "ai-service",
        "status": "UP",
        "version": "1.0.0",
    }
