from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)
# print(article_texts[0])
# print(article_links[0])
# print(article_upvote[0])

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])









# # Read the contents of the HTML file
# with open("website.html") as file:
#     contents = file.read()
    
# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(contents, "html.parser")
# print(soup) # print the entire HTML document
# # Print the title of the HTML document
# print(soup.title)  # <title>My Website</title>
# print(soup.title.string)  # My Website


# with open("./day_45_intermediate_web_dev/website.html") as file:
#     content = file.read()
    
# soup = BeautifulSoup(content, "html.parser")

# # print(soup.title)  # <title>My Website</title

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())  # Get the text inside the tag
#     print(tag.get("href"))  # Get the value of the href attribute

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)