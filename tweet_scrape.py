import snscrape.modules.twitter as twitter
import pandas as pd
import json
import csv
import time


def writeToJSONFile(fileName, data):
    filePathNameWExt = fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def getTweetsFromUser(username, location, limit, sort):
    print(f"Fetching the tweets from {username}")
    tweets = []
    start = time.time()
    count = 0
    items = twitter.TwitterUserScraper(username=username).get_items()
    for i, tweet in enumerate(items):
        count += 1
        if limit != None:
            if i >= limit:
                break
        tweets.append(
            [tweet.id, tweet.date, tweet.likeCount, tweet.content])
    df = pd.DataFrame(
        tweets, columns=["ID", "Date", "Likes", "Content"])
    if sort == "A":
        df = df.sort_values(by=['Likes'])
    elif sort == 'D':
        df = df.sort_values(by=['Likes'], ascending=False)
    df.to_csv("csv/users/"+username+".csv")
    if location != None:
        if location.endswith(".json"):
            make_json("csv/users/"+username+".csv", "json/users/"+location)
        else:
            print("Enter a valid file name")
    end = time.time()
    print(f"Got {count} tweets in {int(end-start)}secs")


def getSearchTweet(username, jsonLocation, dateFrom, dateEnd, limit, sort, minLikes, query="messi"):
    print(f"Fetching the tweets related to {query}")
    finalQuery = query+" "
    if username != None:
        finalQuery += f"(from:{username}) "
    if dateEnd != None:
        finalQuery += f"until:{dateEnd} "
    if dateFrom != None:
        finalQuery += f"since:{dateFrom} "
    if minLikes != None:
        finalQuery += f"min_faves:{minLikes} "
    tweets = []
    start = time.time()
    count = 0
    items = twitter.TwitterSearchScraper(query=finalQuery).get_items()
    for tweet in items:
        count += 1
        if limit != None:
            if len(tweets) == limit:
                break
        tweets.append(
            [tweet.id, tweet.date, tweet.likeCount, tweet.content])
    df = pd.DataFrame(
        tweets, columns=["ID", "Date", "Likes", "Content"])
    if sort == "A":
        df = df.sort_values(by=['Likes'])
    elif sort == 'D':
        df = df.sort_values(by=['Likes'], ascending=False)
    df.to_csv("csv/search/"+query+".csv")
    if jsonLocation != None:
        if jsonLocation.endswith(".json"):
            make_json("csv/search/"+query+".csv", "json/search/"+jsonLocation)
        else:
            print("Enter a valid file name")
    end = time.time()
    print(f"Got {count} tweets in {int(end-start)}secs")
