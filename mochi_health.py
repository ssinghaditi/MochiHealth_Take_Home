import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open("Mochi Health").sheet1

# Function to show bar graph of mood submissions
def show_graph():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    if df.empty:
        st.write("")
        st.markdown("<p style='font-size:17px; margin-bottom:0;'> No submissions yet for today. </p>", unsafe_allow_html=True)
        st.write("")
    else:
        df = df[pd.to_datetime(df["Time"]).dt.date == datetime.now().date()]

        emoji_counts = df["Emoji"].value_counts().sort_values(ascending=False)
        label_counts = emoji_counts.rename(index=labels)

        fig, ax = plt.subplots()
        ax.bar(label_counts.index, label_counts.values)
        ax.set_title(f"Mood Tracker for {datetime.now().date()}")
        ax.set_xlabel("Mood")
        ax.set_ylabel("Count")

        max_count = int(label_counts.values.max())
        ax.set_yticks(range(0, max_count + 1))

        st.pyplot(fig)

# Emoji labels for the form and what they mean
labels = {
        "🤩": "Spectacular",
        "😁": "Good",
        "🫤": "Ok",
        "🤬": "Bad",
        "😭": "Very bad",
        "🤔": "Idk man",
}

# Form
with st.form("mood_form", clear_on_submit=True):
    st.title(" Mood Form 📝")

    st.write("--------------------")

    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 🤩: Spectacular! </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 😁: Good </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 🫤: Ok </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 🤬: Bad </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 😭: So bad I'm crying </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; margin-bottom:0;'> 🤔: Idk man </p>", unsafe_allow_html=True)

    st.write("--------------------")

    st.write("")

    # 1st question
    st.markdown("<p style='font-size:20px; margin-bottom:0;'> Sooo what's the vibe? </p>", unsafe_allow_html=True)

    emoji_options = ["🤩", "😁", "🫤", "🤬", "😭", "🤔"]
    emoji = st.selectbox("", emoji_options)

    st.write("")
    st.write("")

    # 2nd question
    st.markdown("<p style='font-size:20px; margin-bottom:0;'> Any notes? (optional) </p>", unsafe_allow_html=True)
    notes = st.text_area("", height=150)

    st.write("")
    st.write("")
    submitted = st.form_submit_button("Submit")

# On submitting form, show graph and push to Google Sheets
if submitted:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [time, emoji, notes]
    sheet.append_row(row)
    st.success("Another ticket down! 🌟")
    show_graph()

# To just see the bar graph
if st.button("Show the mood today"):
    show_graph()