from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>this is a pharagrap</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWFkMGxjZ2h0YWhvNmJ0Z2tmOHl4dHM4bWM0dmxzYnljOHBjOHRhOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif" width="200px">')


@app.route("/bye")
def bye():
    return 'Bye'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} you are {number} years old "

if __name__ == "__main__":
    app.run(debug=True)