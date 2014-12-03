import twitter
import json

CONSUMER_KEY = 'CM4EcAjVV3cfZMQmkIwuTxpgE'
CONSUMER_SECRET = '4ZxRFhTMsiIvXw7xLCyX8ULqhEQg4FpFLbQKgz0cPJWNIqcWyT'
OAUTH_TOKEN = '320714038-9PsT937H8jrpVbhBeF2iJJDmDpioOzUCEUyMcxjb'
OAUTH_TOKEN_SECRET = raw_input("\nEnter OAUTH_TOKEN_SECRET: ")

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth = auth)

	
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

world_trends_set = set([trend['name'] 

                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] 
                     for trend in us_trends[0]['trends']]) 

common_trends = world_trends_set.intersection(us_trends_set)

print common_trends
