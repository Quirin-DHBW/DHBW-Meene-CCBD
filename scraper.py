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
    db.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            timestamp TIMESTAMPZ,
            text TEXT,
            uri TEXT,
            like_count INTEGER,
            quote_count INTEGER,
            reply_count INTEGER,
            repost_count INTEGER
        )
    """)

    # This part is for directly writing it into the db
    resp = client.app.bsky.feed.search_posts(params={"q":"Trump", "limit":100})
    for post in resp.posts:
        try:
            timestamp = post.record.created_at
            text = post.record.text
            uri = post.uri
            like_count = post.like_count
            quote_count = post.quote_count
            reply_count = post.reply_count
            repost_count = post.repost_count

            db.execute("""
                INSERT INTO posts (timestamp, text, uri, like_count, quote_count, reply_count, repost_count)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (timestamp, text, uri, like_count, quote_count, reply_count, repost_count))
        except Exception as e:
            print(f"Fehler beim Verarbeiten eines Posts: {e}")

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

