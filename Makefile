install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uvx ruff check

ruff-happy:
	uvx ruff format
