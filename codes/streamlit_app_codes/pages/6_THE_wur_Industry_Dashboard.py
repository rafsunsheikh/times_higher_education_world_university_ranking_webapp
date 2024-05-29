import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Industry Dashboard", layout="wide")


industry_income_weight = 0.02
patents_weight = 0.02

industry_income_score = 0.0
patents_score = 0.0


def industry_income_section():
    global industry_income_score

    industry_income_left, industry_income_right = st.columns(2)

    st.divider()
    with industry_income_left:
        st.subheader("Industry Income")
        industry_income = st.number_input("Enter the Industry Income to academic staff at the university:", step=1, value=0, format="%d", key="institutional_income_input")
        industry_income_score = (100*industry_income)/650000.00
        st.write(f"Industry Income Score: {industry_income_score}")

    with industry_income_right:
        st.write("### Industry Income Score ###")

        st.bar_chart({"a: yet to achieve": [100-industry_income_score],
                      "b: achieved": [industry_income_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


def patents_section():
    global patents_score
    # Create two columns layout
    patents_left, patents_right = st.columns(2)

    st.divider()
    with patents_left:
        st.subheader("Patents")
        patents_score = st.slider("Patents Score", 0.0, 100.0, 0.0)
        st.write(f"Patents Score: {patents_score}")

    with patents_right:
        st.write("### Patents Score ###")

        st.bar_chart({"a: yet to achieve": [100-patents_score],
                      "b: achieved": [patents_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
        
def main():
    industry_income_section()
    patents_section()
    

    total_industry_score = industry_income_score * industry_income_weight + patents_score * patents_weight

    st.subheader(f"Industry Score: {total_industry_score}")
    st.bar_chart({"a: yet to achieve": [100-total_industry_score],
                      "b: achieved": [total_industry_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
    



if __name__ == "__main__":
    main()