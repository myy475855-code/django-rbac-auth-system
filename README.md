# Django Authentication & Role-Based Access Control

Portfolio starter project using Django + Django REST Framework.

## Features
- Registration, login, logout, Django password hashing and password validators.
- Student, Company, and Admin groups.
- Protected dashboards and role-protected API endpoints.
- CSRF middleware and session authentication.
- Django Admin for user/group management.
- Automated RBAC tests.

## Run locally (Windows)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py setup_roles
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/. Registering creates a Student account. Assign Company or Admin groups in `/admin/` using your superuser account.

## API
- `GET /api/me/` — authenticated user details
- `GET /api/student/` — Student or Admin
- `GET /api/company/` — Company or Admin
- `GET /api/admin/` — Admin only

## Tests
Run `python manage.py test`.

## Production checklist
Set `DJANGO_DEBUG=0`, set a unique `DJANGO_SECRET_KEY`, configure `DJANGO_ALLOWED_HOSTS`, use HTTPS, secure cookies, production database settings, logging, backups, and dependency updates. This is a learning starter and should be security-reviewed before production use.
