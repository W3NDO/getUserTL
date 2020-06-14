import click
import tweepy
from colorama import Fore, Back, Style 
import re


@click.command()
@click.argument('username')
def getUsername(username):
    click.echo('Welcome to CLI Twitter Search')
    click.echo('Usage: [python3 getUserTimeline \'username\' ] \n')
    click.echo(' Example: python3 getUserTimeline w3ndo_ \n' )
    click.echo('Retweets are Red, tagged tweets are Blue and Normal Tweets are Green \n' )
    click.echo('Requires a Twitter Developer account \n')  

    #Get Twitter Credentials
    click.echo('Let\'s Get you logged in: \n')
    consumer_key = click.prompt('Please enter your account\'s Consumer Key', type = click.STRING)
    consumer_secret = click.prompt('Please Enter your account\'s Consumer Secret', type =  click.STRING) 
    access_token =  click.prompt('Please Enter your account\'s access token', type = click.STRING) 
    access_token_secret = click.prompt('Please Enter your account\'s access token secret', type = click.STRING) 

    #login to twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = []

    for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items():
        tweets.append(status.full_text)   
        for tweet in tweets:
            if tweet.split(' ')[0] == 'RT':
                print(Fore.RED + tweet)
            elif re.search('^@', tweet.split(' ')[0]) :
                print(Fore.BLUE + tweet)
            else:
                print(Fore.GREEN + tweet) 

if __name__ == '__main__':
    getUsername()
