# 🧪 Take-Home: Mood of the Queue

A quick internal tool to log and visualize the "vibe" of the ticket queue.


## 🚀 Setup

To run the app:

```bash
streamlit run app.py
```

**Note:**
My Google service account credentials file (`my-project-mochi-58e87dc36608.json`) is needed to connect with Google Sheets.

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
* Google Sheets 
* Matplotlib

## 📝 Google Sheet Columns

* **Time** – timestamp of form submission
* **Emoji** – emoji submitted for ticket
* **Notes** – any notes for the ticket
