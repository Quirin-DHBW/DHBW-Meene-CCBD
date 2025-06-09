import duckdb
import pandas as pd
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys, os

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

os.chdir(os.path.dirname(sys.argv[0]))

def normalize_word(word):
    word = word.lower()
    word = re.sub(r'\W+', '', word)
    if word in stop_words or len(word) < 3:
        return None
    lemma = lemmatizer.lemmatize(word)
    synsets = wordnet.synsets(lemma)
    if synsets:
        canonical = synsets[0].lemmas()[0].name().lower()
        return canonical
    return lemma

if __name__ == "__main__":
    con = duckdb.connect("bsky_posts.db")
    df = con.execute("SELECT timestamp, text FROM posts").fetchdf()
    con.close()

    stop_words = set(stopwords.words('german') + stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # --- Word Frequency Analysis ---
    all_words = []
    for text in df["text"]:
        tokens = word_tokenize(text.lower())
        for token in tokens:
            norm = normalize_word(token)
            if norm:
                all_words.append(norm)

    counter = Counter(all_words)
    top_words = counter.most_common(30)
    freq_df = pd.DataFrame(top_words, columns=["word", "count"])
    fig = px.bar(freq_df, x="word", y="count", color="word", title="Top 30 häufige Begriffe (mit Synonymgruppen)")
    fig.show()

    # --- Post Frequency Per Day ---
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    post_counts = df.groupby('date').size().reset_index(name='post_count')
    fig = px.line(post_counts, x="date", y="post_count", title="Posts per Day")
    fig.show()

    # --- Scaling by Post Frequency Per Day ---
    highest_post_per_day = post_counts.max()["post_count"]
    print(highest_post_per_day)
    scaling_factors_per_day = post_counts.set_index('date')['post_count'] / highest_post_per_day
    print(scaling_factors_per_day)

    # --- Sentiment Analysis ---
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    sentiment_daily = df.groupby('date')['sentiment'].mean().reset_index()

    sentiment_daily["scaled sentiment"] = sentiment_daily['sentiment'] * scaling_factors_per_day.values

    # --- Visualization ---
    fig = go.Figure()
    fig.add_trace(go.Bar(x=sentiment_daily['date'], 
                         y=sentiment_daily['sentiment'],
                         name='Average Sentiment',
                         marker_color=["#002900" if val > 0 else "red" for val in sentiment_daily['sentiment']]))
    
    fig.add_trace(go.Bar(x=sentiment_daily['date'], 
                         y=sentiment_daily['scaled sentiment'],
                         name='Average Sentiment Scaled by Post Frequency',
                         marker_color=["#002900" if val > 0 else "red" for val in sentiment_daily['sentiment']]))
    
    fig.add_trace(go.Scatter(x=df['date'],
                            y=df['sentiment'],
                            mode='markers',
                            name='Daily Sentiment Per Post',
                            marker=dict(color='rgba(0, 0, 255, 0.5)', size=5)))

    fig.update_layout(
        title="Sentiment Over Time",
        xaxis=dict(title='Date'),
        yaxis=dict(title='Average Sentiment', side='left'),
    )

    fig.show()

