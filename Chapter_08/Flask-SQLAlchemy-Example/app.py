# app.py
# Flask-SQLAlchemy Truck Database

from flask import Flask, render_template, request, redirect, url_for

from database import db
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Time to shut er down'

db_name = 'trucks.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Initializing SQLAlchemy with Flask App
db.init_app(app)

@app.route('/')
def index():
    details = Trucks.query.all()
    return render_template("index.html", details=details)
 
@app.route("/add-truck", methods=['GET', 'POST'])
def add_truck():
    if request.method == 'POST':
        truck_name = request.form.get('truck')
        price = request.form.get('price')
 
        add_detail = Trucks(
            name=truck_name,
            price=price
        )
        db.session.add(add_detail)
        db.session.commit()
        return redirect(url_for('index'))
 
    return render_template('trucks.html')

@app.route('/about')
def about():
    return render_template('about.html')

""" Creating Database with App Context"""
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    from models import Trucks
    create_db()
    app.run(debug=True)

