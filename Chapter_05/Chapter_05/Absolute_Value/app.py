# app.py
# Absolute Value

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    a = -10
    b = 20
    c = 3.55
    d = '1010'
    return render_template('index.html', a=a, b=b, c=c, d=d)

if __name__ == '__main__':
    app.run(debug = True)
