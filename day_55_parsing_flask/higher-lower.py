from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

print(f"🔢 The correct number is: {random_number}")  # for debugging

# Home page
@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='300'>"
    )

# Route for the guess
@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return (
            f"<h1 style='color: blue;'>{guess} is too low!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='300'>"
        )
    elif guess > random_number:
        return (
            f"<h1 style='color: red;'>{guess} is too high!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='300'>"
        )
    else:
        return (
            f"<h1 style='color: green;'>{guess} is correct! 🎉</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='300'>"
        )

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
