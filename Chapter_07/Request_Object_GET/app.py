# app.py
# Request Object

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet')
def greet():
    return render_template('greet.html', name=request.args.get("name", "Big Mike"), \
                           age=request.args.get("age", 46))

if __name__ == '__main__':
    app.run(debug=True)

