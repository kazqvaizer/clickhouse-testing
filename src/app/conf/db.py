# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

from app.conf.environ import env

DATABASES = {
    # read os.environ["DATABASE_URL"] and raises ImproperlyConfigured exception if not found
    "default": env.db(),
    "clickhouse": env.db("CLICKHOUSE_DATABASE_URL", engine="clickhouse_backend.backend"),
}

if env("CI", cast=bool, default=False):
    # Nowait flag for tests!
    DATABASES["clickhouse"]["OPTIONS"] = {
        "settings": {
            "mutations_sync": 1,
        }
    }

# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASE_ROUTERS = ["app.dbrouters.ClickHouseRouter"]
