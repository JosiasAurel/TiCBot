
import requests
import time
import datetime
import pprint


class NewsMan:
    def __init__(self):
        pass

    def get_hn_stories(self, max_stories: int = 10):
        print("max_stories", max_stories, type(max_stories))
        # stories can get upto 500
        hn_news_api_uri = "https://hacker-news.firebaseio.com/v0/"

        hn_top_stories_uri = f"{hn_news_api_uri}/topstories.json"
        # get id of latest and top 10 stories from Hacker News
        hn_latest_stories_id = requests.get(
            hn_top_stories_uri).json()[:max_stories]
        hn_latest_stories = []

        # resolve latest 10 hn top stories
        for item in hn_latest_stories_id:
            item_uri = f"{hn_news_api_uri}/item/{item}.json"
            item_data = requests.get(item_uri).json()
            if item_data.get("url", None) != None:
                # pprint.pprint(item_data)
                story_struct = {
                    "title": item_data["title"],
                    "url": item_data["url"],
                    "time": datetime.datetime.fromtimestamp(item_data["time"]).strftime('%Y-%m-%d %H:%M:%S'),
                    "author": item_data["by"]
                }
                hn_latest_stories.append(story_struct)
            else:
                pass
        return hn_latest_stories
