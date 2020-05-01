
# import libraries
from twitterscraper import query_tweets_from_user
import pandas as pd
import extract_text_from_url as et


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
df['text'] = df['text'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))


# convert user text to lowercase
df['text'] = df['text'].apply(lambda x: x.lower())

# extract url from text
def get_url_from_text(text):
    text_arr = text.split(' ')
    for t in text_arr:
        if("https://") in t: 
            return t[t.find('https://'):]
    return 'NA'

# remove url from text
def remove_url_from_text(text):
    t = get_url_from_text(text)
    return text.replace(t,'')

# save clean text
df['message_text_only'] = df['text'].apply(lambda x: remove_url_from_text(x))

# save extracted url
df['url_links'] = df['text'].apply(lambda x: get_url_from_text(x))

# extract and save text from url
df['url_text'] = df['url_links'].apply(lambda x: et.extract_text_from_url(x))

# output in csv
df.to_csv(user + '-output.csv',index=False)

if __name__ == "__main__":
    pass