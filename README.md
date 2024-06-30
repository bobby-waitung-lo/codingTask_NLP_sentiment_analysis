# NLP_sentiment_analysis

This is a Natural Language Processing coding task about a sentiment analysis on consumer reviews of Amazon product using SpaCy library

The dataset is store in the file amazon_product_reviews.csv in amazon_product_reviews.zip

The program is stored in sentiment_analysis.py

Please download amazon_product_reviews.csv and sentiment_analysis.py in the same directry.

Then, run the program sentiment_analysis.py

1. A description of the dataset used

The dataset used is a list of over 34,000 consumer reviews for Amazon products like
the Kindle, Fire TV Stick, and more provided by Datafiniti's Product Database. The
dataset includes basic product information, rating, review text, and more for each
product.

The ‘reviews.text’ column is selected as the feature and then the missing data in the
feature is removed. The ‘clean_data’ variable stores the preprocessed data as the
input of the sentiment analysis model.


2. Details of the preprocessing steps

First, each review of the input data is tokenized into words by token.orth_ attribute
and the stopwords are filtered in each review by the token.is_stop attribute in the
spacy library.

Then, each word in each stopword removal review is lemmatized its base form by
the token.lemma_ attribute.

After that, blob.polarity attribute in the spacytextblob library is used to measure the
strength of the sentiment in each review. A polarity score between -1 and 1 will be
assigned to indicate a sentiment from very negative to very positive.

Next, the polarity score is classified into 3 sentiment categories “positive”, “neutral”
and “negative” based on the if-else condition statements.

Finally, the sentiment output is stored at the new column next to each review in the
‘clean_data’ dataframe.


3. Evaluation of results

Below are the analysis results of the sentiment analysis model from the chosen
review 2206, 2207 and 2208:

Review 2206:

Nice tab and worth for its money..got this from best buy during thanks giving and
gifted to my friend...

Sentiment: positive

Review 2207:

Hard to use, No way to delete things from screen. Need better manual. most books
are impossible if they are reference books.

Sentiment: negative

Review 2208:

Bought for our son so he wouldn't have to carry books back from his deployment

Sentiment: neutral

Evaluation:

The review 2206 contains the positive words like 'nice', 'worth' and 'best’ and the
overall sentiment of the appreciative feedback is positive which matches with the
analysis result of the model.

The review 2207 contains the negative words like 'hard' and 'impossible', and the
overall sentiment of the complaint comment is negative which matches with the
analysis result of the model.

The review 2208 is a neutral descriptive sentence telling the reason for purchasing
the product which matches with the analysis result of the model.
To summarize, based on the selected sample reviews, the model performs well in
sentiment analysis.


4. Insights into the model's strengths and limitations

There are a few strengths of the spaCy NLP model for sentiment analysis.

First, it is easy to use. The import of spaCy NLP library is straightforward and can be
used directly.

Second, the spaCy NLP model is efficient. The tokenization and lemmatization
algorithm can handle complex sentences with punctuations with ease.

Third, the spaCy NLP model has accurate sentiment analysis tools, such as
blob.polarity, which can get a rough score of the sentiment of sentences.

Limitations:

However, it also has a few limitations.
First, spaCy library has less flexibility than other NLP libraries, such as NLTK, on
customization and fine tuning of pre-trained models.

Second, spaCy library supports fewer languages than some other libraries like
NLTK1. A different library may be needed if a specific language is not supported by
spaCy.

Third, spaCy is designed to train NLP models on GPU. Although CPU-optimized
pipelines are supported, less accurate results may be obtained.

This is the program out put:
![program output](https://github.com/lwtb7801/codingTask_NLP_sentiment_analysis/assets/163464647/3cae59f5-3a29-46cd-8902-54be97732ca4)


Credits 

Author: Bobby
