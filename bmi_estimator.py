import streamlit as st

# ======================
# 🎯 Page Configuration
# ======================
st.set_page_config(page_title="The Professor's BMI Estimator", page_icon="⚖️", layout="centered")

# ===========================
# 🎨 Custom Dark Mode Styling
# ===========================
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .st-cf {
        background-color: #1c1f26 !important;
        color: white !important;
        border-radius: 10px;
        padding: 20px;
    }
    label, input, .stNumberInput, .stButton, .stMarkdown {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ====================
# 🚀 The Professor's BMI Estimator App
# ====================
st.title("⚖️ The Professor’s BMI Estimator")
st.markdown("This app calculates your **Body Mass Index (BMI)** and classifies it based on WHO standards.")

# 📥 User Inputs with Hints
weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    step=0.1,
    format="%.2f",
    help="Enter your current body weight in kilograms (e.g., 70.5)"
)

height = st.number_input(
    "Enter your height (meters)",
    min_value=0.5,
    step=0.01,
    format="%.2f",
    help="Enter your height in meters (e.g., 1.75)"
)

# 🧮 Calculate on button click
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)

        # 🏷️ Classification and health message
        if bmi < 18.5:
            bmi_class = "Underweight"
            health_msg = "⚠️ You're underweight. It's important to eat well-balanced meals and consult with a healthcare provider to ensure you're on a healthy path."
        elif bmi < 25:
            bmi_class = "Normal"
            health_msg = "✅ Great job! You're within a healthy weight range. Keep up your good habits and stay consistent!"
        elif bmi < 30:
            bmi_class = "Overweight"
            health_msg = "⚠️ You're slightly above the recommended weight range. Consider adjusting your diet and activity level to avoid long-term health risks."
        elif bmi < 35:
            bmi_class = "Obese Class I"
            health_msg = "⚠️ Your BMI falls in Obese Class I. Please take steps to manage your weight with lifestyle changes and consider medical advice."
        elif bmi < 40:
            bmi_class = "Obese Class II"
            health_msg = "⚠️ Your BMI indicates Obese Class II. Health risks increase at this level. It's highly advised to speak to a healthcare professional."
        else:
            bmi_class = "Obese Class III"
            health_msg = "🚨 Your BMI is in the highest obesity category. Please prioritize your health by seeking medical guidance and adopting healthier habits."

        # 📊 Output
        st.success(f"✅ Your BMI is **{bmi:.2f}**")
        st.info(f"**Classification:** {bmi_class}")
        st.warning(health_msg) if "⚠️" in health_msg or "🚨" in health_msg else st.success(health_msg)

    else:
        st.error("Please provide valid positive numbers for height and weight.")

# 📝 Footer
st.markdown("---")
st.markdown(
    """
    <div style="font-size: 13px; color: #ccc;">
        Built with ❤️ using Streamlit • Based on WHO BMI classification<br>
        Created by <b>Tolulope Emuleomo</b> aka <b>Data Professor</b> 🧠<br>
        🔗 <a href="https://twitter.com/dataprofessor_" target="_blank">Twitter: @dataprofessor_</a> •
        <a href="https://github.com/dataprofessor290" target="_blank">GitHub: dataprofessor290</a><br>
        💼 Data Scientist
    </div>
    """,
    unsafe_allow_html=True
)
