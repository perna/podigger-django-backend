Podigger Django backend

This repository contains the Django backend and Celery workers for Podigger.

How to run locally:

1. Start PostgreSQL and Redis.
2. Create `.env` from `.env.example`.
3. Install dependencies and run migrations:

```bash
uv pip install --system -r requirements-dev.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

The production image is built by GitHub Actions and deployed by
`podigger-infra`. It is not built on the VPS.

```bash
pytest
```

Database credentials are read from environment variables in `config/settings.py`.
Linting is configured with Ruff in `pyproject.toml`.
