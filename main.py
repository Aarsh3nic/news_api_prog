import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-03-04&sortBy=publishedAt&apiKey" \
      "=d9c96a47766248169b5947a1023bcdca"

api_key = "d9c96a47766248169b5947a1023bcdca"

# Make request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article titles and description
for index, article in enumerate(content["articles"]):
      print(index+1, article["title"])
      print(article["description"])

