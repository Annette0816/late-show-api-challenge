# Late Show API

A beginner-friendly Flask REST API for managing guests, episodes, and appearances on a Late Night TV show.

##  Setup Instructions

1. Clone this repo and enter it:
```bash
git clone https://github.com/your-username/late-show-api-challenge.git
cd late-show-api-challenge
```

2. Set up your environment:
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

3. Create PostgreSQL DB:
```sql
CREATE DATABASE late_show_db;
```

4. Run database migrations and seed data:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
```

5. Start the app:
```bash
flask run
```

## Authentication Flow

- **Register:** `POST /register`
- **Login:** `POST /login` → Returns JWT token
- **Use token:** Add `Authorization: Bearer <token>` header in protected routes

##  API Routes

| Route                 | Method | Protected | Description              |
|----------------------|--------|-----------|--------------------------|
| `/register`          | POST   | ❌        | Register a new user      |
| `/login`             | POST   | ❌        | Get JWT token            |
| `/episodes`          | GET    | ❌        | List all episodes        |
| `/episodes/<id>`     | GET    | ❌        | Get one episode          |
| `/episodes/<id>`     | DELETE | ✅        | Delete episode (cascade) |
| `/guests`            | GET    | ❌        | List all guests          |
| `/appearances`       | POST   | ✅        | Create a new appearance  |

##  Postman Testing

1. Open Postman.
2. Import `challenge-4-lateshow.postman_collection.json`.
3. Run Register, Login, and test all routes.
4. Paste JWT token in Authorization header for protected routes.

