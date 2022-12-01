# Entry point of the application

from flask import Flask

from web_apis import app as app_blueprint


app = Flask(__name__)
app.register_blueprint(app_blueprint)


# UI PAGE URL
@app.route("/")
def index():
    return "It works!!!"



