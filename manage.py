import cat-to-slack

CAT_URL = "https://www.reddit.com/r/CatGifs/hot.json"
CAT_PARAMS = {"sort": "top", "t": "day", "limit": "100"}
CAT_HEADERS = {"user-agent": "Cat to Slack 1.1"}

cat_collection = collections.deque([], 100)
posted_cats = collections.deque([], 14)

INCOMING_WEBHOOK_URL = os.environ.get("INCOMING_WEBHOOK_URL")
CAT_EMOJIS = [
    ":smiley_cat:",
    ":smile_cat:",
    ":joy_cat:",
    ":heart_eyes_cat:",
    ":smirk_cat:",
    ":kissing_cat:",
    ":scream_cat:",
    ":crying_cat_face:",
    ":pouting_cat:",
    ":cat:",
    ":cat2:",
]

PAYLOAD_PARAMS = {
    "channel": os.environ.get("CAT_CHANNEL"),
    "username": "daily_cats",
    "unfurl_media": True,
    "unfurl_links": True,
}


CAT_TIMES = os.environ.get("CAT_TIMES", "10:00").split(",")

if __name__=="__main__":
    for cat_time in CAT_TIMES:
        logging.info(f"Adding daily schedule at {cat_time}")
        schedule.every().day.at(cat_time).do(post_new_cat)
    
    while True:
        schedule.run_pending()
        time.sleep(1)