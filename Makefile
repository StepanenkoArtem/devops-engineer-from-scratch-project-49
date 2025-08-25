.PHONY: install brain-games build package-install lint ruff-happy patch minor clean

install:
	uv sync

brain-games:
	uv run brain-games

clean:
	rm -rf dist/

build: clean
	uv build

package-install:
	uv tool install dist/*.whl

package-update:
	uv tool install dist/*.whl --force

lint:
	uvx ruff check

ruff-happy:
	uvx ruff check --fix
	uvx ruff format

patch:
	uv version --bump=patch

minor:
	uv version --bump=minor
