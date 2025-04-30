import duckdb
import pandas as pd
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from collections import Counter
import plotly.express as px
import sys, os
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

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
    df = con.execute("SELECT text FROM posts").fetchdf()
    con.close()

    stop_words = set(stopwords.words('german') + stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

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

    fig = px.bar(freq_df, x="word", y="count", title="Top 30 häufige Begriffe (mit Synonymgruppen)")
    fig.show()
