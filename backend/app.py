from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///data.db")
app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "variance")

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User Model
class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(200))

# Create DB
with app.app_context():
    db.create_all()

# Routes
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    
    user = User.query.filter_by(email=email).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

# Serve React app
@app.route('/')
def serve_react():
    return send_from_directory('static', 'index.html')

# Catch-all for React Router (optional)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
