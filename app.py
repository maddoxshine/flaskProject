from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# Create the database (only needed once, or on changes)
with app.app_context():
    db.create_all()

# Define the route for the index page
@app.route('/', methods=['POST', 'GET'])
def index():
    tasks = Todo.query.all()  # Fetch all tasks from the database
    return render_template('index.html', tasks=tasks)  # Pass tasks to the template

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
