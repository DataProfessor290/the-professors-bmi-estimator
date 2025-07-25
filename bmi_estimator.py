import streamlit as st

# =======================
# 🎯 App Config
# =======================
st.set_page_config(
    page_title="The Professor's BMI Estimator",
    page_icon="⚖️",
    layout="centered",
)

# =======================
# 🎓 Title & Header
# =======================
st.title("⚖️ The Professor’s BMI Estimator")
st.markdown("This app calculates your **Body Mass Index (BMI)** and classifies it based on **WHO standards**.")

st.divider()

# =======================
# 📥 User Input
# =======================
st.caption("💡 Enter your weight in kilograms (e.g., 65.0)")
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, format="%.2f")

st.caption("💡 Enter your height in meters (e.g., 1.75)")
height = st.number_input("Enter your height (meters)", min_value=0.5, step=0.01, format="%.2f")

# =======================
# 🧮 Calculate BMI Button
# =======================
if st.button("📏 Calculate BMI"):
    bmi = round(weight / (height ** 2), 2)

    # Determine BMI Class
    if bmi < 18.5:
        bmi_class = "Underweight"
        health_msg = "⚠️ You're underweight. Consider consulting a healthcare provider to ensure you're getting adequate nutrition."
    elif bmi < 25:
        bmi_class = "Normal"
        health_msg = "✅ Great job! You're within a healthy weight range. Keep up your good habits and stay consistent!"
    elif bmi < 30:
        bmi_class = "Overweight"
        health_msg = "⚠️ You're slightly overweight. Consider incorporating more physical activity and a balanced diet into your routine."
    elif bmi < 35:
        bmi_class = "Obese Class I"
        health_msg = "🚨 Obese Class I. It's advisable to take immediate steps toward healthier habits."
    elif bmi < 40:
        bmi_class = "Obese Class II"
        health_msg = "🚨 Obese Class II. You're at significant risk. Please consult a medical professional."
    else:
        bmi_class = "Obese Class III"
        health_msg = "🚨 Obese Class III. This is a critical health risk. Seek medical advice promptly."

    # =======================
    # 📊 Output Section
    # =======================
    st.success(f"✅ Your BMI is **{bmi}**")
    st.markdown(f"**Classification**: {bmi_class}")

    if "⚠️" in health_msg or "🚨" in health_msg:
        st.warning(health_msg)
    else:
        st.success(health_msg)

# =======================
# 👣 Footer
# =======================
st.divider()
st.caption("Built with ❤️ using Streamlit • Based on WHO BMI classification")
st.caption("Created by **Tolulope Emuleomo** aka **Data Professor** 🧠")
st.caption("🔗 [Twitter: @dataprofessor_](https://twitter.com/dataprofessor_) • [GitHub: dataprofessor290](https://github.com/dataprofessor290)")
st.caption("💼 Data Scientist")
