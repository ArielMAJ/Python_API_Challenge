start:
	poetry run python ./src/server.py

venv-path:
	@echo Copy and run this file
	@echo $(shell python -m poetry env info -p)\Scripts\activate.ps1

install:
	poetry install

test:
	poetry run python -m unittest discover -s ./src/
