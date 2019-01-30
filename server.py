from flask import Flask, request, render_template
from twitter_analyzer import TweetAnalyzer

app = Flask(__name__)

@app.route("/")
def my_form():
	my_text = request.args.get('text')
	tweets = get_tweets(my_text)
	return render_template('analyzer.html', my_text=my_text)


# HELPER FUNCTIONS
def get_tweets(searchitem):
	url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23{}&result_type=recent'.format(searchitem)
	headers = {'authorization': '<BEARERTOKEN>'}
	res = requests.get(url, headers=headers)
	tweet = res.json()
	tweets = []
	for thing in tweet:
		tweets.append(tweet)
	return tweets
	
if __name__ == '__main__':
	app.run()