# Step 1: Install and Import Libraries
import streamlit as st
from textblob import TextBlob
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title='Sentiment Analyzer')

def typewriter(text: str, speed:int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[: index])
        container.markdown(curr_full_text)
        time.sleep(1/speed)

# Step 2: Build the Web App
st.title('AI Sentiment Analysis App')
st.write('Type in any sentence and I will tell you if it sounds positive or negative.')
user_input = st.text_area('Enter your sentence here:')


bg_color = "#0E1117"


# Step 3: setting sentiment score = none
if 'sentiment_score' not in st.session_state:
    st.session_state.sentiment_score = None





# Step 4: Analysis 
    
if st.button('Analyze'):
    blob = TextBlob(user_input)
    st.session_state.sentiment_score = blob.sentiment.polarity
    if st.session_state.sentiment_score > 0:
        bg_color = "#1a7e1d"
        st.success(f'This sounds positive! 😀 (score: {st.session_state.sentiment_score:.2f})')
    elif st.session_state.sentiment_score < 0:
        st.error(f'This sounds negative. 😟 (score: {st.session_state.sentiment_score:.2f})')
        bg_color = "#9e0b1a"
    else:
        st.info('This seems neutral. 😐')
if st.session_state.sentiment_score is not None:
    if st.button("Show Graph!"):
        fig, ax = plt.subplots()
        ax.scatter([0], [st.session_state.sentiment_score], s=200) #size = 200, scatter plot, and sentiment score is y value
        plt.xlabel("X-Axis")
        plt.ylabel("Sentiment score")
        plt.title("Scatter Plot sample")
        ax.set_ylim(-1, 1)
        st.pyplot(fig)

st.markdown(
    f"""
    <style>
    html, body, [data-testid="stApp"] {{
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

typewriter(text="Made with 💖 by Aarin Sandilya", speed=5)
