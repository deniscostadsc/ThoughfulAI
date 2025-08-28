# Thoughtful AI

[![LINT](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/lint.yaml/badge.svg)](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/lint.yaml)
[![TEST](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/test.yaml/badge.svg)](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/test.yaml)
[![TYPECHECK](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/typecheck.yaml/badge.svg)](https://github.com/deniscostadsc/ThoughfulAI/actions/workflows/typecheck.yaml)

Package sorting and classification system.

## Summary

Determines if packages are bulky (≥150cm dimension or ≥1M cm³ volume) or heavy (≥20kg) and classifies them as:
- `REJECTED` - Both bulky AND heavy
- `SPECIAL` - Either bulky OR heavy
- `STANDARD` - Neither bulky nor heavy

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
