from setuptools import setup, find_packages
setup(
    name="portfolio",
    version="0.1",
    packages=find_packages(),

    install_requires=[
        # Django
        "Django",

        # ENVIRONMENT VARIABLES
        "python-decouple",
        "dj-database-url",

        # DATABASE
        "psycopg2-binary",

        # Bootstrap 4
        "django-bootstrap4",

        # Django SASS
        "libsass",
        "django-compressor",
        "django-sass-processor",

        # Font Awesome
        "django-fontawesome-5",

        # Images and favicons
        "Pillow",
        "pilkit",

        # Split settings
        "django-split-settings",

        # Heroku
        "gunicorn",
        "django-heroku",
        "whitenoise", # serve static files in production

        # AWS S3
        "boto3",
        "django-storages",
    ],

)
