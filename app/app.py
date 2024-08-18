from flask import Flask
from app.routes import main
from app.utils import some_utility_function
from app.model import some_model_function


app = Flask(__name__)

# Register blueprints or routes
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
app = create_app()
