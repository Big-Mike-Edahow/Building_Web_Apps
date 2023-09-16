# app.py
# SQL in easy steps

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./my_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    show_all = conn.execute("SELECT * FROM backpacks;").fetchall()
    conn.commit()
    conn.close()

    return render_template('index.html', show_all=show_all, )


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

