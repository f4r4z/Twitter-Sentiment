# Twitter Sentiment Analysis
A Twitter Sentiment analysis of the Twitter account @TheTempleNews

## Abstract
In this paper, the sentiment analysis classification of tweets is studied using supervised learning. The train dataset is a fairly small dataset containing 200 tweets, from the twitter account ​@TheTempleNews​. The test set included 60 tweets from the same account. Tweets were manually categorized in the labels positive or negative in favor of Temple University. This means that the positivity and negativity is biased and dependent on the effect of the tweet on Temple University.

## Introduction
Sentiment analysis is the process of contextualizing text and categorizing it into sentiments or opinions. A common example of sentiment analysis is dividing news articles into categories such as sports, politics, etc. Natural language processing is used in this process in order to determine the category of text or speech.
In today’s high usage of social media, sentiment analysis can help us identify the context of online contents and categorize them. This helps us in many ways such as identifying online text as harmful, opinion mining around the release of a new product, or even something as simple as identifying emotions of a twitter account.
I focused on two simple human emotions on the twitter account ​@TheTempleNews​, positive and negative. Since this account focuses on news from Temple University, this classification of tweets can help us identify the percentage of positive tweets (good or neutral news) and negative tweets (bad news) about Temple. The percentages will give us a quick overall of the past few events in the university, and users can abstract the results into an overall vibe around the university. For example, someone could look at the recent tweets from the past week and say if Temple had a good week in terms of sports, education, and safety.

## Data
#### Dataset
I extracted 200 tweets from ​@TheTempleNews i​ n order to label. Initially I used the twitter api, wrote a script in python, and extracted tweets into one column of a csv file. Then I manually labeled each tweet by reading each tweet one-by-one. As a result, all labels are my personal opinion and the final results will be based on this initial opinion as well.
Also 60 tweets were extracted later after a couple of days so the test dataset would contain newer tweets. The reason I extracted the tests tweets later was to test the accuracy of the sentiment analysis on newer tweets that have not existed at the time of training. This would be more useful as our final goal is to analyze new tweets.
An important note to make on my labeling is that my goal was to create this sentiment analysis for binary classification, therefore I only counted each tweet as positive or negative. Most of the tweets on the account were either positive or news without emotions. As a result, I labeled any news that was not bad as positive, and any bad news as negative. This leads to my data having more positive tweets in general.

#### Preprocessing
The regex library ‘re’ in python was used in order to preprocess text of tweets. Using online resources, I found regex code for the ‘re’ library to clean up text[​ 1]​. The major concern in preprocessing was to remove extra words and characters from each tweet. First step in the preprocessing was to remove all the extra punctuation, URLs, and usernames. Also meaningless repetition of letters would be removed. The next step in the preprocessing step was to tokenize the words. Only nouns and adjectives in the tweet would go into tokenization. This tokenization would be a list of words.
The final dataset was converted into a dictionary. The key is the tweet, and the label would be the value. The model will be trained based on this format of inputs and labels.
Initially, the frequency of the words were plotted, and I realized that there are words that might not affect the label. After some trials, I decided to remove these words which are called stopwords using the ‘re’ library. The graphs of the word frequency before and after removing stopwords is shown below.
The top figures show the frequency of top 50 words. First figure includes the stopwords and second figure does not. As seen in the figures, after removing the stopwords, a noise is removed from the graph. If the count of a particular word is high, it means that a lot of tweets contain that word, which means it is not a good indicator of positive or negative. For example the word “USER_NAME” which is a replacement for every username used in the tweet, is repeated a lot in negative and positive tweets.
The count of words after the initial high used words flattens out, and most of the top 50 words are repeated about the same amount. If the data points were higher, then the number of these words per label would increase and the results would become more accurate.

## Methodology
Na​ïve Bayes classifiers are a method of classification which are probabilistic. ​Na​ïve Bayes classifiers work well on sentiment analysis because they work well on text categorization[​ 2]​. The algorithm trains a model which calculates the probability of the sentiment being positive or negative given the count (frequency) of features or word vectors. I used online resources to understand and ease the process of vectorization.[​ 3]​ After vectorization of each word and conversion into a dictionary of vectors, we use these vectors in order to get our training features and train our model using the ‘nltk’ library.
The same steps of preprocess and vectorization were taken on the test set as well so we can later input it into our model easily.

## Results
The test dataset was obtained separately from the training dataset and after a few days with new tweets. After vectorication of the test set, a script was written to count all the correct analysis compared to my manual label and calculate the accuracy. The test set contained 60 tweets which is 0.3 times the training dataset.
Two accuracy tests were performed on the test dataset; one contained the stopwords and the other did not. Surprisingly, the accuracy was not much different although I hypothesized that the stopwords would have a larger effect on the accuracy.
The final accuracies on the test dataset can be seen in the table below:
| Accuracy with removing stopwords    | 78.68852% | 
|-------------------------------------|-----------|
| Accuracy without removing stopwords | 77.04918% |


Since the dataset was small, I took a look at the mistakes of the sentiment analysis per tweet to try to figure out what was not done to increase the accuracy.
The table below shows the percentages more in detail on the test dataset:
|       | Positive | Negative | 
|-------|----------|----------|
| True  | 66.6667% | 13.3333% |  
| False | 16.6667% | 3.3333%  |

As we can see, the percentage of false positives is higher than true negatives. The issue with this is that the sentiment analysis model tries to guess tweets as “positive” most of the time. Also the false negative percentage is much lower which shows that if the model guesses the sentiment is negative, then there is a much higher chance that it is. The reason for this is explained further in the conclusion section.


## Conclusion
To summarize this project, two sets of tweets were gathered from The Temple News Twitter account using a script, one for the purpose of training and the other for the purpose of testing. Then using common preprocessing methods, the tweets were preprocessed into a list of usable words. Then using the ‘natural language toolkit’ in python the lists of words were vectorized.
Then the vectorized tweets were trained with Na​ïve Bayes classifiers into two categories of positive or negative. After the model was trained, the test set was tested to analyze their positivity or negativity. The accuracy gave me a result of 78.6% accuracy. Also to note, the percentage of false positives were higher than the true negative.
To discuss this issue further, if we look at the data, the number of positive tweets labeled by me outnumber the number of negative tweets. As a result, the model has a lot less negative tweets to analyze and train. This leads to a low accuracy when you give a negative tweet to the model. But on the other hand, if the model identifies a tweet as negative, we can be a lot more certain that the tweet is negative since the false negatives are much lower. But compared to the limited data that I manually labeled, the result was satisfactory. If I had labeled more than thousands tweets with an equal distribution of negative and positive tweets, the accuracy was set to be much higher.
Timewise, I spent about half of the project time on scraping the 260 tweets, manually labeling each one, and researching on how to preprocess them (learn how to use ‘re’ library). Then most of the remaining time was spent on studying the algorithms for sentiment analysis and choosing ​Na​ïve Bayes, learning how to work with ‘nltk’ library, research vectorization of tweets, and writing the script to train and test the model. The rest of the time was spent on analyzing the results and comparing them to the tweets which I labeled.

## References
[1] “Python Regex Tutorial - A Complete Beginners Guide: ML+.” ​Machine Learning Plus,​ 19 June 2018, www.machinelearningplus.com/python/python-regex-tutorial-examples/.

[2] Go, Alec, et al. ​Twitter Sentiment Classification Using Distant Supervision​. cs.stanford.edu/people/alecmgo/papers/TwitterDistantSupervision09.pdf.

[3] Wahome, Ronald. “This Is How Twitter Sees The World : Sentiment Analysis Part One.” ​Medium​, Towards Data Science, 8 Sept. 2018, towardsdatascience.com/the-real-world-as-seen-on-twitter-sentiment-analysis-part-one-5ac2d06b63fb.