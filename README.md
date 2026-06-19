# 💬 SentiFeed — Customer Sentiment Analyzer

An AI-powered web application that analyzes real Amazon customer 
reviews and classifies them as Positive or Negative sentiment, 
styled as a social media feed.

## 🔗 Live Demo
👉 [Click here to try the app](https://sentimentanalysis-iyurfkzycipcnqfexuhcq9.streamlit.app)

## 📌 Project Overview
Businesses receive thousands of customer reviews daily. This system 
automatically classifies review sentiment in real-time using real 
Amazon Fine Food Reviews data, helping identify unhappy customers 
and prioritize support.

## 📊 Model Performance
| Metric | Value |
|--------|-------|
| Accuracy | 87% |
| Sentiment Classes | 2 (Positive, Negative) |
| Training Data | 8,000 real Amazon reviews |
| Dataset Source | Amazon Fine Food Reviews (Kaggle) |

## 🛠️ Tech Stack
- **Language:** Python
- **ML Model:** Logistic Regression
- **Text Processing:** TF-IDF Vectorization with negation handling
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib
- **Web App:** Streamlit

## 🚀 Features
- ✍️ Real-time review analysis with social-feed style posting
- 📊 Confidence score visualization
- 📈 Live feed statistics
- 🎨 Color-coded sentiment pills

## ⚙️ Key Technical Decisions
- Used **real Amazon Fine Food Reviews** instead of synthetic data 
  for authentic results
- Implemented **negation handling** (e.g., "not good") which 
  improved accuracy from 85.3% to 87%
- Balanced dataset (4000 positive + 4000 negative) to avoid bias

## ⚙️ How to Run Locally
```bash
git clone https://github.com/Dhivanya/sentiment_analysis.git
cd sentiment_analysis
pip install -r requirements.txt
python model.py
streamlit run app.py
```

## 🌍 Real World Applications
- E-commerce review monitoring
- Customer support prioritization
- Brand sentiment tracking

## ⚠️ Known Limitations
TF-IDF based models can struggle with complex negation and sarcasm 
since they don't capture full context like deep learning models 
(BERT) do. This was partially addressed using a custom negation 
preprocessing step.
