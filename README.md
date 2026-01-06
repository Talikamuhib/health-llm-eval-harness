# health-llm-eval-harness

A lightweight evaluation harness for health-focused Large Language Models (LLMs).

## Structure

```
health-llm-eval-harness/
├── src/health_eval/           # Main package
│   ├── __init__.py
│   ├── run.py                 # Evaluation runner
│   ├── datasets.py            # Dataset loading
│   ├── scoring.py             # Metrics and scoring
│   ├── checks.py              # Validation checks
│   ├── report.py              # Report generation
│   └── providers/             # LLM providers
│       ├── __init__.py
│       ├── stub.py            # Stub provider for testing
│       └── openai_compat.py   # OpenAI-compatible API
├── data/                      # JSONL datasets
│   ├── sample.jsonl
│   └── medical_terms.jsonl
├── .github/workflows/
│   └── ci.yml                 # CI configuration
├── requirements.txt           # Dependencies
├── .gitignore
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run basic evaluation

```bash
cd src
python -m health_eval.run
```

### Load datasets

```python
from health_eval.datasets import load_jsonl, get_dataset

# Load specific dataset
items = get_dataset("sample")
print(f"Loaded {len(items)} items")
```

### Use providers

```python
from health_eval.providers.stub import create_provider

provider = create_provider({"model": "test-model"})
response = provider.generate("What is diabetes?")
print(response)
```

## Features

- Clean, minimal codebase with single-column layout
- Pydantic-based data validation
- Pluggable provider system
- JSONL dataset format
- Automated CI/CD with GitHub Actions

## Dependencies

- pydantic>=2.0.0

## Development

The repository follows clean code principles with minimal dependencies and straightforward implementations.