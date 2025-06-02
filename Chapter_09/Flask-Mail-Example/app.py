# app.py
# Flask-Mail Example

from flask_mail import Mail, Message
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'Big Mike likes Cup O Noodles soup'

app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = ""
app.config['MAIL_PASSWORD'] = ""
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        msg = Message('Hello from the other side!',
                      sender='perigran_falcon@yahoo.com', recipients=['perigran_falcon@yahoo.com'])
    msg.body = "Hey Big Mike, sending you this email from my Flask app, let me know if it works!"
    mail.send(msg)
    flash("Message sent successfully.", 'info')
    return render_template('status.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


