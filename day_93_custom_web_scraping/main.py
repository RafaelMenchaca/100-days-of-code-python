import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "https://www.audible.com/search?keywords=python+programming"

# Send HTTP GET request
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "lxml")

# Parse the data
book_titles = []
authors = []
ratings = []
lengths = []

# Each book card
for book in soup.select(".bc-list-item.productListItem"):
    # Title
    title = book.select_one(".bc-heading a")
    title_text = title.get_text(strip=True) if title else "N/A"
    book_titles.append(title_text)

    # Author
    author = book.select_one(".authorLabel span")
    author_text = author.get_text(strip=True) if author else "N/A"
    authors.append(author_text)

    # Rating
    rating = book.select_one(".ratingsLabel span")
    rating_text = rating.get_text(strip=True) if rating else "N/A"
    ratings.append(rating_text)

    # Length
    length = book.select_one(".runtimeLabel span")
    length_text = length.get_text(strip=True) if length else "N/A"
    lengths.append(length_text)

# Combine into DataFrame
df = pd.DataFrame({
    "Title": book_titles,
    "Author": authors,
    "Rating": ratings,
    "Length": lengths
})

# Save to CSV
df.to_csv("audible_books.csv", index=False)

print("✅ Done! Data saved to audible_books.csv")
print(df.head())
