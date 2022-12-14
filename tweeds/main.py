import argparse as ap
import sys
from tweeds.query import Query
from tweeds.tweet_scrape import search


def banner():
    print("""	
        ████████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░░██████╗
        ╚══██╔══╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝
        ░░░██║░░░░╚██╗████╗██╔╝█████╗░░█████╗░░██║░░██║╚█████╗░
        ░░░██║░░░░░████╔═████║░██╔══╝░░██╔══╝░░██║░░██║░╚═══██╗
        ░░░██║░░░░░╚██╔╝░╚██╔╝░███████╗███████╗██████╔╝██████╔╝
        ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═════╝░╚═════╝░

        by Achyuth Jois M
    """)


banner()


def config(args: ap.Namespace):
    c = Query()
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
    c.verified = args.verified
    c.geoCode = args.geocode
    c.links = args.links
    c.videos = args.videos
    c.images = args.images
    c.media = args.media
    c.year = args.year
    c.today = args.today

    return c


def process_args(args: ap.Namespace):
    q = config(args)
    search(q)


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
        '--geocode', type=str, help="Search for geocoded Tweets."
    )
    parse.add_argument(
        '--year', type=int, help="Filter Tweets before specified year."
    )
    parse.add_argument(
        '--today', help="Filter Tweets from today", action='store_true'
    )
    parse.add_argument(
        '--verified', help="Display Tweets only from verified users (Use with -s).", action='store_true'
    )
    parse.add_argument(
        '--links', help="Exclude tweets containing one or more links.", action='store_true'
    )
    parse.add_argument(
        "--videos", help="Display only Tweets with videos.", action='store_true'
    )
    parse.add_argument(
        "--images", help="Display only Tweets with images.", action='store_true'
    )
    parse.add_argument(
        "--media", help="Display Tweets with only images or videos.", action='store_true'
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
        '--silent', help="Don't print the tweets(Only works while taking an output!)[Type anything]", action='store_true'
    )

    args = parse.parse_args(args=None if sys.argv[1:] else ['--help'])

    process_args(args)
