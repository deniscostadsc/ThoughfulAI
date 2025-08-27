FROM python:3.13.7 as base

RUN mkdir /code
WORKDIR /code
RUN pip install -U pip

FROM base as lint
RUN pip install ruff
CMD ruff check . && ruff format --check .

FROM base as test
RUN pip install pytest
CMD python -m pytest test_thoughtful.py

FROM base as typecheck
RUN pip install mypy
CMD mypy --disallow-untyped-defs --strict thoughtful.py
