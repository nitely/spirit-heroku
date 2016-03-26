# Environment

This project setups latest Spirit with Python 3.4 and PostgreSQL on heroku.

# Deploy the app

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/nitely/spirit-heroku)

To deploy the app, click the above *deploy* button.

# SMTP Provider

Although Spirit requires a SMTP provider in order to send emails (ie: user activation, password reset, etc),
it's possible to try this out *without* one.

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
