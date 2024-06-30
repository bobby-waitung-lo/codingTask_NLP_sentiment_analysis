# Import libraries
import pandas as pd
import spacy

from spacytextblob.spacytextblob import SpacyTextBlob


# Import the dataset
dataframe = pd.read_csv('amazon_product_reviews.csv')

# Preprocess the dataset
# Select therelavent reviews
reviews_data = dataframe['reviews.text']

# Remove all missing values
clean_data = reviews_data.dropna()

# load the spaCy model
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("spacytextblob")


# Create a function for sentiment analysis
# This function takes product review as input and predicts its sentiment
def sentiment_analysis(product_review):
    
    # Filter out stop words by using the `token.is_stop` attribute
    def remove_stops(doc):
        return [token.orth_ for token in doc if not token.is_stop]
    
    # Create SpaCy documents by joining the words into a string
    def to_doc(words):
        return nlp(' '.join(words))
    
    # Take the `token.lemma_` of each non-stop word
    def lemmatize(doc):
        return [token.lemma_ for token in doc if not token.is_stop]
    
    
    # Create a list to store preprocessed reviews
    lemmatize_review = []
    for review in product_review:
        
        # apply removing stop words to all
        remove_stops_review = remove_stops(nlp(review))
        print
    
        # apply lemmatization to all
        lemmatize_review.append(lemmatize(to_doc(remove_stops_review)))
    
    
    # Create a list for sentiment analysis results
    sentiment_list = []
    for review in lemmatize_review:
    
        # Using the polarity attribute for sentiment analysis
        polarity = to_doc(review)._.blob.polarity
    
        # Sentiment classification
        if polarity >= 1/3:
            sentiment = "positive"
        elif polarity >= -1/3:
            sentiment = "neutral"
        else:
            sentiment = "negative"
        
        # Save the sentiment in a list    
        sentiment_list.append(sentiment)
    
    
    # Create the result dataframe
    product_review_df = product_review.to_frame()
    sentiment_df = pd.DataFrame({"sentiment":sentiment_list}, index =product_review_df.index)
    analysis_result_df = product_review_df.join(sentiment_df)
    
    # Return the result dataframe
    return analysis_result_df


# Model testing
# Choose sample review for testing
sample_review = clean_data[2206:2209]

# Run the model and 
testing_result = sentiment_analysis(sample_review)

# Display sample reviews
print("Sample reviews\n")

# Obtain prediction result
for i in range(len(testing_result)):
    print(f"Review {testing_result.index[i]}:\n{testing_result.iat[i,0]}\nSentiment: {testing_result.iat[i,1]}\n")