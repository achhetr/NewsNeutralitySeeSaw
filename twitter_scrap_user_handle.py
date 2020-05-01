
# import libraries
from twitterscraper import query_tweets_from_user
import pandas as pd

# number of tweets
limit = 5

# user tweets
user = input('Enter twitter username without @: ')
user = user.lower()


# all tweets within limit
tweets = query_tweets_from_user(user,limit=limit)

# convert twitter object into DataFrame
df = pd.DataFrame(tweet.__dict__ for tweet in tweets)

# clean tweets and remove retweets
df['screen_name'] = df['screen_name'].apply(lambda x: x.lower())
df = df[df['screen_name'] == user]

# convert user text to UTF-8 ---------------------Work in progress
df['text'] = df['text'].apply(lambda x: x)

# convert user text to lowercase
df['text'] = df['text'].apply(lambda x: x.lower())

# remove all urls
def remove_url_from_text(text):
    t = get_url_from_text(text)
    return text.replace(t,'')

def get_url_from_text(text):
    text_arr = text.split(' ')
    for t in text_arr:
        if("https://") in t: 
            return t[t.find('https://'):]
    return 'NA'

df['message_text_only'] = df['text'].apply(lambda x: remove_url_from_text(x))
df['url_links'] = df['text'].apply(lambda x: get_url_from_text(x))


# output in csv
df.to_csv(user + '-output.csv',index=False)