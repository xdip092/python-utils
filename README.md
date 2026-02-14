# Python Utilities

Reusable Python helper functions for text, lists, and numeric analysis.

## Setup

```bash
cd projects/python-utils
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
```

## Run Tests

```bash
python -m unittest discover -s tests
```

## Example

```python
from py_utils import normalize_text, moving_average

print(normalize_text("  AI   Data   App  "))
print(moving_average([1, 2, 3, 4, 5], window=3))
```
