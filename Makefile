.PHONY: install brain-games build package-install lint ruff-happy patch minor

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

patch:
	uv version --bump=patch

minor:
	uv version --bump=minor
