from setuptools import setup, find_packages
import io
import os

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='tweeds',
    version='1.1',
    author='Achyuth Jois M',
    author_email='developer.arjm@gmail.com',
    packages=find_packages(include=['tweeds', 'tweeds.*']),
    install_requires=[
        'pandas',
        'snscrape'
    ],
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
