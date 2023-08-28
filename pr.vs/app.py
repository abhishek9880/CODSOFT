from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact_details = db.Column(db.String(200), nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    Name = request.form['username']
    Email = request.form['email']
    contact__input= request.form['message']
    
    new_user = User (name=Name,email= Email,  contact_details =  contact__input )
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "Thank you for your submission!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)