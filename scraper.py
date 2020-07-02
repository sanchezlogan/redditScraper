import praw


##Authenication ##
reddit = praw.Reddit(client_id="ID",
                     client_secret="Secret",
                     password="Pass",
                     user_agent="UA",
                    username= "UN")

##Authenication ##




##Test of successful login
print('Logged in as: ' + str(reddit.user.me()))

##test of subreddit access ##
subReddit = reddit.subreddit("redditdev")
print("Accessing subreddit: " + str(subReddit.display_name) + "\n")


for submission in subReddit.new(limit=2):
    print("################################\n")
    print(str(submission.author.name) + ": " + submission.title+ "\n")




    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        print("\t" + str(comment.author) + " responded: \n")
        print("\t\t" + str(comment.body) + '\n')
        print("\t\tPost made at: " + str(comment.created_utc) + '\n')
        
        

    

