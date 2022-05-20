from flask import Flask 
from sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/flask-app-v1'
db = SQLAlchemy(app)

@app.route('/')

def index(): 
    return 'Hello Steve' 