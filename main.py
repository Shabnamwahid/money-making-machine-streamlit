

import streamlit as st
import random
import time
import requests

# ✅ Background Image (Sirf CSS ke liye)
background_image = """
<style>
    .stApp {
        background: url("https://i.ebayimg.com/images/g/J04AAOSwcyVc01BA/s-l640.jpg");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
    }
    .block-container {
        padding: 20px;
        border-radius: 10px;
    }
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)  # ✅ Sirf CSS ke liye use ho raha hai

# ✅ Money Making Machine
st.title("💰 Money Making Machine 💰")

def generate_money():
    return random.randint(1, 1000)

st.subheader("💵 Instant Cash Generator 💵")

if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}!")

# ✅ Side Hustle API Function
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles", params={"apiKey": "123456789"})
        if response.status_code == 200:
            data = response.json()
            return data.get("side_hustle", "Freelancing")  # ✅ Key sahi hai
        else:
            return "Freelancing"
    except:
        return "Something went wrong!"

st.subheader("🚀 Side Hustle Ideas 🚀")

if st.button("Generate Hustle", key="hustle_button"):  # ✅ Unique key added
    idea = fetch_side_hustle()
    st.success(idea)

# ✅ Money Quotes API Function
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes", params={"apiKey": "123456789"})
        if response.status_code == 200:
            data = response.json()
            return data.get("money_quote", "Stay focused and keep earning!")  # ✅ Key sahi hai
        else:
            return "Stay focused and keep earning!"
    except:
        return "Money is the root of all evil!"

st.subheader("💡 Money Making Motivation 💡")

if st.button("Get inspired", key="money_button"):  # ✅ Unique key added
    idea = fetch_money_quote()
    st.info(idea)

  

 


st.markdown("<h4 style='text-align: center;'>Built with 💖 by Shabnam Wahid</h4>", unsafe_allow_html=True)


