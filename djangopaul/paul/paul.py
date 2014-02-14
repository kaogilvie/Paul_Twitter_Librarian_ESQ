from twython import Twython
from fortknox import PTLE
import csv

#via ftknox
app_key = PTLE['APP_KEY']
app_secret = PTLE['APP_SECRET']


#prompt for username
username = raw_input('Username: ')
archive_file = username+'.csv'
response_dict = {}

try:
	file = open(archive_file, 'r+b')
	tweet_reader = csv.DictReader(file)
	response_dict = tweet_reader.next()
except IOError:
	print 'No archive file. New tweet timeline will be created.'
	pass

#v0.1 -- twitter to user vai OAuth2 -- put onto Django.
twitter = Twython(app_key, app_secret, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(app_key, access_token=ACCESS_TOKEN)

response = twitter.get_user_timeline(screen_name=username, count=1)

for i in response:
	grab_url = False
	date = i['created_at']
	for k in i['entities']['urls']:
		grab_url = k['expanded_url']
	if grab_url is not False:
		response_dict[date] = grab_url
keys = response_dict.keys()

tweet_writer = csv.DictWriter(open(archive_file, 'wb'), keys)
tweet_writer.writeheader()
tweet_writer.writerow(response_dict)

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