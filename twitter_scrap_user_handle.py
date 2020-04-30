
# import libraries
from twitterscraper import query_tweets_from_user
import datetime as dt
import pandas as pd

# number of tweets
limit = 1000

# user tweets
user = input('Enter twitter username (case sensitive) without @: ')


# all tweets within limit
tweets = query_tweets_from_user(user,limit=limit)

# convert twitter object into DataFrame
df = pd.DataFrame(tweet.__dict__ for tweet in tweets)

# clean tweets and remove retweets
df = df[df['screen_name'] == user]

# output in csv
df.to_csv(user + '-output.csv',index=False)