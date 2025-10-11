from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "instance", "todos.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()



@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add_todo():
    task_text = request.form.get("task")
    if task_text:
        new_task = Todo(task=task_text)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
