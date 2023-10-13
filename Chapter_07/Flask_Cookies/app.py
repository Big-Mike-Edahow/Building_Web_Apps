# app.py
# Flask Cookies

from flask import Flask, render_template, request, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method=='POST':
        user_id = request.form.get('user-id')
        response = make_response(render_template('setcookie.html'))
        response.set_cookie('userID', user_id)

        return response
    
@app.route('/readcookie')
def readcookie():
    name = request.cookies.get('userID')
    return render_template('readcookie.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)

