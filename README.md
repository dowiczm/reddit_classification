## Executive Summary
This research was designed around classification. The best classification model created had a testing score of 0.797. This implies that the model is relatively strong and did a good job at determining which post a subreddit came from. Since the model was strong with its predictions, my conclusion showed that the subreddits were indeed different, and should remain as such, rather than merging into one. 


## Problem Statement

Is it necessary to have two different subreddits for both rants and unpopular-opinions? As an avid Reddit user, I’ve noticed that these two subreddits produce many of the same types of posts. My goal is to produce a classification model designed to predict which subreddit a post came from. The strength of this model will determine if the above subreddits should remain separate, or consider a merge. 

 
 ### Background Info

Reddit describes itself as "the front page of the internet". However, I would describe it as a collection of thoughts and ideas from people across the world. These thoughts and ideas are displayed on Reddit as 'posts'. My research will use posts from two different subreddits ('rant' and 'unpopularopinion') to determine if their contents are the same, or if they can be classified separately by a model I create. If the model is able to accurately classify both subreddits, they should remain separate, otherwise, they are in essence the same and should be considered as such.  


### Data Description 

The data used to analyze these two classes ('rant' and 'unpopularopinion') was gathered using the Pushshift's API (https://github.com/pushshift/api). A Python script was used to grab 100 posts from both subreddits every 10 seconds, to follow Pushshift's rules. 15,000 posts from each subreddit was gathered. 

* [`rant_unpopularopinions.csv`](./datasets/stemlem.csv): Raw Data


### Data Dictionary

|Feature|Type|Description|


|title|object|text introducing the post|
|created_utc|int|unique number used to identify individual posts|
|self_text|object|post content|
|subreddit|object|identifies which subreddit the post is from|
|author|object|post's creator|
|permalink|object|tail-end of url, can be used to access the post online|
|all_text|object|'title' and 'self_text' combined|
|total_word_count|int|total number of words in 'all_text'|
|lem|object|'all_text' with each word lemmatized|


### EDA Results

- Classes are relatively balanced (52% from 'rant', 48% from 'unpopularopinions')

- On average, rants posts are longer by ~70 words

- After performing sentiment analysis on both subreddits, 'rant' posts more than not had a negative sentiment, while 'unpopularopinion' had a much more even distribution of sentiment (half positive, half negative). This points towards the subreddits beinig different with regard to sentiment. Sentiment also polarized towards -1 or 1 as the length of the post increased.

- Many of the same frquent words appear in both subreddits. However, 'rant' had far more negative words and curse words.


### Modeling 

- Many many models were created and tested to classify the respective subreddits. In the end, the two most successful models were:
    - Logistic-Regession model that used a CountVectorizer on the 'lem' column. The CountVectorizer utilized the following     parameters: stop_words = 'english', max_features = 2500, min_df = 2, max_df = 0.9, ngram_range = (1,2). 
        - These paramters were determined by performing multiple grid-searches on different values for the above parameters. This model scored 0.832 on the training data and 0.797 on the testing data. This would imply slight overfitting in the model, but overall it performed quite well.
    
    - Random-Forest-Classifier model that used a CountVectorizer on the 'lem' column. The CountVectorizer utilized the following parameters: max_df = 0.95, max_features = 1000, min_df = 3, ngram_range = (1,1). The RandomForestClassifier utilized: n_estimators = 500 and max_depth = 10.
        - These parameters were determined by using a grid search over multiple paramters for both the RandomForestClassifier as well as the CountVectorizer. This model scored 0.842 on the training data, and 0.781 on the testing data.

- Both models performed almost equally, however I decided that my best model was the LogisticRegression Classifier using a CountVectorizer, as the testing score was marginally higher, and the coefficents were somewhat interpretable. The coefficients of the LogisticRegression model provided insights as to what was important to each class, and what words were used in determining each class.

### Conclusions

Both subreddits are distinct, and should be considered as such. 

After using my model to make predictions, the accuracy of each class was equal. This means that the model is able to determine which subreddit a post came from equally across the board, and therefore, the subreddits are in-essence different from one another. My original hypothesis that the two subreddits are similar and should consider merging was false, as the model was relatively good at determining whether a post was from 'rant' or 'unpopularopinions'. 

The coefficents of the best model (LogReg with CountVec) show all the words correlated with 'rant'. These words are mostly of negative sentiment. A few of them are curse words, while others are words associated with hate and controversy. The word 'rant' also appears to be a determining factor, which is not surprising.  The words seen with determining the 'unpopularopinion' class are all associated with an opinion, such as: (gross, cringe, overrated, better, best, and prefer).

After reviewing these words and their respective coefficents, it is clear that the subreddits are indeed different and should not consider a merge. 
