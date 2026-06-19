import pandas as pd
import random

positive_reviews = [
    "This product is amazing and works perfectly",
    "Excellent quality and fast delivery",
    "Best purchase I have ever made",
    "Highly recommend this to everyone",
    "Outstanding performance and great value",
    "Love this product completely satisfied",
    "Perfect product exactly as described",
    "Great quality exceeded my expectations",
    "Wonderful product very happy with purchase",
    "Superb quality and excellent customer service",
    "Fantastic product works like a charm",
    "Very happy with this purchase",
    "Great product will buy again",
    "Absolutely love it best product ever",
    "Brilliant product highly satisfied",
    "Amazing quality worth every penny",
    "Excellent product very impressed",
    "Perfect exactly what I needed",
    "Very good product recommended",
    "Outstanding quality fast shipping"
]

negative_reviews = [
    "Terrible product complete waste of money",
    "Very disappointed with this purchase",
    "Worst product I have ever bought",
    "Broken on arrival very upset",
    "Poor quality not worth the price",
    "Completely useless product avoid buying",
    "Very bad experience terrible quality",
    "Do not buy this product horrible",
    "Waste of money poor performance",
    "Extremely disappointed very poor quality",
    "Product stopped working after one day",
    "Total disappointment not recommended",
    "Bad product bad customer service",
    "Horrible experience will not buy again",
    "Very poor quality broke immediately",
    "Worst purchase ever money wasted",
    "Defective product very unhappy",
    "Not as described complete fraud",
    "Poor build quality very fragile",
    "Terrible experience avoid this product"
]

neutral_reviews = [
    "Product is okay nothing special",
    "Average quality for the price",
    "Decent product does the job",
    "Neither good nor bad just okay",
    "Works as expected nothing more",
    "Acceptable quality average performance",
    "Not bad but not great either",
    "Mediocre product average experience",
    "Okay product could be better",
    "Average product meets basic needs",
    "Fine product nothing extraordinary",
    "Satisfactory quality average product",
    "Product works but nothing special",
    "Reasonable quality for the cost",
    "Basic product does what it should",
    "Okay experience not impressed not disappointed",
    "Product is fine average quality",
    "Meets expectations nothing more nothing less",
    "Decent enough for the price paid",
    "Average product standard quality"
]

reviews = []
labels = []

for _ in range(500):
    reviews.append(random.choice(positive_reviews))
    labels.append('Positive')
    reviews.append(random.choice(negative_reviews))
    labels.append('Negative')
    reviews.append(random.choice(neutral_reviews))
    labels.append('Neutral')

df = pd.DataFrame({'review': reviews, 'sentiment': labels})
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('reviews.csv', index=False)
print(f"Dataset created! Total reviews: {len(df)}")
print(df['sentiment'].value_counts())