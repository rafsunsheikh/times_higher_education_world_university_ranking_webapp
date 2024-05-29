import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Research Environment Dashboard", layout="wide")

citation_impact_weight = 0.15
research_strength_weight = 0.05
research_excellence_weight = 0.05
research_influence_weight = 0.05

citation_impact_score = 0.0
research_strength_score = 0.0
research_excellence_score = 0.0
research_influence_score = 0.0

def citation_impact_section():
    global citation_impact_score

    citation_impact_left, citation_impact_right = st.columns(2)

    st.divider()
    with citation_impact_left:
        st.subheader("Citation Impact")
        citation_impact_score = st.slider("Citation Impact Score", 0.0, 100.0, 0.0)
        st.write(f"Citation Impact Score: {citation_impact_score}")

    with citation_impact_right:
        st.write("### Citation Impact Score ###")

        st.bar_chart({"a: yet to achieve": [100-citation_impact_score],
                      "b: achieved": [citation_impact_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])    





def research_strength_section():
    global research_strength_score
    # Create two columns layout
    research_strength_left, research_strength_right = st.columns(2)

    st.divider()
    with research_strength_left:
        st.subheader("Research Strength")
        research_strength_score = st.slider("Research Strength Score", 0.0, 100.0, 0.0)
        st.write(f"Research Strength Score: {research_strength_score}")

    with research_strength_right:
        st.write("### Research Strength Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_strength_score],
                      "b: achieved": [research_strength_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])



def research_excellence_section():
    global research_excellence_score
    # Create two columns layout
    research_excellence_left, research_excellence_right = st.columns(2)

    st.divider()
    with research_excellence_left:
        st.subheader("Research excellence")
        research_excellence_score = st.slider("Research excellence Score", 0.0, 100.0, 0.0)
        st.write(f"Research excellence Score: {research_excellence_score}")

    with research_excellence_right:
        st.write("### Research excellence Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_excellence_score],
                      "b: achieved": [research_excellence_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])



def research_influence_section():
    global research_influence_score
    # Create two columns layout
    research_influence_left, research_influence_right = st.columns(2)

    st.divider()
    with research_influence_left:
        st.subheader("Research influence")
        research_influence_score = st.slider("Research Influence Score", 0.0, 100.0, 0.0)
        st.write(f"Research Influence Score: {research_influence_score}")

    with research_influence_right:
        st.write("### Research Influence Score ###")

        st.bar_chart({"a: yet to achieve": [100-research_influence_score],
                      "b: achieved": [research_influence_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])






def main():
    citation_impact_section()  
    research_strength_section()
    research_excellence_section()
    research_influence_section()

    total_research_quality_score = citation_impact_score * citation_impact_weight + research_strength_score * research_strength_weight + research_excellence_score * research_excellence_weight + research_influence_score * research_influence_weight

    st.subheader(f"Research Quality Score: {total_research_quality_score}")
    st.bar_chart({"a: yet to achieve": [100-total_research_quality_score],
                      "b: achieved": [total_research_quality_score]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])


if __name__ == "__main__":
    main()