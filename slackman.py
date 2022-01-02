
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.models.blocks.basic_components import MarkdownTextObject


class TiCSlackClient:
    def __init__(self, SLACK_API_KEY: str, news_channel_name: str):
        self.slack_client = WebClient(token=SLACK_API_KEY)
        self.news_channel_name = news_channel_name
        self.news_channel_id = None
        try:
            for result in self.slack_client.conversations_list():
                # print(result)
                for channel in result["channels"]:
                    if channel["name"] == self.news_channel_name:
                        # print(channel["id"])
                        self.news_channel_id = channel["id"]

        except SlackApiError:
            print("Could not connect with Slack servers")

    def send_message(self, markdown_text: str):
        if self.news_channel_id != None:
            self.slack_client.chat_postMessage(
                channel=self.news_channel_id, text="", blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": markdown_text
                        }
                    }
                ])
        else:
            raise "SlackClientUnitialized"
