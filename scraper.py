import sys, os
os.chdir(os.path.dirname(sys.argv[0]))

# The official Bluesky API accessing package
from atproto import Client

import duckdb
from datetime import *
from time import sleep

SINCE = datetime(year=2024, month=1, day=1)
UNTIL = datetime(year=2025, month=4, day=30)
SINCE_TXT = SINCE.strftime("%Y%m%d")
UNTIL_TXT = UNTIL.strftime("%Y%m%d")
SEARCH_TERMS = ["Trump"]
POSTS_PER_DAY = 100

DO_POST_FETCH = True


single_day = timedelta(days=1)

n_days_timeframe = ((UNTIL - SINCE) // single_day) + 1


days = []
for i in range(n_days_timeframe):
    today_dt = SINCE + (i * single_day)
    tomorrow_dt = SINCE + ((i + 1) * single_day)

    today = today_dt.strftime("%Y-%m-%d")
    tomorrow = tomorrow_dt.strftime("%Y-%m-%d")

    days.append((today, tomorrow))


if DO_POST_FETCH:
    print("Logging in to Bluesky...")
    client = Client()
    with open("login.txt", "r") as login:
        creds = login.read().split("\n")
        #print(creds)
        client.login(creds[0], creds[1])

    with duckdb.connect(f"{SINCE_TXT}_{UNTIL_TXT}_posts.db") as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                timestamp TIMESTAMPTZ,
                text TEXT,
                uri TEXT,
                like_count INTEGER,
                quote_count INTEGER,
                reply_count INTEGER,
                repost_count INTEGER
            )
        """)
        for term in SEARCH_TERMS:
            for day in days:
                print(f"Pulling posts for {term} on {day[0]}...", end="\r")
                resp = None
                resp_success = False
                while not resp_success:
                    resp = client.app.bsky.feed.search_posts(params={"q":term, 
                                                                    "limit":POSTS_PER_DAY,
                                                                    "sort":"top",
                                                                    "since":f"{day[0]}T00:00:00.000Z",
                                                                    "until":f"{day[1]}T00:00:00.000Z"
                                                                    }
                                                            )
                    
                    try:
                        test = resp.posts[0].record.created_at
                        resp_success = True
                    except:
                        print("Pull unsuccessful, retrying in a second...", end="\r")
                        sleep(2)
                        continue
                

                # This part is for directly writing it into the db
                print("\nInserting posts into DB...")
                for post in resp.posts:
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
        print("Finished pulling posts.")

