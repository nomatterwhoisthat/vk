test:
	bash -c "source env/bin/activate && pip install -U pytest psycopg2-binary requests python-dotenv && pytest -v infra/scripts/test_transform.py"
