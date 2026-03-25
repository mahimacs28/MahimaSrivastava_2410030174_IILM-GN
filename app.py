import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# PAGE CONFIG + STYLE
# -----------------------------
st.set_page_config(page_title="IDS Dashboard", layout="wide")

# Custom CSS (BIG FONT + MODERN UI)
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 18px;
    }
    h1 {
        font-size: 42px !important;
    }
    h2 {
        font-size: 30px !important;
    }
    h3 {
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("model/model.pkl", "rb"))

# -----------------------------
# PREPROCESS FUNCTION (FIX)
# -----------------------------
def preprocess_input(df):
    df = df.dropna()

    # Handle attack_cat if exists
    if 'attack_cat' in df.columns:
        df['label'] = df['attack_cat'].apply(lambda x: 0 if x == 'Normal' else 1)
        df = df.drop('attack_cat', axis=1)

    # Encode categorical
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])

    # Drop label if exists
    if 'label' in df.columns:
        df = df.drop('label', axis=1)

    return df

# -----------------------------
# TITLE
# -----------------------------
st.title("🚨 Intrusion Detection System for Cloud")
st.markdown("### Detect malicious or normal network traffic using Machine Learning")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select Option", ["Manual Input", "Upload CSV", "About"])

# -----------------------------
# MANUAL INPUT (FIXED)
# -----------------------------
if option == "Manual Input":
    st.subheader("🧠 Manual Feature Input (Demo Mode)")

    st.warning("⚠️ This is demo mode. For accurate results, use CSV upload.")

    # Create dummy input with correct number of features (43)
    input_data = np.zeros((1, 43))

    if st.button("Predict"):
        result = model.predict(input_data)

        if result[0] == 0:
            st.success("✅ Normal Traffic")
        else:
            st.error("⚠️ Intrusion Detected!")

# -----------------------------
# CSV UPLOAD (FIXED)
# -----------------------------
elif option == "Upload CSV":
    st.subheader("📂 Upload Network Traffic Data")

    file = st.file_uploader("Upload CSV File", type=["csv"])

    if file:
        df = pd.read_csv(file)

        st.write("### 🔍 Preview of Data")
        st.dataframe(df.head())

        try:
            processed_df = preprocess_input(df)

            predictions = model.predict(processed_df)
            df["Prediction"] = predictions
            df["Prediction"] = df["Prediction"].map({0: "Normal", 1: "Attack"})

            st.write("### ✅ Prediction Results")
            st.dataframe(df)

            # Graph
            st.subheader("📊 Attack Distribution")

            counts = df["Prediction"].value_counts()

            fig, ax = plt.subplots()
            ax.bar(counts.index, counts.values)
            ax.set_xlabel("Traffic Type")
            ax.set_ylabel("Count")

            st.pyplot(fig)

            # Metrics
            st.subheader("📈 Summary")

            total = len(df)
            attacks = counts.get("Attack", 0)
            normal = counts.get("Normal", 0)

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Records", total)
            col2.metric("Normal Traffic", normal)
            col3.metric("Intrusions Detected", attacks)

        except Exception as e:
            st.error(f"❌ Error: {e}")

# -----------------------------
# ABOUT
# -----------------------------
elif option == "About":
    st.subheader("📘 About Project")

    st.write("""
    This project is an Intrusion Detection System using Machine Learning to detect cyber attacks in cloud environments.

    🔹 Model Used:
    - Random Forest

    🔹 Dataset:
    - UNSW-NB15

    🔹 Features:
    - Real-time prediction
    - CSV bulk detection
    - Visualization dashboard
    """)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    "<center><b>✨ Developed by Mahima Srivastava, Anshika Nigam, Hammad Siddiqui | IILM University, Greater Noida ✨</b></center>",
    unsafe_allow_html=True
)