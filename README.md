# Hive

![image](image/logo.png)
Hive is a website where people can buy and sell services like housekeeping, tutoring, errand running, massage & accupuncture services and more!

## Virtual Environment

### How to activate virtual environemtn

```bash
source venv/bin/activate
```

### How to deactivate

```bash
deactivate
```

## Basic Django Commands used

```
django-admin help
django-admin startproject <<name-of-project>> .

python manage.py startapp <<name-of-app>>

python manage.py runserver
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py collectstatic
```

## Environment Variables to be set

SECRET_KEY  
DJANGOAPPMODE (Debug for local dev and Prod for deployment)  
USEDEBUGDB (True in local False in prod)

### Email

EMAIL_HOST_USER  
EMAIL_HOST_PASSWORD

### Postgres

DBNAME  
DBUSER  
DBPASSWORD  
DBHOST  
DBPORT

### Bucketeer (in heroku)

BUCKETEER_AWS_ACCESS_KEY_ID  
BUCKETEER_AWS_SECRET_ACCESS_KEY  
BUCKETEER_AWS_REGION  
BUCKETEER_BUCKET_NAME

## Django Messages

Implementing it in base.html

```
django.contrib.messages (already installed)
```

## Django Environment Variable

1. Import environ package  
   `import environ`
2. Initialize environ  
   `env = environ.Env()` and `env.read_env()`

create `.env` file to manage environment variable which is left out in git repository.

This .env is used for local development

## Send email

Use service called "mailgun"

1. Go to Heroku to set mailgun as resource
2. Go to mailgun and get credentials
3. set settings:

```
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USER_TLS=
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
```

## What should be done

- when new profile image is selected, the image shown should change as well
- see how the bio in the profile can have larger text area

## How to serve static file in production

We use `whitenoise` to serve static file.

Once you install it you should add following to Middleware:

```bash
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
```

Then in the settings:

```bash
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

## Deployment to Heroku (Heroku CLI)

```bash
heroku login
```

```bash
heroku git:remote -a <name-of-app-in-heroku>
```

### Files required

Create following files:

- Procfile
  - web: gunicorn hive.wsgi
- requirements.txt
- runtime.txt
  - should indicate python runtime (python-3.9.14 for example or whatever python runtime used for the virtual machine)

### Deployment

```bash
git add .
git commit -m "..."
git push heroku main
```
