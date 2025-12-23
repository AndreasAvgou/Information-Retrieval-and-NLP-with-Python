# File: visualizer.py
import matplotlib.pyplot as plt

def generate_report(results):
    """
    Generates a visual report of the sentiment analysis.
    
    Args:
        results (list): List of labels (Positive, Negative, Neutral).
    """
    print("\n--- Generating Sentiment Report ---")
    
    # Count frequencies
    counts = {
        "Positive": results.count("Positive"),
        "Negative": results.count("Negative"),
        "Neutral": results.count("Neutral")
    }
    
    # Print Summary
    print("Summary:")
    for label, count in counts.items():
        print(f" - {label}: {count}")
        
    # Plot Pie Chart
    labels = counts.keys()
    sizes = counts.values()
    colors = ['#66b3ff', '#ff9999', '#99ff99'] # Blue, Red, Green
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Real-Time Sentiment Analysis Distribution')
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()