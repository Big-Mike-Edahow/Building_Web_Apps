# app.py
# Flask Sessions

from flask import Flask, redirect, request, render_template, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'Little Pink Houses'

@app.route('/')
def index():
    background = 'images/Idaho_Timber.jpg'

    if 'background' in session:
        background = session['background']

    session['background'] = background
    background_image = url_for('static', filename=background)

    return render_template('index.html', background_image=background_image)

@app.route('/new_background', methods=['GET', 'POST'])
def new_background():
    if request.method=='POST':
        background=request.form.get('background-image')
        session['background']=background

        return redirect(url_for('index'))
    
@app.route('/about')
def about():
    background = 'images/kingfisher_oklahoma.jpg'

    if 'background' in session:
        background = session['background']

    session['background'] = background
    background_image = url_for('static', filename=background)

    return render_template('about.html', background_image=background_image)
    
if __name__ == '__main__':
    app.run(debug=True)

