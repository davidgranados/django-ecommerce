DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"

pytest_plugins = [
    "tests.fixtures",
    "tests.selenium",
]
