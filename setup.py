from setuptools import setup, find_packages

long_description = """"Scrape tweets from any Twitter user profile. Twitter API alternative to scrape Twitter hashtags, threads, images, videos, statistics,
and Twitter history. Export data in JSON and CSV format. This project enables you to extract large amounts of data from Twitter.
It lets you do much more than the Twitter API, because it doesn't have rate limits and you don't even need to have a **Twitter account, a registered app,
or Twitter API key.**"""

setup(
    name='tweeds',
    version='2.1.2.3',
    author='Achyuth Jois M',
    author_email='developer.arjm@gmail.com',
    packages=find_packages(include=['tweeds', 'tweeds.*']),
    install_requires=["snscrape==0.5.0.20230113", "pandas==1.5.3"],
    license='MIT',
    license_files=('LICENSE.md'),
    url='https://github.com/achyuthjoism/Twitter-OSINT',
    description='An advanced Twitter scraping & OSINT tool.',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'tweeds = tweeds.main:main',
        ]
    },
)
