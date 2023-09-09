# app.py
# Student Grades List

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/')
def index():
    grades = [{'Name' : 'Steve', 'Grade' : 90},
              {'Name' : 'Jared', 'Grade' : 75},
              {'Name' : 'Mike', 'Grade' : 45},
              {'Name' : 'Gabe', 'Grade' : 85},
              {'Name' : 'Joe', 'Grade' : 30}]

    return render_template('index.html', grades=grades)

if __name__ == '__main__':
    app.run(debug = True)
