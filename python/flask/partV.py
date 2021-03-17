"""HTTP Method decoration.

By default, Flask only accepts GET requests.  Sending a POST to any 
endpoint without explicit settings will return 405.  The route object
allows you to list specific methods in HTTP/1.1 that you would like
enabled.  Then, the object `flask.request` contains the HTTP/1.1
request.  In this example, upon a POST request, the JSON data is sent to
a specific function that then manipulates the data.  A GET request
returns an example data JSON.  Remember only JSON-serializable objects
can be returned.
"""
import flask
def V(app):
    @app.route("/login", methods = ["GET", "POST"])
    def login():
        if (flask.request.method == "POST"):
            obj = flask.request.get_json()
            return munge(obj)
        else:
            return flask.jsonify(data = [1, 2, 3])

    def munge(obj):
        if ("data" in obj):
            obj['data'].append(42.2)
            return flask.jsonify(obj)
        else:
            return flask.jsonify(err = "No data key")
    
    return app
