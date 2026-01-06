"""Dataset loading and processing."""
import json
from typing import List, Dict, Any
from pathlib import Path
from pydantic import BaseModel


class DatasetItem(BaseModel):
    """Single dataset item."""
    prompt: str
    expected: str
    metadata: Dict[str, Any] = {}


def load_jsonl(file_path: str) -> List[DatasetItem]:
    """Load JSONL dataset file."""
    items = []
    path = Path(file_path)
    if not path.exists():
        return items
    
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data = json.loads(line)
                items.append(DatasetItem(**data))
    return items


def get_dataset(dataset_name: str) -> List[DatasetItem]:
    """Get dataset by name."""
    dataset_path = Path("data") / f"{dataset_name}.jsonl"
    return load_jsonl(str(dataset_path))
