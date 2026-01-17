import feedparser


RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    "https://weworkremotely.com/categories/remote-programming-jobs.rss"
]


def get_rss_jobs():
    jobs = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            title = entry.get("title", "")
            link = entry.get("link", "")
            company = entry.get("author", "Unknown")

            jobs.append({
                "title": title,
                "company": company,
                "link": link,
                "source": "RSS"
            })

    return jobs
