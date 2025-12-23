# File: analytics.py
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

def analyze_and_plot_frequency(words, top_n=10):
    """
    Calculates word frequency (removing stopwords/punctuation) and plots the top N words.
    
    Args:
        words (list): List of all tokens.
        top_n (int): Number of top words to display.
    """
    # Get standard stopwords (like 'the', 'is', 'at') and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    
    # Filter list: remove stopwords, punctuation, and convert to lowercase
    filtered_words = [
        w.lower() for w in words 
        if w.lower() not in stop_words and w not in punctuation and w.isalnum()
    ]
    
    # Calculate Frequency Distribution
    fdist = FreqDist(filtered_words)
    
    print(f"\n[Info] Top {top_n} most frequent words:")
    for word, frequency in fdist.most_common(top_n):
        print(f" - {word}: {frequency}")
    
    # Visualization using Matplotlib
    plt.figure(figsize=(10, 6))
    fdist.plot(top_n, title=f"Top {top_n} Most Frequent Words (excluding stopwords)")
    plt.show()