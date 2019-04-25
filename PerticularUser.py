import sys
import json
from tweepy import Cursor
from Permission import get_account
with open('data.txt') as f:
    array = []
    for line in f: # read rest of lines
        for x in line.split():
        	array.append(x)
for i in array:
	user=i
	client=get_account()

	file_name="{}.json".format(user)
	with open(file_name,'w')  as f:
		for page in Cursor(client.user_timeline,user_id=i,count=200).pages(16):
			for status in page:
				f.write(json.dumps(status._json)+','+"\n")