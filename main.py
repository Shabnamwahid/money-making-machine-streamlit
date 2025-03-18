import streamlit as st 
import random
import time
import requests


# bg image
background_image = """
<style>
    .stApp {
        background: url("https://i.ebayimg.com/images/g/J04AAOSwcyVc01BA/s-l640.jpg");
           
        background-size: contain;  /* Full image dikhayega bina crop kiye */
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
        }
</style>
"""

# ✅ Apply the CSS
st.markdown(background_image, unsafe_allow_html=True)

# money making  machine

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

# ✅ Move UI elements outside the function
st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You made ${amount}!")


#   Simple Api  side_hustle

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles", params={"apiKey": "123456789"})
        if response.status_code == 200:
            data = response.json()
            return data.get("side_hustle", "Freelancing")  # ✅ Correct key
        else:
            return "Freelancing"
    except:
        return "Something went wrong!"

st.subheader("Side Hustle Ideas")

if st.button("Generate Hustle", key="hustle_button"):  # ✅ Unique key added
    idea = fetch_side_hustle()
    st.success(idea)

# money_quotes
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes", params={"apiKey": "123456789"})
        if response.status_code == 200:
            data = response.json()
            return data.get("money_quote", "Stay focused and keep earning!")  # ✅ Corrected key
        else:
            return "Stay focused and keep earning!"
    except:
        return "Money is the root of all evil!"

st.subheader("Money Making Motivation")

if st.button("Get inspired", key="money_button"):  # ✅ Unique key added
    idea = fetch_money_quote()
    # st.success(idea)
    st.info(idea)


# import streamlit as st 
# import random
# import time
# import requests

# # ✅ Background Image
# background_image = """
# <style>
#     .stApp {
#         background: url("https://do.lolwot.com/wp-content/uploads/2016/04/10-stupid-criminals-who-got-caught-for-ridiculous-reasons-4.jpg");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-position: center center;
#         background-attachment: fixed;
#     }

#     /* ✅ White Border for All Text Elements */
#     .stText, .stTitle, .stHeader, .stSubheader, .stMarkdown, .stSuccess, .stInfo {
#         border: 2px solid white; 
#         padding: 10px;
#         display: inline-block;
#         background-color:  black; /* Dark background for better visibility */
#         color: white;
#         border-radius: 5px;
#     }
# </style>
# """

# st.markdown(background_image, unsafe_allow_html=True)

# # ✅ Money Making Machine
# st.title("💰 Money Making Machine 💰")

# def generate_money():
#     return random.randint(1, 1000)

# st.subheader("💵 Instant Cash Generator 💵")

# if st.button("Generate Money"):
#     st.write("Counting your money...")
#     time.sleep(1)
#     amount = generate_money()
#     st.success(f"You made ${amount}!")

# # ✅ Side Hustle API
# def fetch_side_hustle():
#     try:
#         response = requests.get("http://127.0.0.1:8000/side_hustles", params={"apiKey": "123456789"})
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("side_hustle", "Freelancing")
#         else:
#             return "Freelancing"
#     except:
#         return "Something went wrong!"

# st.subheader("🚀 Side Hustle Ideas 🚀")

# if st.button("Generate Hustle", key="hustle_button"):
#     idea = fetch_side_hustle()
#     st.success(idea)

# # ✅ Money Quotes API
# def fetch_money_quote():
#     try:
#         response = requests.get("http://127.0.0.1:8000/money_quotes", params={"apiKey": "123456789"})
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("money_quote", "Stay focused and keep earning!")
#         else:
#             return "Stay focused and keep earning!"
#     except:
#         return "Money is the root of all evil!"

# st.subheader("💡 Money Making Motivation 💡")

# if st.button("Get inspired", key="money_button"):
#     idea = fetch_money_quote()
#     st.info(idea)
