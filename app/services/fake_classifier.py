from app.contracts import ClassificationResult


class FakeClassifier:
    def classify(self, text: str) -> ClassificationResult:
        return ClassificationResult(
            category="TECHNOLOGY",
            confidence=0.91,
        )