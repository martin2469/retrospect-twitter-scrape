# retrospect-twitter-scrape
Contains Python script to scrape tweets based on a number of parameters. Developed for Retrospect Technology in QMSS 451.

### Setup
In order to run the script, you must first make sure you've installed all necessary dependencies. Ensure Python and pip are updated, then run:
```
pip3 install -r requirements.txt
```

### Customizing search parameters
The provided Python script is highly customizable. Simply open *`scrape_tweets.py`* in your text editor of choice, and edit the global variables (distinguished by their all-caps format) to your desired parameters. Reference the table below for more details on the functionality of each variable:

| Variable Name   | Functionality                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------|
| `KEYWORDS`      | A list of strings to search for. The script will conduct a twitter search for each item in KEYWORDS. |
| `START_DATE`    | Limits the twitter search to tweets published from START_DATE. Stored in "YYYY-MM-DD" format.        |
| `END_DATE`      | Limits the twitter search to tweets published until END_DATE. Stored in "YYYY-MM-DD" format.         |
| `MIN_LIKES`     | Restricts twitter search to those tweets containing at least MIN_LIKES likes.                        |
| `SAMPLE_SIZE`   | Sets size of random sample. Set equal to 0 if entire dataset is desired.                             |

As previously stated, the script is highly customizable. Because of this, different use cases require you to set variables to different values. In order to retrieve a dataset adequate for longitudinal (time series) analysis, ensure `SAMPLE_SIZE = 0`. For sentiment analysis, it may be useful to limit the number of tweets retrieved per keyword, retrieving a random sample of all tweets in a given time period. This would require you to set `SAMPLE_SIZE` to your desired number of tweets per keyword (such as `SAMPLE_SIZE = 2000` for our analysis)

### Executing the script
After setting all parameters to reflect your desired dataset, you can run the script as such:
```
python3 scrape_tweets.py
```
Depending on the popularity of your keywords and the restrictiveness of your parameters, the script may take over an hour to execute. As such, the program will continually print the keyword it is currently scraping, as well as the number of tweets that have been scraped for the current keyword.

Upon finishing the scrape for each keyword, the script will append results to *`all_tweets.csv`*, meaning not all keywords have to be scraped in one sitting. After finishing the scrape for all the keywords, *`all_tweets.csv`* will contain the output dataset, containing the desired number of tweets per keyword. 
