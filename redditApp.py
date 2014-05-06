import praw
r = praw.Reddit(user_agent='app')

def subsearch(sub='python', n=10):
    submissions = r.get_subreddit(sub).get_hot(limit=n)
    for x in submissions:
        if str(x).find(sub) > 0 or str(x).find(sub.capitalize()) > 0 or str(x).find(sub.upper()) > 0:
            print x

def greaterthan(sub='python', n=10, k=5):
    submissions = r.get_subreddit(sub).get_hot(limit=n)
    for x in submissions:
        if int(str(x)[0:str(x).find(' ')]) >= k:
            print x
