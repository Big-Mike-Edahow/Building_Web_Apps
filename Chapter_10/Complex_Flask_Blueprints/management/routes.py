# /management/routes.py

from flask import render_template, url_for
from flask import Blueprint

management = Blueprint('management', __name__, template_folder='templates',static_folder='static')

management_index_docstring = '''
    <html>
        <head>
            <title>Home</title>
        <head>
        <body style="background-color: aqua;">
            <main style="margin-top: 30px; margin-left: 15px; margin-right: 15px;">
                <section>
                    <h1 style="text-align: center; font-size: 2em;">Big Mike University 🏫</h1>
                    <hr style="text-align: center; border: 5px solid black;"><br>
                </section>
                <section style="display: grid; grid-template-columns: 50% 50%">
                    <div>
                        <img src="https://Big-Mike-Edahow.github.io/images/Boss_Lady.png" alt="Boss Lady" style="width: 410px;">
                    </div>
                    <div>
                        <div style="text-align:center; margin-left: auto; margin-right: auto;">
                            <h2>College of Management Home Page 👩‍💼</h2>
                        </div>
                        <div style="text-align: center; background-color: rgb(231, 217, 217); padding: 10px; margin-left: auto; margin-right: auto; border: 5px solid black;">
                            <h2>
                                <a style="margin: 10px; padding: 10px; background-color: rgb(71, 187, 233); color: black; text-decoration: none; border: 5px solid black;" href="/"><strong>Home 🔙<strong></a>
                                <a style="margin: 10px; padding: 10px;" href="/management/courses">Courses</a>
                                <a style="margin: 10px; padding: 10px;" href="/management/faculty">Faculty</a>
                            </h2>
                        </div>
                    </div>
                </section>
            </main>
        </body>
    </html>
    '''

@management.route('/')
@management.route('/index')
def index():
    return management_index_docstring

management_courses_docstring = '''
    <html>
        <head>
            <title>Courses</title>
        <head>
        <body style="background-color: aqua">
            <main style="margin-top: 50px;">
                <div style="text-align:center; margin-left: auto; margin-right: auto;">
                    <h1>College of Management 🏫</h1>
                    <hr style="text-align: center; width: 700px; border: 5px solid black;">
                    <h2 style="text-align: center">List of courses 🧑‍🎓</h2>
                    <h3 style="text-align: center">General/Operations Manager 👷</h3>
                    <h3 style="text-align: center">Production Manager 👨‍🏭</h3>
                    <h3 style="text-align: center">Management Analyst 📈</h3>
                    <h3 style="text-align: center">Human Resources Manager 👥</h3>
                    <br>
                    <h2><a style="margin: 10px; padding: 10px; background-color: rgb(231, 217, 217); color: black; text-decoration: none; border: 5px solid black;" href="/management"><strong>Home 🔙<strong></a></h2>
                </div>
            </main>
        </body>
    <html>
'''

@management.route('/courses')
def courses():
    return management_courses_docstring

management_faculty_docstring = '''
    <html>
        <head>
            <title>Faculty</title>
        <head>
        <body style="background-color: aqua">
            <main style="margin-top: 50px;">
                <div style="text-align:center; margin-left: auto; margin-right: auto;">
                    <h1>College of Management 🏫</h1>
                    <hr style="text-align: center; width: 700px; border: 5px solid black;">
                    <h2 >List of Faculty Members 👨‍💼</h2>
                    <h3 style="text-align: center">Steve 👨‍💻</h3>
                    <h3 style="text-align: center">Jared 👨‍🔧</h3>
                    <h3 style="text-align: center">Mike 🧔‍♂️</h3>
                    <h3 style="text-align: center">Gabe 🧑‍🔬</h3>
                    <br>
                    <h2><a style="margin: 10px; padding: 10px; background-color: rgb(231, 217, 217); color: black; text-decoration: none; border: 5px solid black;" href="/management"><strong>Home 🔙<strong></a></h2>
                </div>
            </main>
        </body>
    <html>
'''

@management.route('/faculty')
def faculty():
    return  management_faculty_docstring 

