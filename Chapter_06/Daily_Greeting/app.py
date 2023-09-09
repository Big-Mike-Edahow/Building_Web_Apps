# app.py
# Greeting App

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "Big Mike"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

