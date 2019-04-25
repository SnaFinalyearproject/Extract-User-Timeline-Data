import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_auth():
	try:
		consumer_key=" "
		consumer_secret=" "
		access_token=" "
		access_secret=" "
	except KeyError:
		sys.exit(1)
	
	auth=OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_secret)

	return auth;

def get_account():
	auth=get_auth()
	user=API(auth)
	return user
	