import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Teaching Dashboard", layout="wide")

teaching_reputation_weight = 0.15
staff_to_student_ratio_weight = 0.045
doctorate_to_bachelor_weight = 0.02
doctorate_to_staff_weight = 0.055
institutional_income_weight = 0.025

teaching_reputation_score = 0.0
staff_to_student_ratio_score = 0.0
doctorate_to_bachelor_score = 0.0
doctorate_to_staff_score = 0.0
institutional_income_score = 0.0

def teaching_reputation_section():
    global teaching_reputation_score

    teaching_reputation_left, teaching_reputation_right = st.columns(2)

    st.divider()
    with teaching_reputation_left:
        st.subheader("Teaching Reputation")
        teaching_reputation_score = st.slider("Teaching Reputation Score", 0.0, 100.0, 0.0)
        st.write(f"Teaching Reputation Score: {teaching_reputation_score}")

    with teaching_reputation_right:
        st.write("### Teaching Reputation Score ###")

        st.bar_chart({"a: yet to achieve": [100-teaching_reputation_score],
                      "b: achieved": [teaching_reputation_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])    


def staff_to_student_ratio_section():
    global staff_to_student_ratio_score
    # Create two columns layout
    staff_to_student_ratio_left, staff_to_student_ratio_right = st.columns(2)

    st.divider()
    with staff_to_student_ratio_left:
        st.subheader("Staff to Student Ratio")
        fte_students = st.number_input("Enter the no. of FTE students at the university:", step=1, value=1, format="%d")
        fte_staffs = st.number_input("Enter the no. of FTE academic staffs at the university:", step=1, value=0, format="%d")
        ratio = fte_staffs / fte_students
        if ratio <0.1:
            staff_to_student_ratio_score = ratio * 1000
        elif ratio >= 0.1:
            staff_to_student_ratio_score = 100
        st.write(f"Staff to Student Ratio Score: {staff_to_student_ratio_score}")

    with staff_to_student_ratio_right:
        st.write("### Staff to Student Ratio Score ###")

        st.bar_chart({"a: yet to achieve": [100-staff_to_student_ratio_score], 
                      "b: achieved": [staff_to_student_ratio_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


def doctorate_to_bachelor_ratio_section():
    global doctorate_to_bachelor_score
    # Create two columns layout
    doctorate_to_bachelor_ratio_left, doctorate_to_bachelor_ratio_right = st.columns(2)

    st.divider()
    with doctorate_to_bachelor_ratio_left:
        st.subheader("Doctorate to Bachelor Ratio")
        doctorate_students = st.number_input("Enter the no. of students completed their Doctorate at the university:", step=1, value=0, format="%d")
        bachelor_students = st.number_input("Enter the no. of students completed their bachelor at the university:", step=1, value=1, format="%d")
        ratio = doctorate_students / bachelor_students
        if ratio < 0.1:
            doctorate_to_bachelor_score = ratio * 1000
        elif ratio >= 0.1:
            doctorate_to_bachelor_score = 100
        st.write(f"Doctorate to Bachelor Ratio Score: {doctorate_to_bachelor_score}")

    with doctorate_to_bachelor_ratio_right:
        st.write("### Doctorate to Bachelor Ratio Score ###")

        st.bar_chart({"a: yet to achieve": [100-doctorate_to_bachelor_score], 
                      "b: achieved": [doctorate_to_bachelor_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])



def doctorate_to_staff_ratio_section():
    global doctorate_to_staff_score
    # Create two columns layout
    doctorate_to_staff_ratio_left, doctorate_to_staff_ratio_right = st.columns(2)

    st.divider()
    with doctorate_to_staff_ratio_left:
        st.subheader("Doctorate awarded to Academic Staff Ratio")
        doctorate_students = st.number_input("Enter the no. of students completed their Doctorate at the university:", step=1, value=0, format="%d", key="doctorate_students_input")
        fte_staff = st.number_input("Enter the no. of FTE Academic Staffs at the university:", step=1, value=1, format="%d")
        ratio = doctorate_students / fte_staff
        if ratio < 0.1:
            doctorate_to_staff_score = ratio * 1000
        elif ratio >= 0.1:
            doctorate_to_staff_score = 100
        st.write(f"Doctorate awarded to Academic Staff Ratio Score: {doctorate_to_staff_score}")

    with doctorate_to_staff_ratio_right:
        st.write("### Doctorate awarded to Academic Staff Ratio Score ###")

        st.bar_chart({"a: yet to achieve": [100-doctorate_to_staff_score], 
                      "b: achieved": [doctorate_to_staff_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


def institutional_income_score_section():
    global institutional_income_score
    # Create two columns layout
    institutional_income_score_left, institutional_income_score_right = st.columns(2)

    st.divider()
    with institutional_income_score_left:
        st.subheader("Institutional Income Score")
        institutional_income = st.number_input("Enter the Institutional Income to academic staff at the university:", step=1, value=0, format="%d", key="institutional_income_input")
        institutional_income_score = (100*institutional_income)/3000000.00
        st.write(f"Institutional Income Score: {institutional_income_score}")

    with institutional_income_score_right:
        st.write("### Institutional Income Score ###")

        st.bar_chart({"a: yet to achieve": [100-institutional_income_score], 
                      "b: achieved": [institutional_income_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])






def main():
    teaching_reputation_section()
    staff_to_student_ratio_section()
    doctorate_to_bachelor_ratio_section()
    doctorate_to_staff_ratio_section()
    institutional_income_score_section()

    total_teaching_score = teaching_reputation_score * teaching_reputation_weight + staff_to_student_ratio_score * staff_to_student_ratio_weight + doctorate_to_bachelor_score * doctorate_to_bachelor_weight + doctorate_to_staff_score * doctorate_to_staff_weight + institutional_income_score * institutional_income_weight

    st.subheader(f"Teaching Score: {total_teaching_score}")
    st.bar_chart({"a: yet to achieve": [100-total_teaching_score], 
                      "b: achieved": [total_teaching_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


if __name__ == "__main__":
    main()