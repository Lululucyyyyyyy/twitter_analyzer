from flask import Flask, request, render_template
from twitter_analyzer import TweetAnalyzer
import requests
import twitter_analyzer
import os

app = Flask(__name__)
my_list = []
x = os.path.realpath('/Users/wenmo/Development/twitter_analyzer/tweets.txt')

@app.route("/")
def my_form():
	my_text = request.args.get('text')
	tweets = get_tweets(my_text)
	positive_sent = 0
	negative_sent = 0
	for tweet in tweets:
		analyzer1 = TweetAnalyzer()
		positive_sent += analyzer1.analyze_the_comment(tweet)[0]
		negative_sent += analyzer1.analyze_the_comment(tweet)[1]
	pos = "{0:.0%}".format(positive_sent)
	neg = "{0:.0%}".format(negative_sent)
	if my_text != None:
		return render_template('analyzer.html', tweets=tweets, text=my_text, pos=pos, neg=neg)
	else:
		return render_template('analyzer.html')
	

# HELPER FUNCTIONS
def get_tweets(searchitem):
	url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)
	headers = {'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPaX9QAAAAAAu7ce9TNVPW69PM%2FPBt3pnG7HwIs%3D8AU4fkXFf7Fh475qNji0oDYClOnVsrCu85NLPWhguhHYozCXsJ'}
	res = requests.get(url, headers=headers)
	tweet = res.json()
	print('this is searchitem', searchitem)
	tweets = []
	for thing in tweet['statuses']:
		text = thing['text']
		tweets.append(text)
	return tweets

'''
@app.route('/tweet', methods=['GET', 'POST'])
def dictionary():
	if request.method == 'POST':
		my_text = request.form['text']
		my_list.append(my_text)
	return render_template('dictionary.html', my_list=my_list)

	
@app.route('/tweet2', methods=['GET', 'POST'])
def file():
	if request.method == 'POST':
		my_text = request.form['text']
		set_file(my_text)
	listt = get_file()
	return render_template('file.html', list=listt)

def set_file(my_text):
	with open(x, "a") as f:
		f.write(my_text + "\n")

def get_file():
	with open(x, "r") as g:
		temp = g.read()
		my__other_list = temp.split()
		return my__other_list
'''

if __name__ == '__main__':
	app.run()

