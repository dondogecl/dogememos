from flask import Flask, render_template, request, redirect
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
@app.route('/', methods=['POST', 'GET'])
def index():
    # si se recibe una solicitud post (al usar un SUBMIT por ejemplo)
    # se ejecutara el bloque del if, de lo contrario (al ser GET)
    # se ejecutara el Else que retorna la pagina inicial
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        # se guardara esta nueva info en la db
        try:
            if new_task.content == "":
                return 'ingrese un mensaje. <a href="\">Regresar</a> '
            else:
                db.session.add(new_task)
                db.session.commit()
            return redirect('/')
        except:
            return 'Hubo un error al intentar agregar una tarea'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)
    #return "estas en el index"
    

# eliminar
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return('No se pudo eliminar tarea')





# server stuff
if __name__ == "__main__":
    app.run(debug=True)