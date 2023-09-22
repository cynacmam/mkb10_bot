install:
	pip install poetry && \
	poetry install

start:
	poetry run python mkb_bot/main.py