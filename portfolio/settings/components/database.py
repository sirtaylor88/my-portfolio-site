from dj_database_url import parse as db_url
import dj_database_url

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default = 'sqlite:///' + str(BASE_DIR.joinpath('db.sqlite3')),
        cast    = db_url
    )
}
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
