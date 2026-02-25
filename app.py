import streamlit as st
import numpy as np
import pickle

# ——— Page configuration
st.set_page_config(
    page_title="🩺 Diabetes Predictor AI",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ——— Load the trained model
model = pickle.load(open("trained_model.sav", "rb"))

def diabetes_prediction(input_data):
    arr = np.array(input_data).reshape(1, -1)
    pred = model.predict(arr)
    return "🧠 Diabetic" if pred[0] == 1 else "😊 Non‑Diabetic"

# ——— Sidebar content
with st.sidebar:
    st.title("📊 Input Parameters")
    st.write("Adjust the values for prediction:")

    pregnancies = st.slider("Pregnancies", 0, 15, 1)
    glucose = st.slider("Glucose Level", 0, 200, 100)
    bp = st.slider("Blood Pressure", 0, 140, 80)
    skin_thick = st.slider("Skin Thickness", 0, 100, 20)
    insulin = st.slider("Insulin Level", 0, 300, 80)
    bmi = st.slider("BMI", 10, 60, 25)
    pedigree = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.slider("Age", 1, 100, 30)

# ——— App title + image/header
st.title("🩺 Diabetes Prediction Web App")
st.write("Predict if a patient has diabetes using health metrics (AI model)")

# Optional info section
with st.expander("ℹ️ How it works"):
    st.write("""
        Enter patient health metrics in the sidebar.
        The AI model uses these values to predict diabetes risk.
        Outputs show a clear and friendly result.
    """)

# ——— Show input summary
st.markdown("### 🔎 Review Entered Information")
left_col, right_col = st.columns(2)

with left_col:
    st.write(f"**Pregnancies:** {pregnancies}")
    st.write(f"**Glucose:** {glucose}")
    st.write(f"**Blood Pressure:** {bp}")
    st.write(f"**Skin Thickness:** {skin_thick}")

with right_col:
    st.write(f"**Insulin Level:** {insulin}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Pedigree Func:** {pedigree}")
    st.write(f"**Age:** {age}")

# ——— Make prediction button
if st.button("🧪 Predict"):
    result = diabetes_prediction([
        pregnancies, glucose, bp, skin_thick,
        insulin, bmi, pedigree, age
    ])

    # Display result prominently
    if "Non‑Diabetic" in result:
        st.success(f"✔️ Prediction: {result}")
    else:
        st.error(f"⚠️ Prediction: {result}")