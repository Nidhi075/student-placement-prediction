import streamlit as st
import pickle

st.title("Student Placement Prediction")

st.write("Enter the student's details:")

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=8.0)
tenth = st.number_input("10th Percentage", min_value=0.0, max_value=100.0, value=88.0)
twelfth = st.number_input("12th Percentage", min_value=0.0, max_value=100.0, value=86.0)
backlogs = st.number_input("Backlogs", min_value=0, value=0)
internships = st.number_input("Internships", min_value=0, value=1)
projects = st.number_input("Projects", min_value=0, value=3)
skills = st.number_input("Skills Score", min_value=0, value=8)
aptitude = st.number_input("Aptitude Score", min_value=0, value=8)

if st.button("Predict Placement"):

    with open("placement_model.pkl", "rb") as file:
        model = pickle.load(file)

    new_student = [[
        cgpa,
        tenth,
        twelfth,
        backlogs,
        internships,
        projects,
        skills,
        aptitude
    ]]

    prediction = model.predict(new_student)

    if prediction[0] == 1:
        st.success("🎉 Student is likely to be PLACED")
    else:
        st.error("Student is likely NOT to be PLACED")