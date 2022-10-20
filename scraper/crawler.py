import praw
import yaml


config=yaml.safe_load(open('configs.yaml'))

reddit_credentials = config['reddit_credentials']
reddit = praw.Reddit(
    client_id=reddit_credentials['client_id'],
    client_secret=reddit_credentials['client_secret'],
    user_agent=reddit_credentials['user_agent']
)

for submission in reddit.subreddit("whatsthisplant").hot(limit=10):
    print(submission.title)