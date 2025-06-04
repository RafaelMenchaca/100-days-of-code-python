import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# Here we are using the Alpha Vantage API to get the daily stock prices for TSLA (Tesla Inc).
# the ulr is the endpoint for the stock data, and we are passing the stock symbol and API key as parameters.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apiKey": STOCK_API_KEY,
}

# We are making a GET request to the Alpha Vantage API to get the stock data.
response = requests.get(STOCK_ENDPOINT, params=stock_params)

# We are saving Time Series Daily data from the response JSON.
# The data is a dictionary where the keys are dates and the values are dictionaries with stock prices.
# data = response.json()["Time Series (Daily)"]

# # We are creating a list of the stock prices for each day.
# data_list = [value for (key, value) in data.items()]

# # We are getting the stock price for yesterday, which is the first item in the data_list.
# yesterday_data = data_list[0]

# # We are getting the closing price for yesterday.
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


# #TODO 2. - Get the day before yesterday's closing stock price

# # We are getting the stock price for the day before yesterday, which is the second item in the data_list.
# day_before_yesterday_data = data_list[1]

# # We are getting the closing price for the day before yesterday.
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# # We are calculating the absolute difference between the closing prices of yesterday and the day before yesterday.
# difference =abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# We are calculating the percentage difference between the closing prices of yesterday and the day before yesterday.
# diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
# print(diff_percent)
diff_percent = 1  # For testing purposes, we set it to 1 to ensure the next condition is met.

#TODO 5. - If TODO4 percentage is greater than 1 then print("Get News").
if diff_percent >= 1:
    print("Get News")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# We are using the News API to get articles related to the COMPANY_NAME (Tesla Inc).
if diff_percent <= 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# We are slicing the articles list to get the first 3 articles.
three_articles = articles[:3]
# print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# We are creating a new list of dictionaries that contains the headline and description of the first 3 articles.
formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

#TODO 9. - Send each article as a separate message via Twilio. 

# We are using the Twilio API to send messages with the formatted articles.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=f"{STOCK_NAME}: {'🔺' if diff_percent > 0 else '🔻'}{diff_percent:.2f}%\n{article}",
        from_="whatsapp:+14155238886",  # Twilio WhatsApp sandbox number
        to="whatsapp:+123"  # Your phone number in WhatsApp format        
    )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

