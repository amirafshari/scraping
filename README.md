# Iran-500-Top-Websites
500 Top Website in Iran based on Alexa Ranking.

You can use Alexa API for more reliable result, I scraped GooyaTech and this is the result.

Source Page:
https://gooyatech.com/top-sites-in-iran-by-alexa/
Note: In the time of writing this, there is a significant bias between our result and the real ranking, for example the ranking of Tsetmc.com in Alexa is 10, but our source says it's 7, since we picked it from the head, there is more bias in the tail!


$ Conver the list to Pandas Series
$ pd.set_option('display.max_rows', None)
ranking = pd.Series(alexa)
ranking
