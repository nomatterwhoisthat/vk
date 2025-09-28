test:
	bash -c "source env/bin/activate && pip install -U pytest psycopg2-binary requests python-dotenv && pytest -v infra/scripts/test_transform.py"

lint-ruff:
	pip install --upgrade ruff
	ruff check infra/scripts/

stop-docker:
	docker-compose -f infra/docker-compose.yml up --build -d