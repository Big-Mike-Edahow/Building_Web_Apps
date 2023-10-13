# /engineering/routes.py

from flask import Blueprint, render_template

engineering = Blueprint('engineering', __name__)

engineering_index_docstring = '''
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
                        <img src="https://Big-Mike-Edahow.github.io/images/Mad_Scientist.png" alt="Mad Scientist" style="width: 425px; height: 390px;">
                    </div>
                    <div>
                        <div style="text-align:center; margin-left: auto; margin-right: auto;">
                            <h2>College of Engineering Home Page 🧑‍🔬</h2>
                        </div>
                        <div style="text-align: center; background-color: rgb(231, 217, 217); padding: 10px; margin-left: auto; margin-right: auto; border: 5px solid black;">
                            <h2>
                                <a style="margin: 10px; padding: 10px; background-color: rgb(71, 187, 233); color: black; text-decoration: none; border: 5px solid black;" href="/"><strong>Home 🔙<strong></a>
                                <a style="margin: 10px; padding: 10px;" href="/engineering/courses">Courses</a>
                                <a style="margin: 10px; padding: 10px;" href="/engineering/faculty">Faculty</a>
                            </h2>
                        </div>
                    </div>
                </section>
            </main>
        </body>
    </html>
    '''

@engineering.route('/')
def index():
    return engineering_index_docstring

engineering_courses_docstring = '''
    <html>
        <head>
            <title>Courses</title>
        <head>
        <body style="background-color: aqua">
            <main style="margin-top: 50px;">
                <div style="text-align:center; margin-left: auto; margin-right: auto;">
                    <h1>College of Engineering 🏫</h1>
                    <hr style="text-align: center; width: 700px; border: 5px solid black;">
                    <h2 style="text-align: center">List of courses 🧑‍🎓</h2>
                    <h3 style="text-align: center">Python Fundamentals 🐍</h3>
                    <h3 style="text-align: center">Java Programming ☕</h3>
                    <h3 style="text-align: center">C/C++ Programming 🧩</h3>
                    <h3 style="text-align: center">Principles of Data Science 💾</h3>
                    <br>
                    <h2><a style="margin: 10px; padding: 10px; background-color: rgb(231, 217, 217); color: black; text-decoration: none; border: 5px solid black;" href="/engineering"><strong>Home 🔙<strong></a></h2>
                </div>
            </main>
        </body>
    <html>
'''

@engineering.route('/courses')
def courses():
    return engineering_courses_docstring

engineering_faculty_docstring = '''
    <html>
        <head>
            <title>Faculty</title>
        <head>
        <body style="background-color: aqua">
            <main style="margin-top: 50px;">
                <div style="text-align:center; margin-left: auto; margin-right: auto;">
                    <h1>College of Engineering 🏫</h1>
                    <hr style="text-align: center; width: 700px; border: 5px solid black;">
                    <h2 >List of Faculty Members 👨‍💼</h2>
                    <h3 style="text-align: center">Steve 👨‍💻</h3>
                    <h3 style="text-align: center">Jared 👨‍🔧</h3>
                    <h3 style="text-align: center">Mike 🧔‍♂️</h3>
                    <h3 style="text-align: center">Gabe 🧑‍🔬</h3>
                    <br>
                    <h2><a style="margin: 10px; padding: 10px; background-color: rgb(231, 217, 217); color: black; text-decoration: none; border: 5px solid black;" href="/engineering"><strong>Home 🔙<strong></a></h2>
                </div>
            </main>
        </body>
    <html>
'''

@engineering.route('/faculty')
def faculty():
    return engineering_faculty_docstring

