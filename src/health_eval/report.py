"""Report generation."""
import json
from typing import Dict, Any, List
from pathlib import Path
from pydantic import BaseModel


class EvaluationReport(BaseModel):
    """Evaluation report structure."""
    dataset: str
    model: str
    scores: List[Dict[str, Any]]
    summary: Dict[str, Any] = {}


def generate_report(results: Dict[str, Any]) -> EvaluationReport:
    """Generate evaluation report from results."""
    report = EvaluationReport(
        dataset=results.get("dataset", "unknown"),
        model=results.get("model", "unknown"),
        scores=results.get("scores", []),
        summary={"status": results.get("status", "unknown")}
    )
    return report


def save_report(report: EvaluationReport, output_path: str):
    """Save report to file."""
    path = Path(output_path)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(report.model_dump(), f, indent=2)


def print_report(report: EvaluationReport):
    """Print report to console."""
    print(f"\n{'='*50}")
    print(f"Evaluation Report")
    print(f"{'='*50}")
    print(f"Dataset: {report.dataset}")
    print(f"Model: {report.model}")
    print(f"Scores: {report.scores}")
    print(f"Summary: {report.summary}")
    print(f"{'='*50}\n")
