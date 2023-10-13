# app.py
# Flask-Blueprints Example

from __init__ import create_app
from flask import render_template, request, redirect, url_for

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

