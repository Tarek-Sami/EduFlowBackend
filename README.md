# EduFlow Backend

Django REST API for an education-focused workflow: custom user accounts (admin / teacher), JWT authentication (email-based login), and task management. The Django admin uses [Jazzmin](https://github.com/farridav/django-jazzmin) for the UI.

## Live (Railway)

| | URL |
|---|-----|
| Host | https://eduflowbackend-production.up.railway.app |
| API base | https://eduflowbackend-production.up.railway.app/api/ |
| Admin | https://eduflowbackend-production.up.railway.app/admin/ |

## Stack

- Python 3.10+
- Django 6.x
- Django REST Framework + Simple JWT
- PostgreSQL (`psycopg2-binary`)
- WhiteNoise (static files in production)
- Gunicorn (typical production server)

## Project layout

| Path | Purpose |
|------|---------|
| `core/` | Settings, URLs, WSGI |
| `accounts/` | Custom `User` model, registration, JWT login, profile |
| `tasks/` | `Task` model and CRUD API |

## Environment variables

Create a `.env` file in the project root (same folder as `manage.py`). `core/settings.py` loads it via `python-dotenv`.

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key (**required**). Must also be available during production builds if you run `collectstatic` in CI/Railway. |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | Database user |
| `DB_PASSWORD` | Database password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port (e.g. `5432`) |

Production settings use `DEBUG = False`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` in `core/settings.py`; update those values if your public domain changes.

## Local development

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```

Configure `.env` with a local PostgreSQL instance (or adjust `DATABASES` in settings for SQLite only for quick experiments—not recommended for matching production).

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- API base: `http://127.0.0.1:8000/api/`
- Admin: `http://127.0.0.1:8000/admin/`

## API overview

Authentication: obtain a JWT with **email** and **password**, then send `Authorization: Bearer <access_token>` for protected routes.

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/api/register/` | No | Register a new user |
| POST | `/api/token/` | No | Obtain access & refresh tokens (`email`, `password`) |
| POST | `/api/token/refresh/` | No | Refresh access token |
| GET, PATCH | `/api/me/` | Yes | Current user; PATCH updates profile |
| GET | `/api/users/` | Yes | List users |
| CRUD | `/api/tasks/` | Per DRF defaults | Tasks resource |

Router-registered tasks live under `/api/tasks/` (list, create, retrieve, update, delete as configured by `TaskViewSet`).

## Production notes (e.g. Railway)

- **Static files**: `STATIC_ROOT` is `staticfiles/`. Production uses WhiteNoise with hashed/compressed storage. Run `collectstatic` during the image build so admin/Jazzmin CSS and JS load correctly.
- **Railpack**: `railpack.json` appends `collectstatic` to the build step (Railway’s default builder). Ensure `SECRET_KEY` is defined for the service so the build step can load Django settings.
- **Optional**: `nixpacks.toml` and `build.sh` are provided for other hosts or custom build commands; `build.sh` runs `collectstatic` before `migrate` so static collection is not skipped if the database is unreachable at build time.

## License

See `LICENSE` in the repository root.
