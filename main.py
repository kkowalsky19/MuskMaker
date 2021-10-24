
import os
from twilio.rest import Client
account_sid = "--"
auth_token = "--"
client2 = Client(account_sid, auth_token)






# API Key



# copy-light
# API Secret Key



# copy-light
# Bearer Token




import tweepy
import time
from kucoin.client import Client
purchasedYet = 0
api_key = '--'
api_secret = '-'
api_passphrase = '-'

client = Client(api_key, api_secret, api_passphrase)
#currencies = client.get_currency('DOGE')
#print(currencies)

#order = client.create_market_order('DOGE-USDT', Client.SIDE_BUY, funds=1)








#Twitter Stuff
auth = tweepy.OAuthHandler("-", "-")
auth.set_access_token("-", "-")

api = tweepy.API(auth)
mostRecent=""

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
                #print(status.text.encode('UTF-8'))
                mostRecent = str(status.text.encode('UTF-8')).lower()
                if "@elonmusk" in mostRecent:
                    #print("N/A")
                    check=""
                else:
                    #print(mostRecent)
                    if "doge" in mostRecent:
                        print(mostRecent)
                        print("GETTING DOGEYYYY")
                        order = client.create_market_order('DOGE-USDT', Client.SIDE_BUY, funds=200)
                        message = client2.messages \
                            .create(
                                body="Musk just tweeted about Doge, buy up!",
                                from_='+----------',
                                to='+----------'
                            )
                        message = client2.messages \
                            .create(
                                body="Tell your patients you gotta go Musk just tweeted about Doge!",
                                from_='+----------',
                                to='+----------'
                            )
                        message = client2.messages \
                            .create(
                                body="Musk just tweeted about Doge, buy up!",
                                from_='+9999999999',
                                to='+9999999999'
                            )
                        #order = client.create_market_order('DOGE-USDT', Client.SIDE_BUY, funds=200)
                        print(time.ctime())
                        exit()
                
                    
                

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myStream.filter(follow=['44196397']) #1393238577299984387 #Musk: 44196397
