
from news import NewsMan
from slackman import TiCSlackClient
from dotenv import load_dotenv
import os

# load .env
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_USER_ACCESS_TOKEN")


news_src = NewsMan()
slackman = TiCSlackClient(SLACK_BOT_TOKEN, "news")

slackman.send_message("Here are the news for today 👉")
for item in news_src.get_hn_stories():
    slackman.send_message(f"""
    / *{item.get("title")}* \n
    {item.get("url")}
    Published at {item.get("time")} by {item.get("author")}
    """)
slackman.send_message("Have a nice day y'all")
