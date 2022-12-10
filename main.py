import argparse as ap
import tweet_scrape as twitter
import sys


def banner():
    print("""	
	▀█▀ █░█░█ █ ▀█▀ ▀█▀ █▀▀ █▀█   █▀█ █▀ █ █▄░█ ▀█▀
	░█░ ▀▄▀▄▀ █ ░█░ ░█░ ██▄ █▀▄   █▄█ ▄█ █ █░▀█ ░█░

        by Achyuth Jois M
    """)


banner()


def process_args(args: ap.Namespace):
    match args.module:
        case "username":
            username = args.username
            json = args.json
            limit = args.limit
            sort = args.sort
            twitter.getTweetsFromUser(
                username=username, location=json, limit=limit, sort=sort)
        case "search":
            username = args.user
            json = args.json
            limit = args.limit
            sort = args.sort
            since = args.since
            until = args.until
            query = args.search
            minLikes = args.minLikes
            twitter.getSearchTweet(
                query=query, username=username,
                jsonLocation=json, limit=limit,
                sort=sort, dateFrom=since,
                dateEnd=until, minLikes=minLikes
            )


# Initializing the Arguments
parse = ap.ArgumentParser(description="Scrape twitter user tweets")
subparsers = parse.add_subparsers(dest="module")

# User module
parser_user = subparsers.add_parser(
    'username', help="Get all tweets from the user")
parser_user.add_argument("username")
parser_user.add_argument(
    '--json', type=str, help="File to write the JSON output to.")
parser_user.add_argument(
    '--limit', type=int, help="Limit of the tweets retrived"
)
parser_user.add_argument(
    '--sort', type=str, help="Sort the tweets in ascending or descending order(A/D)"
)

# Search module
parse_tweet = subparsers.add_parser(
    'search', help="Get tweets related to the search term")
parse_tweet.add_argument("search")
parse_tweet.add_argument(
    '--user', type=str, help="Tweets from a specific user"
)
parse_tweet.add_argument(
    '--since', type=str, help="Past date(YYYY-MM-DD)"
)
parse_tweet.add_argument(
    '--until', type=str, help="Latest date(YYYY-MM-DD)"
)
parse_tweet.add_argument(
    '--json', type=str, help="File to write the JSON output to.")
parse_tweet.add_argument(
    '--limit', type=int, help="Limit of the tweets retrived"
)
parse_tweet.add_argument(
    '--sort', type=str, help="Sort the tweets in ascending or descending order(A/D)"
)
parse_tweet.add_argument(
    '--minLikes', type=int, help="Minimun likes for the tweet"
)

args = parse.parse_args(args=None if sys.argv[1:] else ['--help'])

process_args(args)
