import streamlit as st
import pickle
import matplotlib.pyplot as plt
from datetime import datetime

# Load model
model = pickle.load(open('sentiment_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="SentiFeed",
    page_icon="💬",
    layout="wide"
)

# CSS — Social Media Style
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    
    .app-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
    }
    
    .post-box {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    
    .feed-card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        border-left: 4px solid #ddd;
    }
    
    .feed-card-positive {
        border-left: 4px solid #2ecc71;
    }
    
    .feed-card-negative {
        border-left: 4px solid #e74c3c;
    }
    
    .user-tag {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 3px 12px;
        border-radius: 15px;
        font-size: 0.8em;
        margin-bottom: 8px;
    }
    
    .sentiment-pill {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.85em;
    }
    
    .pill-positive {
        background: #d5f5e3;
        color: #1e8449;
    }
    
    .pill-negative {
        background: #fadbd8;
        color: #c0392b;
    }
    
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="app-header">
    <h1 style="margin:0;">💬 SentiFeed</h1>
    <p style="margin:5px 0 0 0; opacity:0.9;">
        AI-Powered Customer Sentiment Analyzer
    </p>
</div>
""", unsafe_allow_html=True)

# Session state
if 'feed' not in st.session_state:
    st.session_state.feed = []

def predict_sentiment(text):
    vec = tfidf.transform([text])
    prediction = model.predict(vec)[0]
    confidence = model.predict_proba(vec).max()
    probs = model.predict_proba(vec)[0]
    labels = model.classes_
    return prediction, confidence, labels, probs

# Layout
col1, col2 = st.columns([1.3, 1])

with col1:
    # Post composer
    st.markdown('<div class="post-box">', unsafe_allow_html=True)
    st.markdown("**✍️ What's the review saying?**")

    post_input = st.text_area(
        "",
        placeholder="Paste a customer review here...",
        height=100,
        label_visibility="collapsed"
    )

    ex_cols = st.columns(2)
    examples = {
        "😊 Try Positive": "This product is amazing and exceeded my expectations!",
        "😠 Try Negative": "Terrible quality, complete waste of money"
    }
    for i, (label, txt) in enumerate(examples.items()):
        with ex_cols[i]:
            if st.button(label, use_container_width=True, key=f"ex{i}"):
                st.session_state.temp_input = txt

    post_btn = st.button("🚀 Post & Analyze", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    final_input = st.session_state.get('temp_input', '') if not post_input else post_input

    if post_btn and final_input:
        prediction, confidence, labels, probs = predict_sentiment(final_input)

        st.session_state.feed.insert(0, {
            'text': final_input,
            'sentiment': prediction,
            'confidence': confidence,
            'time': datetime.now().strftime("%I:%M %p")
        })
        st.session_state.temp_input = ''

    elif post_btn and not final_input:
        st.warning("Write something first!")

    # Feed
    st.markdown("### 📰 Analysis Feed")
    if st.session_state.feed:
        for post in st.session_state.feed:
            sentiment = post['sentiment']
            if sentiment == 'Positive':
                card_class = "feed-card-positive"
                pill_class = "pill-positive"
                emoji = "😊"
            else:
                card_class = "feed-card-negative"
                pill_class = "pill-negative"
                emoji = "😠"

            st.markdown(f"""
            <div class="feed-card {card_class}">
                <span class="user-tag">👤 Customer Review</span>
                <span style="float:right; color:#999; font-size:0.8em;">{post['time']}</span>
                <p style="margin:10px 0; color:#333;">{post['text']}</p>
                <span class="sentiment-pill {pill_class}">
                    {emoji} {sentiment} · {post['confidence']:.0%} confident
                </span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No posts analyzed yet. Write a review above to get started!")

with col2:
    # Live stats
    st.markdown("### 📊 Feed Stats")
    
    total = len(st.session_state.feed)
    pos = sum(1 for p in st.session_state.feed if p['sentiment'] == 'Positive')
    neg = sum(1 for p in st.session_state.feed if p['sentiment'] == 'Negative')

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(f"""
        <div class="stat-card">
            <h2 style="color:#667eea; margin:0;">{total}</h2>
            <p style="color:#888; margin:0;">Total Posts</p>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown(f"""
        <div class="stat-card">
            <h2 style="color:#2ecc71; margin:0;">{pos}</h2>
            <p style="color:#888; margin:0;">😊 Positive</p>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown(f"""
        <div class="stat-card">
            <h2 style="color:#e74c3c; margin:0;">{neg}</h2>
            <p style="color:#888; margin:0;">😠 Negative</p>
        </div>
        """, unsafe_allow_html=True)

    # Chart for last analysis
    if st.session_state.feed:
        st.markdown("---")
        st.markdown("### 📈 Last Post Breakdown")
        last_post = st.session_state.feed[0]
        _, _, labels, probs = predict_sentiment(last_post['text'])
        
        colors_chart = ['#e74c3c', '#2ecc71']
        fig, ax = plt.subplots(figsize=(5, 2.5))
        bars = ax.barh(labels, probs * 100, color=colors_chart)
        ax.set_xlim(0, 100)
        for bar, prob in zip(bars, probs):
            ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                    f'{prob:.0%}', va='center', fontsize=9)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)

    st.markdown("---")
    st.markdown("### 📈 Model Performance")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Accuracy", "85.3%")
    with m2:
        st.metric("Classes", "2")
    with m3:
        st.metric("Reviews", "8000+")

    st.markdown("---")
    st.markdown("### ℹ️ About SentiFeed")
    st.markdown("""
    Real-time AI sentiment analysis on real 
    Amazon customer reviews.
    
    **Tech Stack:**
    Python · TF-IDF · Logistic Regression · Streamlit
    
    **Dataset:** Amazon Fine Food Reviews (Kaggle)
    
    **Sentiment Classes:**
    - 😊 Positive
    - 😠 Negative
    """)

st.markdown("---")
st.caption("💬 SentiFeed | AI Sentiment Analysis on Real Amazon Reviews | Powered by Machine Learning")