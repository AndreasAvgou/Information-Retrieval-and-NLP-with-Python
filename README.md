# Information Retrieval & NLP with Python

This repository contains a collection of five Python projects focused on Information Retrieval (IR), Natural Language Processing (NLP), and Machine Learning.

Each project follows a **Modular Programming** architecture, splitting logic into distinct files for better maintainability and readability.


## Repository Structure

To run these projects without conflicts, organize your folders as follows:

```text
├── 1_NLTK/          # Text Processing & Analysis
├── 2_SearchEngine/  # Simple Inverted Index Search
├── 3_Clustering/    # K-Means Document Clustering
├── 4_Sentiment/     # Real-Time Sentiment Analysis
└── 5_Recommender/   # ML-Based Recommendation System
```

## Prerequisites & Installation

All projects require **Python 3.x**. You can install all necessary dependencies for the entire suite using the following command:

```bash
pip install nltk matplotlib pandas numpy scipy scikit-learn
```

## Project Summaries

### 1️⃣ Project 1: Text Processing and Analysis with NLTK
**Objective:** Learn the basics of NLP including tokenization, POS tagging, and Named Entity Recognition (NER).

* **Key Modules:**
    * `preprocessing.py`: Splits text into sentences and tokens.
    * `tagging.py`: Identifies parts of speech (Nouns, Verbs, etc.).
    * `entities.py`: Extracts names of People, Organizations, and Locations.
    * `analytics.py`: Plots word frequency distributions.

**How to Run:**
```bash
cd Project1_NLTK
python main.py
```

### 2️⃣ Project 2: Building a Simple Search Engine
**Objective:** Understand the fundamental concepts of search engines: Indexing and Ranking.

* **Key Modules:**
    * `indexing.py`: Builds an **Inverted Index** mapping words to documents.
    * `ranking.py`: Implements a scoring algorithm (Term Frequency) to rank results.
    * `search.py`: Handles user queries.

**How to Run:**
```bash
cd Project2_SearchEngine
python main.py
```

### 3️⃣ Project 3: Document Clustering
**Objective:** Group similar documents together using Unsupervised Machine Learning.

* **Key Modules:**
    * `preprocessing.py`: Converts text to numbers using **TF-IDF Vectorization**.
    * `clustering.py`: Applies the **K-Means** algorithm.
    * `visualizer.py`: Uses **PCA** to reduce dimensions and plot clusters in 2D.

**How to Run:**
```bash
cd Project3_Clustering
python main.py
```

### 4️⃣ Project 4: Real-Time Sentiment Analysis
**Objective:** Analyze a stream of social media messages to determine if they are Positive, Negative, or Neutral.

* **Key Modules:**
    * `data_stream.py`: Simulates a live feed of user comments.
    * `analysis.py`: Uses **NLTK VADER** to calculate sentiment scores.
    * `visualizer.py`: Generates a pie chart summary of the session.

**How to Run:**
```bash
cd Project4_Sentiment
python main.py
```

### 5️⃣ Project 5: Machine Learning-Based Recommendation System
**Objective:** Build a system that suggests items (movies/products) to users based on their past interactions using Collaborative Filtering.

* **Key Modules:**
    * `data_generator.py`: Creates a synthetic User-Item rating dataset.
    * `model.py`: Trains a **Singular Value Decomposition (SVD)** model.
    * `evaluation.py`: Calculates RMSE and generates personalized recommendations.

**How to Run:**
```bash
cd Project5_Recommender
python main.py
```

## Technical Details

All projects follow this execution flow:

1.  **Config/Setup:** Load settings or download resources.
2.  **Data Ingestion:** Load text or simulate data.
3.  **Preprocessing:** Clean and format data (Tokenization, Vectorization, Matrix creation).
4.  **Core Logic:** Run the Algorithm (Indexing, Clustering, SVD, etc.).
5.  **Output:** Display results via console or Matplotlib charts.
