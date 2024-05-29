import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Research Environment Dashboard", layout="wide")

research_reputation_weight = 0.18
research_income_weight = 0.055
research_productivity_weight = 0.055

research_reputation_score = 0.0
research_income_score = 0.0
research_productivity_score = 0.0

def research_reputation_section():
    global research_reputation_score

    research_reputation_left, research_reputation_right = st.columns(2)

    st.divider()
    with research_reputation_left:
        st.subheader("Research Reputation")
        research_reputation_score = st.slider("Research Reputation Score", 0.0, 100.0, 0.0)
        st.write(f"Research Reputation Score: {research_reputation_score}")

    with research_reputation_right:
        st.write("### Research Reputation Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_reputation_score],
                      "b: achieved": [research_reputation_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])    





def research_income_score_section():
    global research_income_score
    # Create two columns layout
    research_income_score_left, research_income_score_right = st.columns(2)

    st.divider()
    with research_income_score_left:
        st.subheader("Research Income Score")
        research_income = st.number_input("Enter the Research Income to academic staff at the university:", step=1, value=0, format="%d", key="institutional_income_input")
        research_income_score = (100*research_income)/650000.00
        st.write(f"Research Income Score: {research_income_score}")

    with research_income_score_right:
        st.write("### Research Income Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_income_score],
                      "b: achieved": [research_income_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])





def research_productivity_section():
    global research_productivity_score

    research_productivity_left, research_productivity_right = st.columns(2)

    st.divider()
    with research_productivity_left:
        st.subheader("Research Productivity")
        research_productivity_score = st.slider("Research Productivity Score", 0.0, 100.0, 0.0)
        st.write(f"Research Productivity Score: {research_productivity_score}")

    with research_productivity_right:
        st.write("### Research Productivity Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_productivity_score],
                      "b: achieved": [research_productivity_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])    





def main():
    research_reputation_section()
    research_income_score_section()
    research_productivity_section()
    

    total_research_environment_score = research_reputation_score * research_reputation_weight + research_income_score * research_income_weight + research_productivity_score * research_productivity_weight

    st.subheader(f"Research Environment Score: {total_research_environment_score}")
    st.bar_chart({"a: yet to achieve": [100-total_research_environment_score],
                      "b: achieved": [total_research_environment_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


if __name__ == "__main__":
    main()