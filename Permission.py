import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_auth():
	try:
		consumer_key="hWC6lYlmoOmkuWYOK9wjV0nNQ"
		consumer_secret="bl6DUjkTsMjfKbP9uEGbbFV6rLEZjUSqPMPcC7CIWenjeEWtzM"
		access_token="1100439059544055811-ppzMhkgecGg8Kw58wYPERjFpl5dBoR"
		access_secret="Iejcim3pwDZluXrboGm6i27FWzViVAcZNHsCkTbsErFxS"
	except KeyError:
		sys.exit(1)
	
	auth=OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_secret)

	return auth;

def get_account():
	auth=get_auth()
	user=API(auth)
	return user
	