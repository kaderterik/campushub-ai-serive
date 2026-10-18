from app.contracts import Classifier
from app.schemas.classification import ClassificationResponse


class InferenceService:
    def __init__(self, classifier: Classifier) -> None:
        self.classifier = classifier

    def classify(self, text: str) -> ClassificationResponse:
        result = self.classifier.classify(text)

        return ClassificationResponse(
            category=result.category,
            confidence=result.confidence,
        )