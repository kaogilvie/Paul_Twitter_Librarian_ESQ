from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def paul():
	return render_template('paul.html')

@app.route("/annals")
def annals():
	return 'results page'

if __name__ == '__main__':
	app.debug = True
	app.run()