import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# App styling
st.set_page_config(page_title="Sales Predictor", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #0a3d62;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.3em;
        color: #3c6382;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Background image
st.image("images/bg.jpg", use_container_width=True)

st.markdown('<div class="title">📈 Sales Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict your sales based on your ad budgets</div>', unsafe_allow_html=True)

# Sidebar for input
st.sidebar.header("Enter Advertisement Budgets")
tv = st.sidebar.number_input("TV Budget ($)", min_value=0.0, step=1.0)
radio = st.sidebar.number_input("Radio Budget ($)", min_value=0.0, step=1.0)
newspaper = st.sidebar.number_input("Newspaper Budget ($)", min_value=0.0, step=1.0)

# Predict button
if st.sidebar.button("Predict Sales"):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)[0]

    st.success(f"🧠 Predicted Sales: **{prediction:.2f} Units**")

    st.balloons()
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f0f0f0;
        color: #FFFFFF;
        font-size: 20px;
    }
    </style>

    <div class="footer">
        Developed by Jacob
    </div>
    """,
    unsafe_allow_html=True
)



