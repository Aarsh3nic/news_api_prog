import requests
import send_email
topic="tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-04&" \
      "sortBy=publishedAt&" \
      "apiKey=d9c96a47766248169b5947a1023bcdca" \
      "&language=en"

api_key = "d9c96a47766248169b5947a1023bcdca"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article titles and description
email_message = ""
for index, article in enumerate(content["articles"][:20]):
    if article["title"] is not None:
        email_message = email_message + "\n\n\n\n" + \
                        str((index + 1)) + ": " + \
                        "Title: " + article["title"] + "\n\n" + \
                        "Description: " + article["description"] + "\n\n"\
                        "Link: " + article["url"]

news = f"""Subject : New news! From API

{email_message}
""".encode('utf8')
# Using the utf8 decode because ASCII gives error
send_email.send_email_news(news)
