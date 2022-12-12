import argparse as ap
import sys
import tweeds.classes.query as query
import tweeds.tweet_scrape as ts


def banner():
    print("""	
	▀█▀ █░█░█ █ ▀█▀ ▀█▀ █▀▀ █▀█   █▀█ █▀ █ █▄░█ ▀█▀
	░█░ ▀▄▀▄▀ █ ░█░ ░█░ ██▄ █▀▄   █▄█ ▄█ █ █░▀█ ░█░

        by Achyuth Jois M
    """)


banner()


def config(args: ap.Namespace):
    c = query.Query()
    c.search = args.s
    c.username = args.u
    c.limit = args.limit
    c.json = args.json
    c.since = args.since
    c.until = args.until
    c.near = args.near
    c.minLikes = args.minLikes
    c.csv = args.csv
    c.minReplies = args.minReplies
    c.minRetweets = args.minRetweets
    c.silent = args.silent

    return c


def process_args(args: ap.Namespace):
    q = config(args)
    ts.search(q)


def main():
    parse = ap.ArgumentParser(description="Scrape twitter user tweets")

    parse.add_argument("-u", help="User's Tweets you want to scrape.")
    parse.add_argument(
        "-s", help="Search for Tweets containing this word or phrase.")
    parse.add_argument(
        '--since', type=str, help="Filter Tweets sent since date (Example: \"2017-12-27 20:30:15\" or 2017-12-27)."
    )
    parse.add_argument(
        '--until', type=str, help="Filter Tweets sent until date (Example: \"2017-12-27 20:30:15\" or 2017-12-27)."
    )
    parse.add_argument(
        '--limit', type=int, help="Number of Tweets to pull"
    )
    parse.add_argument(
        '--near', type=str, help="Find tweets near a particular location"
    )
    parse.add_argument(
        '--minLikes', type=int, help="Minimun likes for the tweet"
    )
    parse.add_argument(
        '--minRetweets', type=int, help="Minimun retweets for the tweet"
    )
    parse.add_argument(
        '--minReplies', type=int, help="Minimun replies for the tweet"
    )
    parse.add_argument(
        '--json', type=str, help="File to write the JSON output to.")
    parse.add_argument(
        '--csv', type=str, help="To store the output in CSV"
    )
    parse.add_argument(
        '--silent', type=str, help="Don't print the tweets(Only works while taking an output!)[Type anything]"
    )

    args = parse.parse_args(args=None if sys.argv[1:] else ['--help'])

    process_args(args)
