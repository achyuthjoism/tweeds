import snscrape.modules.twitter as api
import pandas as pd
import json
from tweeds.query import Query
from datetime import date


def make_json(data, jsonFilePath):
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def printRes(tweet: api.Tweet):
    print(f"{tweet.id} {tweet.date} <{tweet.user.username}> {tweet.rawContent} \n")


def toOBJ(tweet: api.Tweet) -> object:
    return {
        "id": tweet.id,
        "date": tweet.date.strftime('%Y/%m/%d'),
        "username": tweet.user.username,
        "content": tweet.rawContent,
        "likes": tweet.likeCount,
        "retweet": tweet.retweetCount,
        "reply": tweet.replyCount,
        "user": {
            "username": tweet.user.username,
            "followers": tweet.user.followersCount,
            "displayName": tweet.user.displayname,
            "id": tweet.user.id
        },
        "url": tweet.url
    }


def search(q: Query) -> None:
    """Print tweets"""
    query = ""

    if q.search:
        query += f"{q.search} "
    if q.username:
        query += f"(from:{q.username}) "
    if q.today:
        today = date.today().strftime("%Y-%m-%d")
        query += f"since:{today} "
    if q.year:
        query += f"since:{q.year}-01-01 "
    if q.until:
        query += f"until:{q.until} "
    if q.since:
        query += f"since:{q.since} "
    if q.minLikes:
        query += f"min_faves:{q.minLikes} "
    if q.minReplies:
        query += f" min_replies:{q.minReplies} "
    if q.minRetweets:
        query += f" min_retweets:{q.minRetweets} "
    if q.near:
        query += f"near:{q.near} "
    if q.geoCode:
        query += f"geocode:{q.geoCode} "
    if q.verified:
        query += f"filter:verified "
    if q.media:
        query += f"filter:media "
    if q.videos and not q.media and not q.images:
        query += f"filter:native_video "
    if q.images and not q.media and not q.videos:
        query += f"filter:images "
    if q.links:
        query += "-filter:links "
    jsonObj = {}
    csvObj = []

    for i, tweet in enumerate(api.TwitterSearchScraper(query).get_items()):
        if q.limit:
            if i == q.limit:
                break
        jsonObj[tweet.id] = toOBJ(tweet)
        csvObj.append(
            [tweet.id, tweet.date, tweet.rawContent, tweet.url,
             tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.sourceLabel[12:]]
        )
        if q.silent:
            if q.csv or q.json:
                pass
        else:
            printRes(tweet)

    if q.json:
        if q.json.find(".json") != -1:
            make_json(jsonObj, q.json)
            print("Output saved in JSON!")

    if q.csv:
        df = pd.DataFrame(
            csvObj, columns=["ID", "Date", "Tweet", "URL", "Likes", "Retweet", "Replies", "Source"])
        df.to_csv(q.csv)
        print("Output saved in CSV!")
