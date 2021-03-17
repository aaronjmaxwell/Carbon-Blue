# Flask has a built-in function for generating the URLs that route to specific functions, 
# `flask.url_for`.  It takes a sole argument, the name of the function, and keyword arguments
# corresponding to the variable routes.  This method is always preferred over hard-coding the URLs
# into the code and page templates.
import flask
def IV(app):
    # *** http://localhost:5000/description
    @app.route("/description")
    def show_routes():
        msg = "<h1>Site Map</h1>\n"
        msg += " <p>\n"
        msg += "  The site index is stored at <strong>{0}</strong>.</br>\n"
        msg += "  The standard message can be retrieved from <strong>{1}</strong>.<br>\n"
        msg += "  The page for John Doe can be found at <strong>{2}</strong>, while Project Blue Book is found at <strong>{3}</strong>.\n"
        msg += " </p>"
        return msg.format(flask.url_for("index"), flask.url_for("hello"), flask.url_for("show_user",
            username = "John Doe"), flask.url_for("show_project"))
    return app
