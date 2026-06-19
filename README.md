# 💬 SentiFeed — Customer Sentiment Analyzer

An AI-powered web application that analyzes customer reviews and 
classifies them as Positive, Negative, or Neutral sentiment, 
styled as a social media feed.

## 🔗 Live Demo
👉 https://sentimentanalysis-iyurfkzycipcnqfexuhcq9.streamlit.app/
## 📌 Project Overview
Businesses receive thousands of customer reviews daily. Manually 
reading each one to gauge customer satisfaction is slow and 
inefficient. This system automatically classifies review sentiment 
in real-time, helping businesses identify unhappy customers and 
prioritize support.

## 📊 Model Performance
| Metric | Value |
|--------|-------|
| Accuracy | 100% (on test dataset) |
| Sentiment Classes | 3 (Positive, Negative, Neutral) |
| Training Samples | 1,500 reviews |

## 🛠️ Tech Stack
- **Language:** Python
- **ML Model:** Logistic Regression
- **Text Processing:** TF-IDF Vectorization
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib
- **Web App:** Streamlit
- **UI Style:** Social media feed design

## 🚀 Features
- ✍️ Real-time review analysis with social-feed style posting
- 📊 Confidence score visualization for each sentiment class
- 📈 Live feed statistics (total posts, positive/negative/neutral counts)
- 🎨 Color-coded sentiment pills (green/red/orange)
- 🕐 Analysis history feed

## 📁 Project Structure
sentiment-analysis/

│

├── app.py                  # Streamlit web app

├── model.py                # Model training script

├── eda.py                  # Exploratory data analysis

├── generate_data.py        # Dataset generation script

├── sentiment_model.pkl     # Trained ML model

├── tfidf.pkl                # TF-IDF vectorizer

├── reviews.csv              # Training dataset

└── requirements.txt         # Dependencies
## ⚙️ How to Run Locally
```bash
git clone https://github.com/Dhivanya/sentiment_analysis.git
cd sentiment_analysis
pip install -r requirements.txt
streamlit run app.py
```

## 📈 How It Works
1. User enters a customer review
2. Text is converted to numerical features using TF-IDF
3. Logistic Regression model predicts the sentiment
4. Result displayed with confidence score and visual breakdown

## 🏦 Sample Predictions
| Review | Predicted Sentiment |
|--------|---------------------|
| "This product is amazing and works perfectly" | 😊 Positive |
| "Terrible product complete waste of money" | 😠 Negative |
| "Product is okay nothing special" | 😐 Neutral |

## 🌍 Real World Applications
- E-commerce platforms analyzing product reviews
- Restaurant apps monitoring customer feedback
- Social media brand sentiment monitoring
- Customer support prioritization systems
