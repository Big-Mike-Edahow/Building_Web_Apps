# app.py
# Flask File Uploading

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
app.secret_key = 'It is a great day to be alive'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

        flash('File uploaded successfully.', 'info')

        return redirect(url_for('status'))
    
@app.route('/status')
def status():
    return render_template('status.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

