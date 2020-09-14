import praw

reddit = praw.Reddit('bot1')

sub_entered = input("What subreddit would you like to get posts from?")
lim = input("How many posts would you like to see?")
category = input("What category would you like the posts to be drawn from: 'Hot', 'Controversial', 'New' ?")


subreddit = reddit.subreddit(sub_entered)

if(category == "Hot"):
    for submission in subreddit.hot(limit=int(lim)):
        print("Title: " + submission.title)
        print("Author: " + str(submission.author))
        print("Text: " + str(submission.selftext))
        print("Score (Upvote + Downvote): " + str(submission.score))
if(category == "Controversial"):
  for submission in subreddit.controversial(limit=int(lim)):
        print("Title: " + submission.title)
        print("Author: " + str(submission.author))
        print("Text: " + str(submission.selftext))
        print("Score (Upvote + Downvote): " + str(submission.score))
if(category == "New"):
    for submission in subreddit.new(limit=int(lim)):
        print("Title: " + submission.title)
        print("Author: " + str(submission.author))
        print("Text: " + str(submission.selftext))
        print("Score (Upvote + Downvote): " + str(submission.score))