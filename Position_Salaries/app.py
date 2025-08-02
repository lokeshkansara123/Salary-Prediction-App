import streamlit as st
import pickle

# Load model
with open("Position_Salaries.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Salary Prediction App")
st.markdown("Predict salary based on job level and experience using a Decision Tree model.")

level = st.number_input("Enter job level (1-10)", min_value=1.0, max_value=10.0, step=0.1)
experience = st.number_input("Enter years of experience", min_value=0.0, max_value=20.0, step=0.1)


if st.button("Predict Salary"):
    prediction = model.predict([[level, experience]])
    st.write(f"Predicted salary: ₹{prediction[0]:,.2f}")




