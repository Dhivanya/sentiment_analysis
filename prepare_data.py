import pandas as pd

df = pd.read_csv('Reviews.csv')

print(f"Total reviews: {len(df)}")

# Convert to 2-class: drop neutral (3-star), keep only clear positive/negative
def get_sentiment(score):
    if score <= 2:
        return 'Negative'
    elif score >= 4:
        return 'Positive'
    else:
        return None  # drop 3-star (ambiguous)

df['sentiment'] = df['Score'].apply(get_sentiment)
df_clean = df[['Text', 'sentiment']].dropna()
df_clean.columns = ['review', 'sentiment']

print("\n=== BEFORE BALANCING ===")
print(df_clean['sentiment'].value_counts())

# Balance classes
min_count = df_clean['sentiment'].value_counts().min()
sample_size = min(min_count, 4000)

balanced_df = df_clean.groupby('sentiment').apply(
    lambda x: x.sample(n=sample_size, random_state=42)
).reset_index(drop=True)

balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

print("\n=== BALANCED (2-CLASS) ===")
print(balanced_df['sentiment'].value_counts())

balanced_df.to_csv('processed_reviews.csv', index=False)
print("\n✅ 2-class real dataset saved!")