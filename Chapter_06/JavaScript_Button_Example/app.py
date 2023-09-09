# app.py
# Images in Flask

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = "Big Mike"

    return render_template('index.html', name=name)

if __name__ =='__main__':
    app.run(debug=True)

