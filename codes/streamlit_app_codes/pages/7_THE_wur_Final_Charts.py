import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Charts", layout="wide")

url = "https://raw.githubusercontent.com/rafsunsheikh/THE_WUR/main/data/wur_score_data/WUR_score_2023.csv?token=GHSAT0AAAAAACJQPQKW4JJOK5RAQTYBQ6GAZKTLMRQ"
wur_dataset = pd.read_csv(url)

df = wur_dataset[["Rank", "Overall"]].iloc[:200]

df = df.dropna()

X = df.drop("Rank", axis=1)
y = df["Rank"]

y = y.str.replace(r'\D', '', regex=True).astype(int)

linear_reg = LinearRegression()
linear_reg.fit(X, y)


################################## Teaching ##########################################
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
        fte_students = st.number_input("Enter the no. of FTE students at the university:", step=1, value=1, format="%d", key="fte_students_input")
        fte_staffs = st.number_input("Enter the no. of FTE academic staffs at the university:", step=1, value=0, format="%d", key="fte_staffs_input")
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
        doctorate_students = st.number_input("Enter the no. of students completed their Doctorate at the university:", step=1, value=0, format="%d", key="doctorate_students_input")
        bachelor_students = st.number_input("Enter the no. of students completed their bachelor at the university:", step=1, value=1, format="%d", key="bachelor_students_input")
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
        doctorate_students = st.number_input("Enter the no. of students completed their Doctorate at the university:", step=1, value=0, format="%d", key="doctorate_staff_input")
        fte_staff = st.number_input("Enter the no. of FTE Academic Staffs at the university:", step=1, value=1, format="%d", key="fte_staff_input")
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



################################## Research ##########################################
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
        research_income = st.number_input("Enter the Research Income to academic staff at the university:", step=1, value=0, format="%d", key="research_income_input")
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

################################## International Outlook ##########################################
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
        fte_students = st.number_input("Enter the total no. of FTE students at the university:", step=1, value=1, format="%d", key="fte_students_input_2")
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
        fte_staffs = st.number_input("Enter the total no. of FTE staffs at the university:", step=1, value=1, format="%d", key="fte_staffs_input_2")
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
   
################################## Research Quality ##########################################
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

################################## Industry ##########################################
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
        industry_income = st.number_input("Enter the Industry Income to academic staff at the university:", step=1, value=0, format="%d", key= "industry_income_input")
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
    
################################## Main ##########################################
def main():
    st.title("THE WUR Rankings")
    st.divider()

    left_col, right_col = st.columns(2)
    with left_col:
        ranking_placeholder = st.empty()
        score_placeholder = st.empty()

    with right_col:
        right_1, right_2 = st.columns(2)
        with right_1:
            st.write("(Lower is better)")
            overall_rank_bar_chart_placeholder = st.empty()
            st.write("THE WUR Ranking")

        with right_2:
            st.write("(Higher is better)")
            overall_score_bar_chart_placeholder = st.empty()
            st.write("THE WUR Score")
    st.divider()


    st.subheader("THE WUR Rankings Factors")
    col_1, col_2, col_3, col_4, col_5, = st.columns(5)
    with col_1:
        
        right_1_bar_chart_placeholder = st.empty()
        st.write("Teaching (29.5%)")
    with col_2:
        
        right_2_bar_chart_placeholder = st.empty()
        st.write("Research Environment (29%)")
    with col_3:
        
        right_3_bar_chart_placeholder = st.empty()
        st.write("Research Quality (30%)")
    with col_4:
        
        right_4_bar_chart_placeholder = st.empty()
        st.write("International Outlook (7.5%)")
    with col_5:
        
        right_5_bar_chart_placeholder = st.empty()
        st.write("Industry (4%)")

    st.divider()


    st.title("Teaching")
    teaching_reputation_section()
    staff_to_student_ratio_section()
    doctorate_to_bachelor_ratio_section()
    doctorate_to_staff_ratio_section()
    institutional_income_score_section()

    total_teaching_score = teaching_reputation_score * teaching_reputation_weight + staff_to_student_ratio_score * staff_to_student_ratio_weight + doctorate_to_bachelor_score * doctorate_to_bachelor_weight + doctorate_to_staff_score * doctorate_to_staff_weight + institutional_income_score * institutional_income_weight
    total_teaching_score_scaled_up = (total_teaching_score * 100.00) / 29.5 
    st.subheader(f"Teaching Score: {total_teaching_score_scaled_up:.2f}")
    st.bar_chart({"a: yet to achieve": [100-total_teaching_score_scaled_up], 
                      "b: achieved": [total_teaching_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])

    right_1_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_teaching_score_scaled_up],
                        "b: achieved": [total_teaching_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#a7d967", "#9967d9"])
    
    st.divider()


    st.title("Research Environment")
    research_reputation_section()
    research_income_score_section()
    research_productivity_section()
    

    total_research_environment_score = research_reputation_score * research_reputation_weight + research_income_score * research_income_weight + research_productivity_score * research_productivity_weight
    total_research_environment_score_scaled_up = (total_research_environment_score * 100.00) / 29.0
    st.subheader(f"Research Environment Score: {total_research_environment_score_scaled_up:.2f}")
    st.bar_chart({"a: yet to achieve": [100-total_research_environment_score_scaled_up],
                      "b: achieved": [total_research_environment_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])

    right_2_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_research_environment_score_scaled_up],
                        "b: achieved": [total_research_environment_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#a7d967", "#9967d9"])
    st.divider()



    st.title("Research Quality")
    citation_impact_section()  
    research_strength_section()
    research_excellence_section()
    research_influence_section()

    total_research_quality_score = citation_impact_score * citation_impact_weight + research_strength_score * research_strength_weight + research_excellence_score * research_excellence_weight + research_influence_score * research_influence_weight
    total_research_quality_score_scaled_up = (total_research_quality_score * 100.00) / 30.0

    st.subheader(f"Research Quality Score: {total_research_quality_score_scaled_up:.2f}")
    st.bar_chart({"a: yet to achieve": [100-total_research_quality_score_scaled_up],
                      "b: achieved": [total_research_quality_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
    
    right_3_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_research_quality_score_scaled_up],
                        "b: achieved": [total_research_quality_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#a7d967", "#9967d9"])
    
    st.divider()


    st.title("International Outlook")
    proportion_of_interntaional_students_section()
    proportion_of_international_staff_section()
    international_collaboration_section()
    

    total_international_outlook_score = proportion_of_interntaional_students_score * proportion_of_interntaional_students_weight + proportion_of_international_staff_score * proportion_of_international_staff_weight + international_collaboration_score * international_collaboration_weight
    total_international_outlook_score_scaled_up = (total_international_outlook_score * 100.00) / 7.5

    st.subheader(f"International Outlook Score: {total_international_outlook_score_scaled_up:.2f}")
    st.bar_chart({"a: yet to achieve": [100-total_international_outlook_score_scaled_up],
                      "b: achieved": [total_international_outlook_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
    
    right_4_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_international_outlook_score_scaled_up],
                        "b: achieved": [total_international_outlook_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#a7d967", "#9967d9"])
    
    st.divider()


    st.title("Industry")
    industry_income_section()
    patents_section()
    

    total_industry_score = industry_income_score * industry_income_weight + patents_score * patents_weight
    total_industry_score_scaled_up = (total_industry_score * 100.00) / 4.0
    st.subheader(f"Industry Score: {total_industry_score_scaled_up:.2f}")
    st.bar_chart({"a: yet to achieve": [100-total_industry_score_scaled_up],
                      "b: achieved": [total_industry_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#48ffff", "#ff7648"])
    
    right_5_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_industry_score_scaled_up],
                        "b: achieved": [total_industry_score_scaled_up]}, use_container_width=False, width = 250, height=500, color=["#a7d967", "#9967d9"])
    st.divider()

    final_score = total_teaching_score + total_research_environment_score + total_research_quality_score + total_international_outlook_score + total_industry_score
    score_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Ranking Score: {final_score:.2f}</h1>", unsafe_allow_html=True)

    overall_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-final_score],
                      "b: achieved": [final_score]}, use_container_width=False, width=350, height=450, color=["#48ffff", "#ff7648"])


    pred = np.array([[final_score]])
    rank = linear_reg.predict(pred)

    ranking_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Ranking Outcome: {int(rank)}</h1>", unsafe_allow_html=True)
    overall_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [500 - int(rank)],
                      "b: achieved": [int(rank)]}, use_container_width=False, width=350, height=450, color=["#abdd87", "#a075c0"])



if __name__ == "__main__":
    main()