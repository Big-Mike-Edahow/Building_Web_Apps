# app.py
# Flask-SQLite3 Example

from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('my_database.db')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    student_list = curs.execute("SELECT * FROM students;").fetchall()

    conn.commit()
    conn.close()

    return render_template('index.html', student_list=student_list)

@app.route('/new_student')
def new_student():
    return render_template('new_student.html')

@app.route('/show')
def show():
    username=request.args.get('username')

    conn=sqlite3.connect("my_database.db")
    curs = conn.cursor()

    curs.execute("select * FROM students where username=?",(username,))
    student=curs.fetchone();

    return render_template('show.html', student=student)

@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        conn = sqlite3.connect('my_database.db')
        curs = conn.cursor()
        msg = ''

        try:
            name = request.form.get('name')
            gender = request.form.get('gender')
            course = request.form.get('course')
            mobile = request.form.get('mobile')
            username = request.form.get('username')
            password = request.form.get('password')

            sql_query = "INSERT INTO students VALUES (?,?,?,?,?,?)"
            curs.execute(sql_query, (name, gender, course, mobile, username, password))
            conn.commit()
            
            msg = "Record successfully added."
        except Exception as e:
            conn.rollback()
            msg = "Error in insert operation."
        finally:
            conn.close()
            return render_template('result.html', msg=msg)
        
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='POST':
        conn=sqlite3.connect("my_database.db")
        curs=conn.cursor()
        msg=''
        
        name=request.form.get('name')
        gender=request.form.get('gender')
        course=request.form.get('course')
        mobile=request.form.get('mobile')
        username=request.form.get('username')
        sql_query = "UPDATE students SET name=?, gender=?, course=?, mobile=?, username=? where username=?"
        try:
            curs.execute(sql_query,(name,gender,course,mobile,username,username) )
            conn.commit()
            msg= "Record successfully updated."
        except Exception as e:
            conn.rollback()
            print ("sss",str(e))
            
            msg= "Error in UPDATE operation."
        finally:
            return render_template('result.html', msg=msg)

@app.route('/delete')
def delete():
    name=request.args.get('name')
    conn=sqlite3.connect("my_database.db")
    curs = conn.cursor()
    try:
            curs.execute("DELETE from students where name=?",(name,))
            conn.commit()
            msg= "Record successfully deleted."
    except Exception as e:
            conn.rollback()
            error_message = print ("sss",str(e))
            
            msg= "Error in delete operation."
    finally:
            conn.close()
            return render_template('result.html', msg=msg)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

