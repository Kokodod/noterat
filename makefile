.PHONY: *

lint:
	uv run mypy noterat && uv run ruff check

test:
	uv run pytest

clean:
	rm -rf noterat/__pycache__
	rm -rf .venv