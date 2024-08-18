from flask import Flask
from app.routes import main
from app.utils import some_utility_function
from app.model import some_model_function


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
