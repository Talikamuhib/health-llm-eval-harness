"""Scoring and metrics calculation."""
from typing import Dict, Any, List
from pydantic import BaseModel


class Score(BaseModel):
    """Evaluation score."""
    metric: str
    value: float
    metadata: Dict[str, Any] = {}


def calculate_accuracy(predictions: List[str], expected: List[str]) -> float:
    """Calculate accuracy score."""
    if not predictions or not expected or len(predictions) != len(expected):
        return 0.0
    
    correct = sum(1 for p, e in zip(predictions, expected) if p == e)
    return correct / len(predictions)


def compute_scores(predictions: List[str], expected: List[str]) -> List[Score]:
    """Compute all evaluation scores."""
    accuracy = calculate_accuracy(predictions, expected)
    return [
        Score(metric="accuracy", value=accuracy)
    ]
