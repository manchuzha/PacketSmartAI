from flask import Flask, render_template
from flask_cors import CORS

from routes.home import home_bp
from routes.party import party_bp
from routes.jewelry import jewelry_bp

app = Flask(__name__)

CORS(app)

app.secret_key = "pocketsmart-secret-key"

app.register_blueprint(home_bp)
app.register_blueprint(party_bp)
app.register_blueprint(jewelry_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)