from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# database settings
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# initializes the db
db = SQLAlchemy(app)

# Creation of models

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    # each time that this function gets called it's going to return:
    def __repr__(self):
        return '<Task %t>' % self.id


# define routes
@app.route('/')
def index():
    #return "estas en el index"
    return render_template("index.html")






# server stuff
if __name__ == "__main__":
    app.run(debug=True)