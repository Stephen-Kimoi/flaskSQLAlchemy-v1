from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/flask-app-v1' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Persons(db.Model): 
    ___tablename___ = 'persons' 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(), nullable=False)  

    def __repr__(self): 
        return f'<Person ID:{self.id} name:{self.name}>'

db.create_all() 

@app.route('/')

def index():  
    person = Persons.query.first()
    return 'Hello ' + person.name