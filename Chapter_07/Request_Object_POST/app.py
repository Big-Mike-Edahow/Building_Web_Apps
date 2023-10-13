# app.py
# Request Object POST

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        course=request.form.get('course')
        
        student_info = [('Name', name), ('Age', age), ('Gender', gender), ('Course', course)]

    return render_template('results.html', student_info=student_info)

if __name__ == '__main__':
    app.run(debug=True)

