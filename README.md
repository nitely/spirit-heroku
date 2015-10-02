# Environment

This project setups latest Spirit with Python 3.4 and PostgreSQL on heroku.

# Create the app: Automatic deployment

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/nitely/spirit-heroku)

After you complete the above deployment (click on deploy button), you may want to clone it locally to make further deploy changes.

Make sure you have installed the [Heroku Toolbelt](https://toolbelt.heroku.com/)

```
$ heroku login
$ heroku git:clone -a my-app-name  # Change my-app-name by your app name, found in "Personal Apps"
$ cd my-app-name
$ heroku run python manage.py createsuperuser  # Create your administrator user for Spirit
```

Where do I go from here? the next section you should visit is *[Setting up an email service provider](https://github.com/nitely/spirit-heroku#setting-up-an-email-service-provider)*

# Create the app: Manual deployment

Follow this steps along the *[Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)* guide

```
$ heroku login  # step: Set up
$ git clone https://github.com/nitely/spirit-heroku.git  # step: Prepare the app
$ cd spirit-heroku
$ heroku create  # step: Deploy the app

# Go to http://www.miniwebtool.com/django-secret-key-generator/ and generate a key
$ heroku config:set SECRET_KEY="my_generated_key"  # ie: SECRET_KEY="ybz&m)c4+gm#4nh(shz4t^3gk2w7b!!99rbdha&4jll=8!-7j_"
$ heroku config  # Should display the SECRET_KEY

$ git push heroku master
$ heroku run python manage.py spiritinstall
$ heroku run python manage.py createsuperuser
$ heroku ps:scale web=1
$ heroku open
```

# Setting up an email service provider

Spirit requires an email service provider.
There are many [heroku addons to send emails](https://addons.heroku.com/?q=email).
This example uses [postmark](https://postmarkapp.com/) SMTP (no addon required).

Create a `local_prod.py` file within the `./project/settings` folder:

> Note: when a `local_prod.py` is found, it will loaded instead of `heroku_prod.py`.

```
# local_prod.py

from .heroku_prod import *


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.postmarkapp.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Change this credentials
EMAIL_HOST_USER = 'postmark_api_key'
EMAIL_HOST_PASSWORD = 'postmark_api_key'
DEFAULT_FROM_EMAIL = 'noreply@myforum.com'
```

You will have to deploy the new changes to heroku (see the next section).

# Deploying changes

After creating/modifying a file (ie: `local_prod.py`) you may want to deploy your changes to heroku.

```
$ git add .
$ git commit -am "my changes"
$ git push heroku master
```

# Running locally

This assumes you have followed the *Create the app* section steps.

Make sure you have installed [Heroku Toolbelt](https://toolbelt.heroku.com/) and [PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```
$ virtualenv -p /usr/bin/python3.4 venv  # Ubuntu 14.04
$ source venv/bin/activate
$ pip install -r requirements.txt
$ sudo -u postgres createuser -s $USER  # Ubuntu 14.04
$ createdb spirit
$ heroku local:run python manage.py spiritinstall
$ heroku local:run python manage.py createsuperuser
$ heroku local web
```

Visit [http://0.0.0.0:5000](http://0.0.0.0:5000)
