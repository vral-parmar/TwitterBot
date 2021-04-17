#tweet.py file
#Author  : 	Viral Parmar   
#Github  : 	https://github.com/vral-parmar
#Twitter : 	https://twitter.com/vral_parmar
#live Bot:	https://twitter.com/TaelynCorb

import tweepy
from time import sleep
from Cred import *
import logging
from multiprocessing import Process

logging.basicConfig(filename="Tweetlog.log", format='%(asctime)s %(message)s', filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
print('You can Check twitted Log in Project Root directory')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def reTweet():
    for tweet in tweepy.Cursor(api.search, q=('#CyberSecurity OR #infosec OR #Hacking OR #Linux -filter:retweets'), lang='en').items(5):
        try:
            # print('\nTweet by: @' + tweet.user.screen_name + tweet.text)
            tweet.retweet()

            print('Retweeted tweet')
            logger.info('\nTweet by: @' + tweet.user.screen_name + tweet.text)
            logger.info("===================== Retweeted Above Tweet ============================")
            
            sleep(20)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def likeTweet():
    for tweet in tweepy.Cursor(api.search, q=('#Malware OR #databreach OR #security OR #Linux -filter:retweets'),lang='en').items(10):
            try:
                # print('\nTweet by: @' + tweet.user.screen_name + tweet.text)
                tweet.favorite()

                print('Liked Tweet')
                logger.info('\nTweet by: @' + tweet.user.screen_name + tweet.text)
                logger.info("------------------------ Liked Above Tweet -------------------------")
                
                sleep(10)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

if __name__ == '__main__':
    Process(target=reTweet).start()
    Process(target=likeTweet).start()
