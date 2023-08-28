# app.py
# Student Grade List

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    students = [('Steve', 90), ('Jared', 75), ('Mike', 45), ('Gabe', 85), ('Joe', 30)]
    return render_template('index.html', students = students)

if __name__ == '__main__':
    app.run(debug = True)
