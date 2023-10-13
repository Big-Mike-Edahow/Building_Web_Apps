# app.py
# Flask-Blueprints Example

from flask import Flask
from blueprint import bp
 
# Flask app instance
app = Flask(__name__)
 
app.register_blueprint(bp, url_prefix="/")
 
if __name__ == "__main__":
    app.run(debug=True)




