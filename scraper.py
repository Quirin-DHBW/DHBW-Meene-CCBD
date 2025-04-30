import sys, os
os.chdir(os.path.dirname(sys.argv[0]))

# The official Bluesky API accessing package
from atproto import Client

import duckdb

client = Client()
with open("login.txt", "r") as login:
    creds = login.read().split("\n")
    #print(creds)
    client.login(creds[0], creds[1])

with duckdb.connect("bsky_posts.db") as db:
    pass

# Stop this to prevent unnecessary scraping for now (don't need to use our limited daily API calls if I have a test set saved UwU)
"""
resp = client.app.bsky.feed.search_posts(params={"q":"Trump", "limit":100})
with open("pull.txt", "w", encoding="utf-8") as f:
    print(resp)
    for post in resp.posts:
        cleaned_post_text = post.record.text.replace("\n", " <b> ")
        f.write(cleaned_post_text + "\n")
print(resp)
"""

