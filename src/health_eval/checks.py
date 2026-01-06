"""Validation and sanity checks."""
from typing import List, Dict, Any
from pydantic import BaseModel


class CheckResult(BaseModel):
    """Result of a validation check."""
    check_name: str
    passed: bool
    message: str = ""


def check_dataset_format(dataset: List[Dict[str, Any]]) -> CheckResult:
    """Verify dataset format is correct."""
    if not dataset:
        return CheckResult(
            check_name="dataset_format",
            passed=False,
            message="Dataset is empty"
        )
    
    required_fields = {"prompt", "expected"}
    for item in dataset:
        if not all(field in item for field in required_fields):
            return CheckResult(
                check_name="dataset_format",
                passed=False,
                message="Missing required fields"
            )
    
    return CheckResult(
        check_name="dataset_format",
        passed=True,
        message="Dataset format is valid"
    )


def run_checks(dataset: List[Dict[str, Any]]) -> List[CheckResult]:
    """Run all validation checks."""
    return [
        check_dataset_format(dataset)
    ]
