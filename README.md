# Environment

This project setups latest Spirit with Python 3.6 and PostgreSQL on heroku.

# Deploy the app

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/nitely/spirit-heroku)

To deploy the app, click the above *deploy* button.

# SMTP Provider

Although Spirit requires a SMTP provider in order to send emails (ie: user activation, password reset, etc),
it's possible to try this out *without* one.

You can use [django-sendgrid-v5](https://github.com/sklarsa/django-sendgrid-v5) for the email configuration.
1. Create and activate a virtual environment on your local machine (eg. virtualenv forum-env)

2. pip install [django-sendgrid-v5](https://github.com/sklarsa/django-sendgrid-v5).

3. Clone this repo and associate it to the heroku repo:

```
$ git clone https://github.com/nitely/spirit-heroku.git
$ cd spirit-heroku
$ heroku git:remote -a my-app-name
```
4.  cd spirit-heroku and Update the requiements.txt file of the cloned repo (spirit-heroku) with pip freeze > requirements.txt

5. Copy and paste the requirements in the requirements.txt file of [spirit-heroku repo](https://github.com/nitely/spirit-heroku/blob/master/requirements.txt) into the requirements.txt file on your local machine or cloned repo. After that, change the django version in the requirements.txt file to Django==1.11.13.
                                                      OR
 Add the text below to the requirements.txt file of your cloned repo:
                                                  ```       [
                                                Django==1.11.13
                                                django-sendgrid-v5==0.6.87
                                                python-http-client==3.1.0
                                                pytz==2018.4
                                                sendgrid==5.4.0
                                                django-spirit
                                                dj-database-url==0.3.0
                                                gunicorn==19.3.0
                                                psycopg2==2.7.3.2
                                                SQLAlchemy==1.0.4
                                                whitenoise==3.0
                                                ]```

6. In your cloned repo on your local machine, open a text editor and navigate to spirit-heroku/project/settings/heroku_prod.py and add this:
                                    ```
                                    # Django Email configuration
                                    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
                                    SENDGRID_API_KEY = "YOUR SENDGRID API KEY"
                                    SENDGRID_SANDBOX_MODE_IN_DEBUG = False
                                    DEFAULT_FROM_EMAIL = 'DEFAULT FROM EMAIL' 
                                    ```

to the file and uncomment or delete the other two email configuration settings.

7. Then deploy it:
```
$ git add .
$ git commit -am "my changes"
$ git push heroku master
``` 

Heroku has [many addons](https://elements.heroku.com/search?utf8=%E2%9C%93&q=email)
but you can also use Gmail's SMTP (it has a daily limit, though)
or something like [postmark](https://postmarkapp.com/).

# Limitations

It's not possible to make
[persistent changes to the filesystem](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem)
of a (Dyno) Heroku instance.
This means it's not possible to upload files or build the (Whoosh) search index.

There are ways to overcome this: images can be uploaded to AWS S3
(there are many Django apps out there for this)
and instead of Whoosh use [elastic-search](https://elements.heroku.com/addons/bonsai).

Or don't use Heroku ;)

# Deploying changes

First clone this repo and associate it to the heroku repo:

```
$ git clone https://github.com/nitely/spirit-heroku.git
$ cd spirit-heroku
$ heroku git:remote -a my-app-name
```

Then make the desire changes to the files and deploy it:

```
$ git add .
$ git commit -am "my changes"
$ git push heroku master
```

# Troubleshooting

If you haven't yet, clone this repo and associate it to the heroku repo:

```
$ git clone https://github.com/nitely/spirit-heroku.git
$ cd spirit-heroku
$ heroku git:remote -a my-app-name
```

Then run the following command to show the error log:

```
$ heroku logs
```

# License

MIT
