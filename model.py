import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import re

# Load data
df = pd.read_csv('processed_reviews.csv')

# Clean text function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Mark words after "not"/"no" with NOT_ prefix
    words = text.split()
    result = []
    negate = False
    for word in words:
        if word in ['not', 'no', 'never']:
            negate = True
            result.append(word)
        elif negate:
            result.append('not_' + word)
            negate = False
        else:
            result.append(word)
    
    text = ' '.join(result)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['review'] = df['review'].apply(clean_text)

X = df['review']
y = df['sentiment']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Improved TF-IDF
tfidf = TfidfVectorizer(
    max_features=10000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9,
    sublinear_tf=True,
    stop_words='english'
)
X_train_tf = tfidf.fit_transform(X_train)
X_test_tf = tfidf.transform(X_test)

# Train (no class_weight this time)
model = LogisticRegression(max_iter=2000, C=5)
model.fit(X_train_tf, y_train)

# Evaluate
preds = model.predict(X_test_tf)
accuracy = accuracy_score(y_test, preds)
print(f"✅ Accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, preds))

# Save
pickle.dump(model, open('sentiment_model.pkl', 'wb'))
pickle.dump(tfidf, open('tfidf.pkl', 'wb'))
print("\n✅ Model saved!")