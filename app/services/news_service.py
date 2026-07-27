import feedparser


class NewsService:

    def latest(self, coin="crypto"):

        feed = feedparser.parse(
            "https://cointelegraph.com/rss"
        )

        news = []

        for item in feed.entries[:5]:
            news.append({
                "title": item.title,
                "link": item.link,
            })

        return news


news_service = NewsService()
