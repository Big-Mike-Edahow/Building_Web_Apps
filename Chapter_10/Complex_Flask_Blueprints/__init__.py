# __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        from engineering.routes import engineering
        from management.routes import management

        app.register_blueprint(engineering, url_prefix='/engineering/')
        app.register_blueprint(management, url_prefix='/management/')

        return app


