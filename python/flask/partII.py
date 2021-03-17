# -*- coding: utf-8 -*-
"""Part II: URL triggers.

We will define some variable routes that depend on the URL trigger. Any
variable contained within angle brackets can be passed as a string
variable, with the only restriction being it cannot contain `/`, which
is reserved for path names. We can also set the type of incoming
variables through the following python casts.
"""


def triggers(app):
    """Cast Triggers.

    All variables are cast as `str` implicitly.
    """
    @app.route("/user/<username>")
    def show_user(username):
        """Retrieve user name from URL.

        Under the http://localhost:5000/user/<username>, the variable
        username contains 'username' which can be passed into the app.
        For example, http://localhost:5000/user/sepultura.

        :param username: The page user's name. :type str

        :return HTML :type str
        """
        return "User is {}\n".format(username)

    @app.route("/integers/<int:i>")
    def show_int(i):
        """Cast variables to integers.

        For example, http://localhost:5000/integers/3

        :param i: Integer variable retrieved from URL :type int

        :return: HTML :type str
        """
        return "Posted ID is {}\n".format(i + 3)

    @app.route("/floats/<float:x>")
    def show_float(x):
        """Cast variables to floats.

        For example, http://localhost:5000/floats/2.783

        :param x: Integer variable retrieved from URL :type float

        :return: HTML :type str
        """
        return "Positive float x -> 2 x + 7 = {}\n".format(2 * x + 7)

    @app.route("/subpaths/<path:s>")
    def show_sub_path(s):
        """Special Flask Class for sub paths.

        This special variable allows us to fetch the various sub paths
        that we might want to access. For example,
        http://localhost:5000/subpaths/through/the/looking/glass

        :param s: Sub path to retrieve. :type str

        :return: HTML :type str
        """
        return "This sub-path is {}\n".format(s)

    return app
