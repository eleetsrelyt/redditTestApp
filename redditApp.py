import praw
r = praw.Reddit(user_agent='test_app')
submissions = r.get_subreddit('opensource').get_hot(limit=5)
[str(x) for x in submissions]

