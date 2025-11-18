# Eco-EV-chatbot-and-dashboard-assistant-
A Streamlit-based interactive system that provides EV insights through a rule-based AI chatbot and real-time dashboard visualizations.

📌 Overview

The Eco EV Companion integrates an AI-powered rule-based chatbot with a dynamic analytics dashboard to help users understand Electric Vehicle (EV) performance, charging behavior, and energy efficiency.
It simplifies EV data analysis and supports decision-making through intuitive charts and natural-language interactions.

🎯 Features
🔹 EV Analytics Dashboard

Distance vs Energy Consumption

Cost vs Distance

Charging Time Distribution

Daily Efficiency Trends

Derived metrics (cost/km, energy/km)

🔹 AI Chatbot

Rule-based NLP

Recognizes intents using keywords

Answers questions on:

Charging time

Energy consumption

Battery usage

Cost estimation

Environmental benefits

🔹 User Interface

Streamlit split layout

Chatbot on left panel

Dashboard on right panel

Beginner-friendly and clean UI

🧠 System Architecture

User Interface Layer – Streamlit chat panel + dashboard view

Chatbot Engine – Intent detection + response generation

Data Management Layer – Dataset loading, preprocessing, derived metrics

Visualization Layer – Interactive charts (Plotly/Matplotlib)

Backend Logic – Python functions powering data flow

🛠 Tech Stack
Component	Technology
UI Framework	Streamlit
Data Processing	Pandas
Visualization	Plotly / Matplotlib
NLP	Rule-based keywords
Language	Python
📂 Project Structure
Eco-EV-Companion/
│── app.py                 # Main Streamlit app
│── chatbot.py             # Chatbot logic
│── dashboard.py           # Visualizations
│── utils.py               # Helper functions
│── data/ev_data.csv       # EV dataset
│── README.md              # Project documentation

▶️ How to Run the Project
1. Install dependencies
pip install streamlit pandas plotly matplotlib

2. Run the Streamlit app
streamlit run app.py

3. Open in browser

Streamlit starts automatically at:

http://localhost:8501

📊 Dataset Preprocessing

Remove null values

Standardize units (km, kWh)

Compute cost/km & energy/km

Normalize values for smoother visualization

💬 Chatbot Intent Mapping
Intent	Keywords
Charging Info	"charging", "time"
Cost Calculation	"cost", "price"
Battery Info	"battery", "range"
Eco Benefits	"benefits", "environment"
🎉 Results

Improved user understanding of EV performance

Clear visual patterns of consumption & cost

Easy access to EV knowledge through chatbot

Enhanced learning for first-time EV users

🚀 Future Enhancements

Real-time EV API integration

ML-based battery and range prediction

Mobile app version

Multilingual chatbot

Voice-enabled EV assistant
