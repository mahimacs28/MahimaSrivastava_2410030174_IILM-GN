# 🚨 Intrusion Detection System for Cloud using Machine Learning

## 📌 Overview
This project is a Machine Learning-based Intrusion Detection System (IDS) that detects whether network traffic is **normal** or an **attack**.  
It uses the **UNSW-NB15 dataset** and a trained **Random Forest model** to identify malicious activities.

---

## 🎯 Objective
The goal of this project is to enhance cybersecurity by automatically detecting suspicious network behavior using Machine Learning techniques.

---

## 🧠 How It Works
1. Network traffic data is taken as input
2. Data is preprocessed (cleaning + encoding)
3. Machine Learning model is trained
4. Model predicts:
   - ✅ Normal Traffic  
   - ⚠️ Intrusion Detected  
5. Results are displayed on a dashboard

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## 📊 Dataset
- **UNSW-NB15 Dataset**
- Contains modern network traffic with various attack types

---

## 🤖 Machine Learning Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest (Selected as Best Model)

---

## 🚀 Features
- Real-time intrusion detection  
- CSV file upload for bulk prediction  
- Interactive dashboard using Streamlit  
- Graphical visualization of results  
- Automated detection using ML  

---

## 🖥️ Dashboard
- Upload network traffic data (CSV)
- View predictions instantly
- Visualize attack distribution
- Summary metrics display

---
## 👨‍💻 Developed By
- Mahima Srivastava
**IILM University, Greater Noida**


## 🚀 Future Scope
- Real-time cloud deployment
- Integration with live network traffic
- Advanced deep learning models

---
## ▶️ How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt
2. Run the application:
streamlit run app.py
