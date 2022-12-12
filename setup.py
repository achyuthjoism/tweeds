from setuptools import setup, find_packages

setup(
    name='tweeds',
    version='1.0',
    author='Achyuth Jois M',
    packages=find_packages(include=['tweeds', 'tweeds.*']),
    install_requires=[
        'pandas',
        'snscrape'
    ],
    license='MIT',
    license_files=('LICENSE.md'),
    description='An advanced Twitter scraping & OSINT tool.',
    entry_points={
        'console_scripts': [
            'tweeds = tweeds.main:main',
        ]
    },

)
