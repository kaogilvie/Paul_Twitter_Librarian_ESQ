from twython import Twython
from fortknox import PTLE
import csv

#debug
#username = 'thecliffsodover'
#app_secret = PTLE['APP_SECRET']
#app_key = PTLE['APP_KEY']

def get_timeline(app_key, app_secret, username):
	response_dict = {}

	#try:
	#	file = open(archive_file, 'r+b')
	#	tweet_reader = csv.DictReader(file)
	#	response_dict = tweet_reader.next()
	#except IOError:
	#	print 'No archive file. New tweet timeline will be created.'

	#v0.1 -- twitter to user vai OAuth2
	twitter = Twython(app_key, app_secret, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(app_key, access_token=ACCESS_TOKEN)

	response = twitter.get_user_timeline(screen_name=username, count=100)

	for i in response:
		#get date
		grab_url = False
		date = i['created_at']
		print date
		for k in i['entities']['urls']:
			grab_url = k['expanded_url']
		if grab_url is not False:
			response_dict[date] = {'url':grab_url}
		
		#get hashtags
		hashtags = i['entities']['hashtags']
		try:
			response_dict[date]['hashtags'] = hashtags
		except KeyError:
			#no grab_url for that date, pass
			pass

		#get text of tweet
		text = i['text']
		try:
			response_dict[date]['text'] = text
		except KeyError:
			#no grab_url for that date, pass
			pass

		#can put these all together in a function, I think

	keys = response_dict.keys()


	#tweet_writer = csv.DictWriter(open(archive_file, 'wb'), keys)
	#tweet_writer.writeheader()
	#tweet_writer.writerow(response_dict)

	#v0.2
	#hoist onto the web using FLASK -- return json response and print out
	return response_dict, keys

#debug
#get_timeline(app_key, app_secret, username)

#v0.3
#parse json response into something readable
#give option to download CSV
#need to set environment variables on the linux server

#v0.4
#give user ability to authenticate to Twitter if tweets are private

#v0.5
#give the user the ability to annotate each entry

#v0.6
#give the user the ability to tag things using hashtags

#v2.0
#connect to tumblr

#v3.0
#wordpress widget

#v4.0
#website plugin