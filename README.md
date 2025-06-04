# 🧪 Take-Home: Mood of the Queue

A quick internal tool to log and visualize the "vibe" of the ticket queue.


## 🚀 Setup

To run the app:

https://ssinghaditi-mochihealth-take-home-mochi-health-ooh9ib.streamlit.app/

or locally:

```bash
streamlit run app.py
```

## ✅ Features

* **Mood Form**

  * Select a mood (emoji dropdown)
  * Optional notes
* **Visualization**

  * Bar chart of today’s moods
* **Storage**

  * Auto-saves entries to Google Sheet with timestamp

## 🛠️ Tech Stack

* Streamlit
* Google Sheets (https://docs.google.com/spreadsheets/d/1Mq7kRCuTr9hQGI9kYhYuEued-x_MzRNmzEknjF8nTc8/edit?usp=sharing)
* Matplotlib

## 📝 Google Sheet Columns

* **Time** – timestamp of form submission
* **Emoji** – emoji submitted for ticket
* **Notes** – any notes for the ticket
