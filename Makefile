
venv:
	mkdir -p .env
	python -m venv .env

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

shell:
	ipython

test:
	pytest tests/