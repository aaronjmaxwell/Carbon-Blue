# -*- coding: utf-8 -*-
"""Quickstart

Sets up a simple application using the Flask class. In order to run the
app, set a new environment variable, FLASK_APP, to be the name of this
script in the command line console:

`export FLASK_APP=quickstart.py`

Then run using `flask run` or `python -m flask run`.

The main work horse is the class object flask.Flask, which returns a
WSGI application. It has various configuration settings that define the
application characteristics. Each application must be passed the name of
the application module or package, which tells Flask where to look for
all other files and templates.

Flask also has a context block method under:

`flask.Flask.test_request_context()`

that will let it behave like it is handling a request even though it is
in the shell.
"""
__author__ = "ajmax85@gmail.com"
__version__ = "0.6.0"

import flask
from partI import base
from partII import triggers
from partIII import reroute
from partIV import IV
from partV import V
app = flask.Flask(__name__)

app = base(app)
app = triggers(app)
app = reroute(app)
app = IV(app)
app = V(app)

with app.test_request_context():
    print(flask.url_for("index"))
    print(flask.url_for("show_subpath", s = "test/this"))
    print(flask.url_for("hello", next="/"))
    print(flask.url_for("show_user", username="John Doe"))
