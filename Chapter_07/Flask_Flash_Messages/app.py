# app.py
# Flask Flash Messages

from flask import Flask, redirect, render_template, request, url_for
from flask import flash

app = Flask(__name__)
app.secret_key = 'I am all coded out for the day'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('user-pwd') == '' or request.form.get('username') == '':
            flash('Username and password is required', 'error')
            return redirect(url_for('index'))
        if len(request.form.get('user-pwd')) in range(1,9):
            flash('Weak password!', 'warning')
            return redirect(url_for('status'))
        if request.form.get('username') not in ['admin', 'manager', 'supervisor']:
            flash('You were successfully logged in.', 'info')
            return redirect(url_for('status'))
        else:
            flash('User name unavailable', 'error')
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

