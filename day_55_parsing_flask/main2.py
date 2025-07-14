from flask import Flask  # Import the Flask class from the flask module
app = Flask(__name__)    # Create a new Flask web application instance

# Define a route for the root URL "/"
@app.route("/")
def hello_world():
    # Return an HTML string with a heading, paragraph, and image
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>this is a pharagrap</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWFkMGxjZ2h0YWhvNmJ0Z2tmOHl4dHM4bWM0dmxzYnljOHBjOHRhOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif" width="200px">')

# Define a route for the URL "/bye"
@app.route("/bye")
def bye():
    return 'Bye'  # Return the string 'Bye'

# Define a route with dynamic parameters: name (string) and number (integer)
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    # Return a personalized greeting using the provided name and number
    return f"Hello there {name} you are {number} years old "

# Run the app only if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask development server with debug mode enabled