from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage  #  nuevo import

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SEND_TO = os.getenv("SEND_TO")
AMAZON_URL = "https://www.amazon.com/acer-Gaming-Laptop-GeForce-Backlit/dp/B0DZH5WTQJ/?_encoding=UTF8&pd_rd_w=eSVd8&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=AFS7N31CHASN5P6KKJCS&pd_rd_wg=8geXK&pd_rd_r=a4c95859-79ec-4ce1-876f-525a23826c78&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1"
# AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 800

# Full headers would look something like this
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response = requests.get(url=AMAZON_URL, headers=headers)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find("span", class_="a-offscreen")
price = price.getText()
# print(price + "$$$")

price_without_currency = price.split("$")[1]
# print(price_without_currency)

price_float = float(price_without_currency)
# print(price_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)
safe_title = title.encode("ascii", errors="ignore").decode()
# print(safe_title)

# Mensaje plano (texto)
message = f"{safe_title}\nIs now: {price}\n{AMAZON_URL}"
print(message)

# Mensaje HTML (para emails modernos)
html_message = f"""
<html>
  <body>
    <h2> Amazon Price Alert</h2>
    <p><strong>{safe_title}</strong></p>
    <p><strong> Price:</strong> {price}</p>
    <p><a href="{AMAZON_URL}"> View Product on Amazon</a></p>
  </body>
</html>
"""

# Enviar email si el precio es menor al objetivo
if price_float < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)

        email_msg = EmailMessage()
        email_msg["Subject"] = "Amazon Price Alert"
        email_msg["From"] = EMAIL
        email_msg["To"] = SEND_TO
        email_msg.set_content(message)  # texto plano (por compatibilidad)
        email_msg.add_alternative(html_message, subtype="html")  # HTML moderno

        connection.send_message(email_msg)
