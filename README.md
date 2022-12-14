# Tweeds - Twitter Scraping Tool

<p align="center">
<img src="https://media.tenor.com/Xrt-ty39PfEAAAAC/elon-musk-smoke.gif"/>
</p>

Scrape tweets from any Twitter user profile. Twitter API alternative to scrape Twitter hashtags, threads, images, videos, statistics,
and Twitter history. Export data in JSON and CSV format. This project enables you to extract large amounts of data from Twitter.
It lets you do much more than the Twitter API, because it doesn't have rate limits and you don't even need to have a **Twitter account, a registered app,
or Twitter API key.**

### Do not forget to star this project.🌟 😍

## 💡 Features

- No API Key required
- No Limit
- No Authentication required
- Get tweets from specific user
- JSON and CSV export for further Data Analysis
- And the best part it is OpenSource 😉

## ✔️ Requirements

- Python >= 3.9

## ⚙ Installation

```bash
pip install tweeds
```

## 💃 Usage

```Bash
achyuthjoism-MBP ~ % tweeds

        ████████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░░██████╗
        ╚══██╔══╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝
        ░░░██║░░░░╚██╗████╗██╔╝█████╗░░█████╗░░██║░░██║╚█████╗░
        ░░░██║░░░░░████╔═████║░██╔══╝░░██╔══╝░░██║░░██║░╚═══██╗
        ░░░██║░░░░░╚██╔╝░╚██╔╝░███████╗███████╗██████╔╝██████╔╝
        ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═════╝░╚═════╝░

        by Achyuth Jois M

usage: tweeds [-h] [-u U] [-s S] [--since SINCE] [--until UNTIL] [--limit LIMIT] [--near NEAR] [--geocode GEOCODE]
              [--year YEAR] [--today] [--verified] [--link LINK] [--videos] [--images] [--media] [--minLikes MINLIKES]
              [--minRetweets MINRETWEETS] [--minReplies MINREPLIES] [--json JSON] [--csv CSV] [--silent]

Scrape twitter user tweets

options:
    -h, --help            show this help message and exit
    -u U                  Users Tweets you want to scrape.
    -s S                  Search for Tweets containing this word or phrase.
    --since SINCE         Filter Tweets sent since date (Example: "2017-12-27 20:30:15" or 2017-12-27).
    --until UNTIL         Filter Tweets sent until date (Example: "2017-12-27 20:30:15" or 2017-12-27).
    --limit LIMIT         Number of Tweets to pull
    --near NEAR           Find tweets near a particular location
    --geocode GEOCODE     Search for geocoded Tweets.
    --year YEAR           Filter Tweets before specified year.
    --today               Filter Tweets from today
    --verified            Display Tweets only from verified users (Use with -s).
    --links LINK          Exclude tweets containing one or more links.
    --videos              Display only Tweets with videos.
    --images              Display only Tweets with images.
    --media               Display Tweets with only images or videos.
    --minLikes MINLIKES   Minimun likes for the tweet
    --minRetweets MINRETWEETS
                          Minimun retweets for the tweet
    --minReplies MINREPLIES
                          Minimun replies for the tweet
    --json JSON           File to write the JSON output to.
    --csv CSV             To store the output in CSV
    --silent              Dont print the tweets(Only works while taking an output!)

achyuthjoism-MBP ~ %

```

## 📙 Example

### CLI Example

Some simple examples to help you understand the basics:

- `tweeds -u username` - Scrape all the Tweets of a _user_ (doesn't include **retweets** but includes **replies**).
- `tweeds -u username -s pineapple` - Scrape all Tweets from the _user_'s timeline containing _pineapple_.
- `tweeds -s pineapple` - Collect every Tweet containing _pineapple_ from everyone's Tweets.
- `tweeds -u username --since "2015-12-20 20:30:15"` - Collect Tweets that were tweeted since 2015-12-20 20:30:15.
- `tweeds -u username --since 2015-12-20` - Collect Tweets that were tweeted since 2015-12-20 00:00:00.
- `tweeds -s "Rocking Star Yash" --verified` - Display Tweets by verified users that Tweeted about Rocking Star Yash.
- `tweeds --geocode "48.880048,2.385939,1km" --csv paris.csv --limit 10` - Scrape Tweets from a radius of 1km around a place in Paris and export them to a csv file.
- `tweeds -u username --images` - Scrape Tweets from a user containing only images.
- `tweeds -u username --videos` - Scrape Tweets from a user containing only videos.
- `tweeds -u username --media` - Scarape Tweets from a user containing both images and videos.
- `tweeds -u username --links` - Scrape Tweets from a user which excludes links.
- `tweeds -u username --json file.json` - Scrape Tweets and save as a json file.
- `tweeds -u username --csv file.csv` - Scrape Tweets and save as a csv file.

### Module Example

Now Tweed can be used as a module and allows custom formatting.
Example:

```python
import tweeds

query = tweeds.Query()

query.search = "Yash Boss"
query.limit = 10
query.verified = True

tweeds.search(query)
```

**Have fun 🥰💞**

## 📮 Details

### Obvious disclaimer

This tool is for educational purposes only, I am not responsible for its use.

### Less obvious disclaimer

This project is under [MIT Licence](https://choosealicense.com/licenses/mit/), and you have to respect it.\
**Use it only in personal, criminal investigations, pentesting, or open-source projects.**
