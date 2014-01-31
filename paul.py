import requests
from requests_oauthlib import OAuth1
from twython import Twython
from fortknox import PTLE
import csv

archive_file = 'archive.csv'

#temporary CSV archive
file = open(archive_file, 'r+')
tweet_reader = csv.DictReader(file)
print tweet_reader

#v0.1 -- twitter to user
#make call to twitter REST API

username = 'thecliffsodover'
get_request = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=10"
#callback = 

twitter = Twython(PTLE['APP_KEY'], PTLE['APP_SECRET'])
auth = twitter.get_authentication_tokens()
#need callback URL for web application
#auth = twitter.get_authentication_token(callback_url=callback)

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
#should store these in a session variable in Django when you migrate to web

#(should redirect here??) 
verify_creds = auth['auth_url']
#this is where the user_creds come from--when the user grants permission then you make
#a call to grab the USER_OAUTH_TOKENs; need to make another twython instance
#for now, we can hard code them to get the ball rolling.

auth = OAuth1(PTLE['APP_KEY'], PTLE['APP_SECRET'], PTLE['USER_OAUTH_TOKEN'], PTLE['USER_OAUTH_TOKEN_SECRET'])

r = requests.get(get_request, auth=auth)
response = r.json()

#return URLs and parse them into a dictionary

response_dict = {}

for i in response:
	grab_url = False
	date = i['created_at']
	for k in i['entities']['urls']:
		grab_url = k['expanded_url']
	if grab_url is not False:
		response_dict[date] = grab_url
keys = response_dict.keys()

#this is problematic with the way it writes to a csv
#only writes in a horizontal row, with the links only. want dates and links
tweet_writer = csv.DictWriter(file, keys)
tweet_writer.writerow(response_dict)

#need something that will persist, will check for membership.

#v0.2
#give the user the ability to annotate each entry

#v0.3
#give the user the ability to tag things using hashtags

#v0.4
#connect to tumblr

#v2.0
#wordpress widget

#v3.0
#website plugin