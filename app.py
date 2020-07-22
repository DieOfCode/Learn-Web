import os

from flask import Flask, render_template, request
from views.users import user_blueprint
from views.stores import store_blueprint
from views.alerts import alert_blueprint
from dotenv import load_dotenv
from common.database import Database

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get("ADMIN")
)


@app.route("/")
def home():
    return render_template("home.html")


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(store_blueprint, url_prefix="/store")
if __name__ == "__main__":
    app.run(debug=True)
