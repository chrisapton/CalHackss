from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import my_script

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'  # SQLite DB in the same directory
db = SQLAlchemy(app)

# Define a simple User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'name': user.name, 'age': user.age} for user in users])

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        input_text = request.form['text_input']
        output = my_script.some_function(input_text)  # Call a function from your script
        return render_template('result.html', result=output)  # Display the output on a results page
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates DB tables if they don't exist
    app.run(host='0.0.0.0', debug=True)  # Start the Flask app locally

# Querying the index
query_engine = index.as_query_engine()

response = query_engine.query("Make this question very verbose." + "What concepts are in this homework assignment?")
print(response)

