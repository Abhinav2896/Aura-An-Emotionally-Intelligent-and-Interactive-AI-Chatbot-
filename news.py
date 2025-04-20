import requests

def get_news():
    API_KEY = "YOUR_NEWSAPI_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    res = requests.get(url).json()
    articles = res['articles'][:5]
    for article in articles:
        print(article['title'])