# app.py
# Flask-Admin Example

from flask import Flask, render_template, redirect, request, url_for
from flask_admin import Admin

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Flask-Admin! 👨‍💼', template_mode='bootstrap4')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

