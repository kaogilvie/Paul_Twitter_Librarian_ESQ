from flask import Flask, render_template, request
from fortknox import PTLE
import paul
import requests
import lxml.html
#from lxml import etree

app = Flask(__name__)

#app variables
app_key = PTLE['APP_KEY']
app_secret = PTLE['APP_SECRET']

@app.route("/")
def paul_home():
	return render_template('paul.html')

@app.route("/annals", methods=['GET', 'POST'])
def annals():
	if request.method == 'POST':
		username = request.form['username']
		response, keys = paul.get_timeline(app_key, app_secret, username)
		titles = []
		#example of grabbing title
		for key in keys:
			r = requests.get(response[key]['url'])
			tree = lxml.html.fromstring(r.text)
			title = tree.xpath('/html/head/title/text()')
			response[key]['title'] = title[0]
		return render_template('annals.html', response_dict=response, response_keys=keys, titles=titles)
	else:
		return 'get request'

if __name__ == '__main__':
	app.debug = True
	app.run()