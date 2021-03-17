# -*- coding: utf-8 -*-
"""Part III: Re-Routing to prevent Folder Access.

We can explicitly set re-routing if a user tries to access a folder
instead of a file.
"""


def reroute(app):
    """Canonical URLS.

    Canonical URLs defined by the route with a trailing slash are assumed to
    be a folder. If the app does not want to expose the directory,
    explicitly include the back slash at the end.
    """
    @app.route("/projectBlueBook/")
    def show_project():
        """Explicit Routing

        Flask will route to the function regardless of whether the back slash is
        included in the URL.

        For example, http://localhost:5000/projectBlueBook

        returns the same as http://localhost:5000/projectBlueBook/

        :return: HTML :type str
        """
        return "Welcome to Project Blue Book.\n"

    # *** http://localhost:5000/about
    @app.route("/about")
    def show_about():
        """Implicitly assumed file names.

        A route without a backslash is assumed to be a file. Consequently,
        including a backslash will return HTTP/1.1 404.

        :return: HTML or 404 status code. :type str
        """
        return "I love physics, Star Trek, and cheesecake.  Not necessarily in that order.\n"

    return app
