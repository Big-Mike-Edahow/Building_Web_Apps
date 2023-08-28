# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/langs/')
def langs():
    languages = ['C', 'C++', 'C#', 'Python', 'HTML', 'CSS', 'JavaScript','SQL']
    return render_template('langs.html', languages=languages)

@app.route('/hello/')
def hello():
    stats = ['Mike', '46', 'Blue', 'Pizza', 'Truck Driver', 'Being a nerd']
    return render_template('hello.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)

