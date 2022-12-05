import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
from random import sample

KEYWORDS = ['autonomous vehicle', 
            'self driving car', 
            'driverless',
            'robotaxi', 
            'automated delivery robot']  # Edit to match desired keywords
START_DATE = "2020-10-12"  # Edit to match desired search start date (YYYY-MM-DD)
END_DATE = "2022-10-12"  # Edit to match desired search end date (YYYY-MM-DD)
MIN_LIKES = 2  # Edit to match minimum number of likes per tweet to be included in data
SAMPLE_SIZE = 2000  # Edit to match desired random sample size per tweet. Set to 0 if complete data set is desired

def main():
    num_tweets = dict.fromkeys(KEYWORDS, 0)
    tweets = {k:[] for k in KEYWORDS}

    for keyword in KEYWORDS:
        search_query = f"{keyword} since:{START_DATE} until:{END_DATE} min_faves:{str(MIN_LIKES)}"
        print(f"search_query: {search_query}")
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
            num_tweets[keyword] += 1
            tweets[keyword].append({'keyword': keyword,
                                    'content': tweet.content,
                                    'username': tweet.user.username,
                                    'url': tweet.url,
                                    'date': tweet.date,
                                    'likeCount': tweet.likeCount,
                                    'retweetCount': tweet.retweetCount,
                                    'replyCount': tweet.replyCount})
            print(f"{keyword}: {num_tweets[keyword]}")
    
        if SAMPLE_SIZE != 0:
            n = SAMPLE_SIZE if num_tweets[keyword] >= SAMPLE_SIZE else num_tweets[keyword]
            tweets[keyword] = sample(tweets[keyword], n)
        
        df = pd.DataFrame(tweets[keyword])
        df.to_csv('all_tweets.csv', mode='a', encoding='utf-8-sig', header=False)



if __name__ == '__main__':
    header = ['', 'keyword', 'content', 'username', 'url', 'date', 'likeCount', 'retweetCount', 'replyCount']
    with open('all_tweets.csv', mode='w', encoding='utf-8-sig') as file:
        write = csv.writer(file)
        write.writerow(header)
    main()
