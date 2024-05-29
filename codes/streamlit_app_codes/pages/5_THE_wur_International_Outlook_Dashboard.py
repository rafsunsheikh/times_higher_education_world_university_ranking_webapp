import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="International Outlook Dashboard", layout="wide")

proportion_of_interntaional_students_weight = 0.025
proportion_of_international_staff_weight = 0.025
international_collaboration_weight = 0.025

proportion_of_interntaional_students_score = 0.0
proportion_of_international_staff_score = 0.0
international_collaboration_score = 0.0

def proportion_of_interntaional_students_section():
    global proportion_of_interntaional_students_score

    proportion_of_interntaional_students_left, proportion_of_interntaional_students_right = st.columns(2)

    st.divider()
    with proportion_of_interntaional_students_left:
        st.subheader("Proportion of International Students")
        fte_students = st.number_input("Enter the total no. of FTE students at the university:", step=1, value=1, format="%d", key="fte_students_input")
        fte_international_students = st.number_input("Enter the total no. of FTE International students at the university:", step=1, value=0, format="%d", key="fte_international_students_input")
        proportion_of_interntaional_students_score = (100*fte_international_students)/fte_students
        st.write(f"Proportion of International Students Score: {proportion_of_interntaional_students_score}")

    with proportion_of_interntaional_students_right:
        st.write("### Proportion of International Students Score ###")

        st.bar_chart({"a: yet to achieve": [100-proportion_of_interntaional_students_score],
                      "b: achieved": [proportion_of_interntaional_students_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
        



def proportion_of_international_staff_section():
    global proportion_of_international_staff_score
    # Create two columns layout
    proportion_of_international_staff_left, proportion_of_international_staff_right = st.columns(2)

    st.divider()
    with proportion_of_international_staff_left:
        st.subheader("Proportion of International Staff")
        fte_staffs = st.number_input("Enter the total no. of FTE staffs at the university:", step=1, value=1, format="%d", key="fte_staffs_input")
        fte_international_staffs = st.number_input("Enter the total no. of FTE International staffs at the university:", step=1, value=0, format="%d", key="fte_international_staffs_input")
        proportion_of_international_staff_score = (100*fte_international_staffs)/fte_staffs
        st.write(f"Proportion of International Staff Score: {proportion_of_international_staff_score}")

    with proportion_of_international_staff_right:
        st.write("### Proportion of International Staff Score ###")

        st.bar_chart({"a: yet to achieve": [100-proportion_of_international_staff_score],
                      "b: achieved": [proportion_of_international_staff_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
        



        
def international_collaboration_section():
    global international_collaboration_score
    # Create two columns layout
    international_collaboration_left, international_collaboration_right = st.columns(2)

    st.divider()
    with international_collaboration_left:
        st.subheader("International Collaboration")
        international_collaboration_score = st.slider("International Collaboration Score", 0.0, 100.0, 0.0)
        st.write(f"International Collaboration Score: {international_collaboration_score}")

    with international_collaboration_right:
        st.write("### International Collaboration Score ###")

        st.bar_chart({"a: yet to achieve": [100-international_collaboration_score],
                      "b: achieved": [international_collaboration_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
        
def main():
    proportion_of_interntaional_students_section()
    proportion_of_international_staff_section()
    international_collaboration_section()
    

    total_international_outlook_score = proportion_of_interntaional_students_score * proportion_of_interntaional_students_weight + proportion_of_international_staff_score * proportion_of_international_staff_weight + international_collaboration_score * international_collaboration_weight

    st.subheader(f"International Outlook Score: {total_international_outlook_score}")
    st.bar_chart({"a: yet to achieve": [100-total_international_outlook_score],
                      "b: achieved": [total_international_outlook_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
    


if __name__ == "__main__":
    main()