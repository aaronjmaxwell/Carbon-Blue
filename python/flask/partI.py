# -*- coding: utf-8 -*-
"""Part I: Decorating URL Routes.

Once we have assigned our WSGI application, we use a decorator to define
the URL route that will trigger the decorated function. Once we have
received the base app object, we decorate the URLs and pass it back.
"""


def base(app):
    """Basic Decorators.

    The name is used to generate URLs for the particular function.
    """
    @app.route("/")
    def index():
        """Define the Index.

        It returns a simple message at http://localhost:5000
        """
        return "Index Page\n"

    @app.route("/hello")
    def hello():
        """Sub-Routing.

        We define a second route that can be used to get the familiar
        greeting at http://localhost:5000/hello
        """
        return "Hello, World!\n"

    return app
