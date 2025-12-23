# File: analysis.py
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a text string.
    
    Args:
        text (str): Input text.
        
    Returns:
        dict: Contains 'compound', 'pos', 'neg', 'neu' scores.
        str: The label (Positive, Negative, Neutral).
    """
    sid = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    scores = sid.polarity_scores(text)
    compound_score = scores['compound']
    
    # Determine Label based on Compound score
    if compound_score >= 0.05:
        label = "Positive"
    elif compound_score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
        
    return scores, label