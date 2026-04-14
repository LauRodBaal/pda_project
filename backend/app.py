from flask import Flask
from flask_cors import CORS

from backend.routes.simulate import simulate_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(simulate_bp, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def home():
        return {
            "message": "PDA Backend running successfully."
        }, 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True) 