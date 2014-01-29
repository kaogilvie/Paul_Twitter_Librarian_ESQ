import requests
from requests_oauthlib import OAuth1
from twython import Twython
from fortknox import PTLE


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

auth = OAuth1(PTLE['APP_KEY'], PTLE['APP_SECRET'], OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

r = requests.get(get_request, auth=auth)
print r.json()

#return URLs and parse them into a list of sorts

for i in response:
	for k in i['urls']:
		grab_url = k['expanded_url']
		print grab_url

#write out a CSV // something that will get updated (append the CSV?)

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