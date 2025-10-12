from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.openbrewerydb.org/v1/breweries"

@app.route("/", methods=["GET", "POST"])
def home():
    breweries = []
    query = None
    error = None

    if request.method == "POST":
        query = request.form.get("query")
        if query:
            params = {"by_city": query.lower()}
            response = requests.get(API_URL, params=params)
            if response.ok:
                breweries = response.json()
                if not breweries:
                    error = f"No breweries found in '{query.title()}' 🍺"
            else:
                error = "API request failed. Try again later."
        else:
            error = "Please enter a city name."

    return render_template("index.html", breweries=breweries, query=query, error=error)

if __name__ == "__main__":
    app.run(debug=True)
