# File: data_stream.py
import time
import random

# Simulated stream of tweets/comments
SIMULATED_DATA = [
    "I absolutely love this new phone! The camera is amazing.",
    "The service was terrible. I will never come back here.",
    "Just had a normal day, nothing special happened.",
    "OMG! I can't believe I won the lottery! #excited",
    "This movie was okay, but the ending was a bit boring.",
    "Worst experience ever. Do not buy this product!",
    "Happy birthday to my best friend! Love you!",
    "I'm feeling a bit sad today because of the rain.",
    "The new update is buggy and crashes constantly.",
    "Great job team! We crushed the goals this quarter."
]

def get_realtime_data_stream(limit=10):
    """
    Yields data one by one to simulate a real-time stream.
    
    Args:
        limit (int): How many items to stream.
        
    Yields:
        str: A single text message.
    """
    print(f"--- Starting Data Stream (Limit: {limit}) ---")
    for i in range(limit):
        # Pick a random message
        text = random.choice(SIMULATED_DATA)
        
        # Simulate network delay (0.5 to 1.5 seconds)
        time.sleep(random.uniform(0.5, 1.5))
        
        yield text