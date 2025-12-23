# File: main.py
import setup_nltk
import data_stream
import preprocessing
import analysis
import visualizer

def main():
    print("=== Project 4: Real-Time Sentiment Analysis ===\n")
    
    # Step 0: Setup
    setup_nltk.download_vader_lexicon()
    
    # List to store results for visualization
    sentiment_history = []
    
    # Step 1: Start Data Stream
    stream = data_stream.get_realtime_data_stream(limit=10)
    
    print("\n--- Processing Live Feed ---")
    
    for raw_text in stream:
        # Step 2: Clean
        clean_text = preprocessing.clean_text(raw_text)
        
        # Step 3: Analyze
        scores, label = analysis.analyze_sentiment(clean_text)
        
        # Store result
        sentiment_history.append(label)
        
        # Live Output
        print(f"Msg: \"{clean_text}\"")
        print(f" -> Label: {label} (Score: {scores['compound']:.2f})")
        print("-" * 30)
        
    # Step 4: Visualize
    visualizer.generate_report(sentiment_history)
    
    print("\n=== Execution Finished ===")

if __name__ == "__main__":
    main()