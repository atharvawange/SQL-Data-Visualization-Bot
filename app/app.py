from flask import Flask

def create_app():
    # Create a Flask instance
    app = Flask(__name__)

    # Load configuration if you have a config file
    # app.config.from_pyfile('config.py')  # Uncomment if needed

    # Register blueprints
    from routes import main
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
