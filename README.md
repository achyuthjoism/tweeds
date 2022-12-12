<h1>Tweeds - Twitter Scraping Tool</h1>
<p align="center"><img src="https://media.tenor.com/Xrt-ty39PfEAAAAC/elon-musk-smoke.gif"/></p>

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
![Basic](https://files.catbox.moe/ph7txh.png)

## 📙 Example
Getting tweets from a specific user
```Bash
tweeds -u TheNameisYash --json yashtweets.json
```
Getting tweets from a search term or #hastag
```Bash
tweeds -s "#Messi" --json messigoat.json --minLikes 10000 --limit 100
```
Getting tweets from a specific region (.ie Paris)
```Bash
tweeds -s "coffee sucks" --near Paris --limit 100
```
A some more simple examples to help you understand the basics:

- `tweeds -u username` - Scrape all the Tweets of a *user* (doesn't include **retweets** but includes **replies**).
- `tweeds -u username -s pineapple` - Scrape all Tweets from the *user*'s timeline containing _pineapple_.
- `tweeds -s pineapple` - Collect every Tweet containing *pineapple* from everyone's Tweets.
- `tweeds -u username --since "2015-12-20 20:30:15"` - Collect Tweets that were tweeted since 2015-12-20 20:30:15.
- `tweeds -u username --since 2015-12-20` - Collect Tweets that were tweeted since 2015-12-20 00:00:00.
- `tweeds -u username --csv file.csv` - Scrape Tweets and save as a csv file.
- `tweeds -u username --json file.json` - Scrape Tweets and save as a json file.

**Have fun 🥰💞**

## 📮 Details

### Obvious disclaimer

This tool is for educational purposes only, I am not responsible for its use.

### Less obvious disclaimer

This project is under [MIT Licence](https://choosealicense.com/licenses/mit/), and you have to respect it.\
**Use it only in personal, criminal investigations, pentesting, or open-source projects.**
