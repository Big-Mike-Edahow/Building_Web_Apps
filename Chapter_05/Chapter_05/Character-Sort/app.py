# app.py
# Character Sort

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    list = [5, 8, 4, 6, 7]
    string = "Hello World"
    return render_template('index.html', list=list, string=string)

if __name__ == '__main__':
    app.run(debug = True)
