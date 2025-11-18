import streamlit as st
import pandas as pd
import os
import random

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Eco EV Dashboard & Chatbot", page_icon="🔋", layout="wide")

st.title("🔋 Eco EV Dashboard & Chatbot Assistant")
st.caption("Explore electric vehicle insights, efficiency trends, and get instant recommendations through an AI-powered chatbot.")

# -----------------------------
# Load or Create Dataset
# -----------------------------
@st.cache_data
def load_data():
    file_path = r"C:\Users\Harshika\Downloads\eco ev chatbot\data\ev_data.csv"
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        default_data = {
            "Model": [
                "Tata Nexon EV", "MG ZS EV", "Hyundai Kona Electric",
                "Mahindra XUV400", "BYD e6", "Tata Tiago EV"
            ],
            "Battery_Capacity_kWh": [30.2, 44.5, 39.2, 39.4, 71.7, 24.0],
            "Range_km": [312, 419, 452, 456, 520, 250],
            "Charging_Time_hr": [8, 6.5, 6, 6.5, 10, 9],
            "Efficiency_km_per_kWh": [10.3, 9.4, 11.5, 11.6, 7.2, 10.4],
            "Price_INR_Lakh": [14.0, 23.5, 23.8, 16.5, 29.2, 8.5],
        }
        df = pd.DataFrame(default_data)
        df.to_csv(file_path, index=False)
        st.success("✅ Default EV dataset created automatically.")
    else:
        df = pd.read_csv(file_path)
    return df

df = load_data()

if df.empty:
    st.warning("No EV data found. Please upload or add EV entries.")
    st.stop()

# -----------------------------
# Tabs Layout
# -----------------------------
tab1, tab2 = st.tabs(["📊 EV Dashboard", "🤖 EV Chatbot"])

# -----------------------------
# Dashboard Tab
# -----------------------------
with tab1:
    st.subheader("📈 EV Model Overview")

    # --- Search Functionality
    search = st.text_input("🔍 Search EV Model", placeholder="Type to filter (e.g., Tata, MG, BYD)...")
    filtered_df = df[df["Model"].str.contains(search, case=False)] if search else df
    st.dataframe(filtered_df, use_container_width=True)

    # --- Metric Cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🌍 Average Range (km)", round(df["Range_km"].mean(), 1))
    with c2:
        st.metric("⚡ Fastest Charging EV", df.loc[df["Charging_Time_hr"].idxmin(), "Model"])
    with c3:
        st.metric("💰 Average Price (₹ Lakh)", round(df["Price_INR_Lakh"].mean(), 2))

    st.markdown("---")

    # --- Charts
    st.subheader("⚡ Range vs Battery Capacity")
    st.bar_chart(df.set_index("Model")[["Range_km", "Battery_Capacity_kWh"]])

    st.subheader("💰 Price vs Efficiency")
    st.scatter_chart(df, x="Price_INR_Lakh", y="Efficiency_km_per_kWh", color="Model")

    st.subheader("⏱️ Charging Time Comparison")
    st.bar_chart(df.set_index("Model")[["Charging_Time_hr"]])

# -----------------------------
# Chatbot Tab
# -----------------------------
with tab2:
    st.subheader("💬 Eco EV Chatbot Assistant")
    st.write("Ask me anything about EVs — range, efficiency, price, or recommendations!")

    user_input = st.text_input("🗨️ You:", placeholder="Try asking 'Which EV gives best value for money?' or 'Show EVs under 20 lakh'")

    fun_facts = [
        "🔋 EVs convert over 77% of grid energy to power at the wheels.",
        "🌱 EVs produce zero tailpipe emissions — great for the environment!",
        "⚡ Fast chargers can power EVs up to 80% in under an hour.",
        "🚗 India’s EV market is expected to grow at 49% CAGR by 2030."
    ]

    if user_input:
        query = user_input.lower()
        response = ""

        if "best range" in query:
            best = df.loc[df["Range_km"].idxmax()]
            response = f"🚗 The best range EV is **{best['Model']}** with **{best['Range_km']} km** per charge."
        elif "fastest charging" in query or "least charging" in query:
            fast = df.loc[df["Charging_Time_hr"].idxmin()]
            response = f"⚡ The fastest charging EV is **{fast['Model']}**, taking only **{fast['Charging_Time_hr']} hours**."
        elif "efficient" in query:
            eff = df.loc[df["Efficiency_km_per_kWh"].idxmax()]
            response = f"🌿 The most efficient EV is **{eff['Model']}**, offering **{eff['Efficiency_km_per_kWh']} km/kWh**."
        elif "cheapest" in query or "lowest price" in query:
            cheap = df.loc[df["Price_INR_Lakh"].idxmin()]
            response = f"💸 The cheapest EV is **{cheap['Model']}**, costing ₹{cheap['Price_INR_Lakh']} Lakh."
        elif "expensive" in query or "highest price" in query:
            costly = df.loc[df["Price_INR_Lakh"].idxmax()]
            response = f"💰 The most expensive EV is **{costly['Model']}**, priced at ₹{costly['Price_INR_Lakh']} Lakh."
        elif "value for money" in query:
            df["Value_Index"] = df["Range_km"] / df["Price_INR_Lakh"]
            best_value = df.loc[df["Value_Index"].idxmax()]
            response = f"💡 Best value-for-money EV: **{best_value['Model']}**, offering {round(best_value['Value_Index'], 2)} km per ₹ Lakh."
        elif "under" in query and "lakh" in query:
            try:
                limit = float(query.split("under")[1].split("lakh")[0].strip())
                under_df = df[df["Price_INR_Lakh"] <= limit]
                if not under_df.empty:
                    models = ", ".join(under_df["Model"])
                    response = f"💰 EVs under ₹{limit} Lakh: {models}."
                else:
                    response = f"No EVs found under ₹{limit} Lakh."
            except:
                response = "Please mention a valid price limit (e.g., under 20 lakh)."
        elif "above" in query and "km" in query:
            try:
                km = int(query.split("above")[1].split("km")[0].strip())
                above_df = df[df["Range_km"] > km]
                if not above_df.empty:
                    models = ", ".join(above_df["Model"])
                    response = f"🚀 EVs with range above {km} km: {models}."
                else:
                    response = f"No EVs found above {km} km range."
            except:
                response = "Please specify a valid number for range (e.g., above 400 km)."
        elif "recommend" in query or "suggest" in query:
            rec = random.choice(df["Model"].tolist())
            response = f"🔋 You might like the **{rec}**, it offers a great balance of range and price!"
        else:
            response = "🤔 I can help you with EV price, efficiency, range, or model suggestions."

        st.success(response)

        # Add random fact for engagement
        st.info(random.choice(fun_facts))
