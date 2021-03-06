# Kickstart Heroku `django-admin startproject` Guide

> This was original created for Kickstart Coding, the affordable,
> inclusive, and intensive coding course teaching cutting-edge Python /
> Django and JavaScript / React web development in Oakland, CA.
> [Learn more and enroll here.](http://kickstartcoding.com/?utm_source=github&utm_campaign=cheatsheets)

-------------

This is project that's the result of following this guide:

<https://github.com/kickstartcoding/heroku-getting-started/>

Here are tips for launching projects with the Django Admin startproject from
the previous guide, copied below.  An important thing: Notice how manage.py
Procfile, Pipfile, etc are all at the "top level" of the repo. There should be
nothing underneath it.


1. Create your project:

```bash
django-admin startproject djtestproject
cd djtestproject
pipenv --python 3
pipenv shell
pipenv install django
django-admin startapp testapp
# Do Django stuff... e.g.
# ...add view functions to testapp/views.py
# ..add urls routes to testapp/urls.py
# Put static files in testapp/static/
# Put template files in testapp/templates/
```

2. Now, let's configure Heroku by adding a "Procfile" with the following contents:

```bash
web: python manage.py runserver 0.0.0.0:$PORT
```


3. Create a heroku app

```bash
heroku create
```


4. Let's disable a Heroku feature that trips up our Django configuration:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1
```

5. Finally, we need to configure Django to expect different hosts. If you want it to work on any domain (good enough for now), you can change settings.py to have the following, either by adding it on the end of the file, or replacing the similar line near the top:

```bash
ALLOWED_HOSTS=['*']
```

6. If all went well, we can launch it to Heroku by running:

```bash
git push heroku master
```


