import sys, os
os.chdir(os.path.dirname(sys.argv[0]))

from atproto import Client

client = Client()
with open("login.txt", "r") as login:
    creds = login.read().split("\n")
    #print(creds)
    client.login(creds[0], creds[1])

resp = client.app.bsky.feed.search_posts(params={"q":"Book"})
print(resp)

