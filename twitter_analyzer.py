
import requests
import os
import csv
import time
import pprint

x = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
y = os.path.realpath('/Users/wenmo/Development/polyglot/cohort-1/data/goodwords.txt')
z = os.path.realpath('/Users/wenmo/Development/polyglot/cohort-1/data/badwords.txt')

tweets = set()
goodwords = set()
badwords = set()

#create sets for words
def wordlists(path, set):
    with open(path, "r") as g:
        line = g.readlines()
        for word in line:
            words = word.split(',')
            for i in words:
                temp = i
                temp = temp.strip(' ')
                temp = temp.strip('\n')
                set.add(temp)
wordlists(y, goodwords)
wordlists(z, badwords)


class TweetAnalyzer:
    def __init__(self):
        self.goodwords = goodwords
        self.badwords = badwords

    def analyze_the_comment(self, comment):
        gnum = 0
        bnum = 0
        words = comment.lower().split()
        total = len(words)
        for word in words:
            if word in self.goodwords:
                gnum += 1
            if word in self.badwords:
                bnum += 1
        comment_sentiment_pos = gnum / total
        comment_sentiment_neg = bnum / total
        return [comment_sentiment_pos, comment_sentiment_neg]





        