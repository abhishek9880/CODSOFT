from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    description = data['description']
    new_task = Task(description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'description': new_task.description})

@app.route('/edit/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.get_json()
    new_description = data['description']
    task = Task.query.get_or_404(task_id)
    task.description = new_description
    db.session.commit()
    return jsonify({'description': task.description})

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
