# Thoughtful AI

Package sorting and classification system.

## Summary

Determines if packages are bulky (≥150cm dimension or ≥1M cm³ volume) or heavy (≥20kg) and classifies them as:
- `REJECTED` - Both bulky AND heavy
- `SPECIAL` - Either bulky OR heavy
- `STANDARD` - Neither bulky nor heavy

## Quick Start

```bash
make lint      # Check code quality
make lint-fix  # Fix formatting and linting issues
make test      # Run tests
make typecheck # Type checking
```

## Makefile Tasks

| Task | Description |
|------|-------------|
| `make lint` | Check code quality and formatting with ruff |
| `make lint-fix` | Auto-fix linting issues and format code |
| `make test` | Run pytest test suite |
| `make typecheck` | Check type annotations with mypy |

## Requirements

- Docker
- Make
