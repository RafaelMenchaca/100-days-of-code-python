from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_titles = soup.find_all(name="span", class_="titleline")
print(article_titles)
                               












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