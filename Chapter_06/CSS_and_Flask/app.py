# app.py
# CSS and Flask

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    college = "College of Engeneering"
    grades = [{'Name' : 'Steve', 'Grade' : 95}, {'Name' : 'Jared', 'Grade' : 80}, \
                {'Name' : 'Mike', 'Grade' : 42}, {'Name' : 'Gabe', 'Grade' : 90}, \
                {'Name' : 'Joe', 'Grade' : 49}]

    return render_template('index.html', college=college, grades=grades)

if __name__ == '__main__':
    app.run(debug=True)

