import praw
import time
user_agent = ("This is me playing with the Reddit API praw for Python. ")
r = praw.Reddit(user_agent=user_agent)

def subReturnTitles(sub='python', n=10):
    submissions = r.get_subreddit(sub).get_top(limit=n)
    for x in submissions:
        titleOnly(str(x))

def subSearch(sub='python', n=10):
    submissions = r.get_subreddit(sub).get_top(limit=n)
    for x in submissions:
        if str(x).find(sub) > 0 or str(x).find(sub.capitalize()) > 0 or str(x).find(sub.upper()) > 0:
            titleOnly(str(x))

def subGreaterThanK(sub='python', n=10, k=5):
    submissions = r.get_subreddit(sub).get_top(limit=n)
    for x in submissions:
        if int(str(x)[0:str(x).find(' ')]) >= k:
            titleOnly(str(x))

def titleOnly(i):
    print i[i.find(' :: ')+4:]
