import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from value_to_score_linear_regression_models import *

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


st.set_page_config(page_title="RANKING DASHBOARD", page_icon="📈", layout="wide")

url = "https://raw.githubusercontent.com/rafsunsheikh/THE_WUR/main/data/wur_score_data/WUR_score_2023.csv"
wur_dataset = pd.read_csv(url)

df = wur_dataset[["Rank", "Overall"]].iloc[:200]

df = df.dropna()

X = df.drop("Rank", axis=1)
y = df["Rank"]

y = y.str.replace(r'\D', '', regex=True).astype(int)

linear_reg = LinearRegression()
linear_reg.fit(X, y)


################################ Pillar Weights ####################################
teaching_weight = 0.295
research_weight = 0.29
citation_weight = 0.30
industry_income_weight = 0.04
international_outlook_weight = 0.075

#################################  Pillar Default Scores ###########################
default_teaching_score = 28.0
default_research_score = 26.9
default_citation_score = 73.0
default_industry_income_score = 62.9
default_international_outlook_score = 79.9

###################################  Pillar Factors Default Values ############################################
default_fte_students = 24363
default_fte_academic_staff = 826
default_doctorate_degree_for_bachelor = 1219
default_academic_staff_with_doctorate = 215
default_total_publication = 6278
default_international_co_author = 2826
default_fte_international_students = 4118
default_fte_international_academic_staff = 322
default_institutional_income_to_academic_staff = 688757
default_research_income_to_academic_staff = 128979
default_industry_income_to_academic_staff = 65614



def teaching_section():
    doctorate_bachelor_awarded_weight = 0.0678
    doctorate_awarded_to_academic_staff_weight = 0.1864
    teaching_reputation_weight = 0.5085
    student_to_academic_staff_rati0_weight = 0.1525
    institutional_income_to_academic_staff_weight = 0.0847

    st.divider()
    
    # st.title("Teaching (29.5%)")
    st.markdown("<h1 style='text-align: center;'> Teaching (29.5%) </h1>", unsafe_allow_html=True)
    st.divider()

    st.subheader("Doctorate to Bachelor Ratio")
    doctorate_students = st.number_input("Enter the no. of students completed their Doctorate at the university:", step=1, value=default_doctorate_degree_for_bachelor, format="%d", key="doctorate_students_key")
    bachelor_students = st.number_input("Enter the no. of students completed their bachelor at the university:", step=1, value=default_fte_students, format="%d", key="bachelor_students_key")
    doctorate_bachelor_awarded_value = doctorate_students / bachelor_students
    st.write(f"Doctorate to Bachelor Ratio Value: {doctorate_bachelor_awarded_value:.2f}")


    doctorate_bachelor_awarded_score = doctorate_student_awarded(doctorate_bachelor_awarded_value)
    st.write(f"Doctorate to Bachelor Ratio Score: {int(doctorate_bachelor_awarded_score)}")
    st.divider()

    st.subheader("Doctorate Awarded to Academic Staff Ratio")
    doctorate_staff = st.number_input("Enter the no. of Academic Staff completed their Doctorate at the university:", step=1, value=default_academic_staff_with_doctorate, format="%d", key="doctorate_staff_key")
    academic_staff = st.number_input("Enter the no. of FTE Academic Staff at the university:", step=1, value=default_fte_academic_staff, format="%d", key = "academic_staff_key")
    doctorate_awarded_to_academic_staff_value = doctorate_staff / academic_staff
    
    st.write(f"Doctorate awarded to Academic Staff Value: {doctorate_awarded_to_academic_staff_value:.2f}")

    doctorate_awarded_to_academic_staff_score = doctorate_awarded_to_academic_staff(doctorate_awarded_to_academic_staff_value)
    st.write(f"Doctorate awarded to Academic Staff Score: {int(doctorate_awarded_to_academic_staff_score)}")
    st.divider()


    st.subheader("Teaching Reputation")
    teaching_value = st.slider("Teaching Reputation Value", 0.0, 100.0, 13.3)
    
    st.write(f"You have selected the Teaching value as {teaching_value}")

    teaching_score = teaching_reputation(teaching_value)
    st.write(f"Teaching Reputation Score: {float(teaching_score):.2f}")
    st.divider()


    st.subheader("Students to Academic Staff Ratio")
    fte_students = st.number_input("Enter the no. of FTE students at the university:", step=1, value=default_fte_students, format="%d", key="fte_students_key")
    fte_academic_staff = st.number_input("Enter the no. of FTE Academic Staff at the university:", step=1, value=default_fte_academic_staff, format="%d", key = "fte_academic_staff_key")
    students_to_academic_staff_value = fte_students / fte_academic_staff
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Students to Academic Staff Ratio Value: {students_to_academic_staff_value:.2f}")

    students_to_academic_staff_score = student_to_academic_staff_ratio(students_to_academic_staff_value)
    st.write(f"Students to Academic Staff Ratio Score: {int(students_to_academic_staff_score)}")
    st.divider()



    st.subheader("Institutional Income to Academic Staff")
    institutional_income_to_academic_staff = st.number_input("Enter the Institutional Income (AUD) to Academic Staff at the university:", step=1, value=default_institutional_income_to_academic_staff, format="%d", key="institutional_income_to_academic_staff_key")
    
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Institutional Income to  Value: {institutional_income_to_academic_staff:.2f} AUD")

    ########## Convert to USD ############
    institutional_income_to_academic_staff = institutional_income_to_academic_staff * 0.63

    institutional_income_to_academic_staff_score = institutional_income_to_academic_staff_model(institutional_income_to_academic_staff)
    st.write(f"Institutional Income to Academic Staff Score: {int(institutional_income_to_academic_staff_score)}")
    st.divider()

    overall_teaching_score = (doctorate_bachelor_awarded_score * doctorate_bachelor_awarded_weight) + (doctorate_awarded_to_academic_staff_score * doctorate_awarded_to_academic_staff_weight) + (teaching_score * teaching_reputation_weight) + (students_to_academic_staff_score * student_to_academic_staff_rati0_weight) + (institutional_income_to_academic_staff_score * institutional_income_to_academic_staff_weight)
    return overall_teaching_score





def research_section():
    publication_per_staff_weight = 0.1897
    research_reputation_weight = 0.6207
    research_income_to_academic_staff_weight = 0.1897
    
    st.divider()
    
    # st.title("Research Environment (29%)")
    st.markdown("<h1 style='text-align: center;'> Research Environment (29%) </h1>", unsafe_allow_html=True)
    st.divider()

    st.subheader("Publication Per Staff")
    total_publication = st.number_input("Enter the no. of total publications at the university:", step=default_total_publication, value=default_total_publication, format="%d", key="total_publication_key")
    academic_staff_for_publication = st.number_input("Enter the no. of FTE academic staff at the university:", step=1, value=default_fte_academic_staff, format="%d", key="academic_staff_for_publication_key")
    publication_per_staff_value = total_publication / academic_staff_for_publication
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Doctorate to Bachelor Ratio value: {publication_per_staff_value:.2f}")

    publication_per_staff_score = publications_per_staff_model(publication_per_staff_value)
    st.write(f"Doctorate to Bachelor Ratio Score: {int(publication_per_staff_score)}")
    st.divider()


    st.subheader("Research Reputation")
    research_reputation_value = st.slider("Research Reputation Value", 0.0, 100.0, 21.5)
    st.write(f"You have selected the Research Reputation Score as {research_reputation_value:.2f}")

    research_reputation_score = research_reputation_model(research_reputation_value)
    st.write(f"Research Reputation Score: {float(research_reputation_score):.2f}")
    st.divider()


    st.subheader("Research Income to Academic Staff")
    research_income_to_academic_staff_value = st.number_input("Enter the research Income (AUD) to Academic Staff at the university:", step=1, value=default_research_income_to_academic_staff, format="%d", key="research_income_to_academic_staff_key")
    
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Research Income to  Value: {research_income_to_academic_staff_value:.2f} AUD")

    ############### Convert to USD ##################
    research_income_to_academic_staff_value = research_income_to_academic_staff_value * 0.63

    research_income_to_academic_staff_score = research_income_to_academic_staff_model(research_income_to_academic_staff_value)
    st.write(f"Research Income to Academic Staff Score: {int(research_income_to_academic_staff_score)}")
    st.divider()

    overall_research_score = (publication_per_staff_score * publication_per_staff_weight) + (research_reputation_score * research_reputation_weight) + (research_income_to_academic_staff_score * research_income_to_academic_staff_weight)
    return overall_research_score



def citation_section():
    citation_weight = 1.00

    st.divider()
    
    # st.title("Research Environment (29%)")
    st.markdown("<h1 style='text-align: center;'> Research Quality (30%) </h1>", unsafe_allow_html=True)
    st.divider()

    st.subheader("Citation")
    citation_score = st.slider("Citation Score", 0.0, 100.0, 73.0)
    st.write(f"You have selected the Citation Score as {citation_score:.2f}")

    st.divider()

    overall_citation_score = citation_score * citation_weight
    return overall_citation_score



def Industry_income_section():
    industry_income_to_academic_staff_weight = 1.00

    st.divider()
    
    # st.title("Research Environment (29%)")
    st.markdown("<h1 style='text-align: center;'> Industry Income to Academic Staff (4%) </h1>", unsafe_allow_html=True)
    st.divider()


    st.subheader("Industry Income to Academic Staff")
    industry_income_to_academic_staff_value = st.number_input("Enter the Industry Income (AUD) to Academic Staff at the university:", step=1, value=default_industry_income_to_academic_staff, format="%d", key="industry_income_to_academic_staff_key")
    
    st.write(f"Industry Income to  Value {industry_income_to_academic_staff_value:.2f} AUD")

    ############### Convert to USD ##################
    industry_income_to_academic_staff_value = industry_income_to_academic_staff_value * 0.63

    industry_income_to_academic_staff_score = industry_income_to_academic_staff_model(industry_income_to_academic_staff_value)
    st.write(f"Industry Income to Academic Staff Score: {int(industry_income_to_academic_staff_score)}")
    st.divider()

    overall_industry_income_score = industry_income_to_academic_staff_score * industry_income_to_academic_staff_weight
    return overall_industry_income_score



def international_outlook_section():
    proportion_of_international_academic_staff_weight = 0.33
    internation_co_authorship_weight = 0.33
    proportion_of_international_students_weight = 0.33

    st.divider()
    
    # st.title("Research Environment (29%)")
    st.markdown("<h1 style='text-align: center;'> International Outlook (7.5%) </h1>", unsafe_allow_html=True)
    st.divider()


    st.subheader("Proportion of International Academic Staff")
    fte_total_academic_staff = st.number_input("Enter the total no. of FTE Academic Staff at the university:", step=1, value=default_fte_academic_staff, format="%d", key="fte_total_academic_staff_key")
    fte_international_academic_staff = st.number_input("Enter the total no. of FTE International academic staff at the university:", step=1, value=default_fte_international_academic_staff, format="%d", key="fte_international_academic_staff_key")
    proportion_of_international_academic_staff_value = (fte_international_academic_staff / fte_total_academic_staff) * 100
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Proportion of International Academic Staff Value: {proportion_of_international_academic_staff_value:.2f}%")

    proportion_of_international_academic_staff_score = proportion_of_international_academic_staff_model(proportion_of_international_academic_staff_value)
    st.write(f"Proportion of International Academic Staff Score: {int(proportion_of_international_academic_staff_score)}")
    st.divider()


    st.subheader("International Co-authorship")
    total_publications = st.number_input("Enter the total no. of publications at the university:", step=1, value=default_total_publication, format="%d", key="total_publications_key")
    total_publications_with_international_co_author = st.number_input("Enter the total no. of publications which have International co-author at the university:", step=1, value=default_international_co_author, format="%d", key="total_publications_with_international_co_author_key")
    proportion_of_international_co_author_value = (total_publications_with_international_co_author / total_publications) * 100
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Proportion of International Co-authorship Value: {proportion_of_international_co_author_value:.2f}%")

    proportion_of_international_co_author_score = proportion_of_international_co_author_model(proportion_of_international_co_author_value)
    st.write(f"Proportion of International Co-authorship Score: {int(proportion_of_international_co_author_score)}")
    st.divider()



    st.subheader("Proportion of International Students")
    fte_total_students = st.number_input("Enter the total no. of FTE Students at the university:", step=1, value=default_fte_students, format="%d", key="fte_total_students_key")
    fte_international_students = st.number_input("Enter the total no. of FTE International students at the university:", step=1, value=default_fte_international_students, format="%d", key="fte_international_students_key")
    proportion_of_international_students_value = (fte_international_students / fte_total_students) * 100
    # if ratio < 0.1:
    #     doctorate_to_bachelor_score = ratio * 1000
    # elif ratio >= 0.1:
    #     doctorate_to_bachelor_score = 100
    st.write(f"Proportion of International Students Value: {proportion_of_international_students_value:.2f}%")

    proportion_of_international_students_score = proportion_of_international_students_model(proportion_of_international_students_value)
    st.write(f"Proportion of International Students Score: {int(proportion_of_international_students_score)}")
    st.divider()

    overall_international_outlook_score = (proportion_of_international_academic_staff_score * proportion_of_international_academic_staff_weight) + (proportion_of_international_co_author_score * internation_co_authorship_weight) + (proportion_of_international_students_score * proportion_of_international_students_weight)
    return overall_international_outlook_score


def overall_rank_model(overall_score):
    
    url_rank = "https://raw.githubusercontent.com/rafsunsheikh/THE_WUR/main/data/wur_score_data/WUR_score_2023.csv"
    wur_dataset = pd.read_csv(url_rank)

    df = wur_dataset[["Rank", "Overall"]].iloc[:200]

    df = df.dropna()

    X = df["Overall"].values.reshape(-1, 1)
    y = df["Rank"].values

    # Use a loop to remove non-numeric characters and convert to integers
    for i in range(len(y)):
        y[i] = int(''.join(filter(str.isdigit, str(y[i]))))


    linear_reg = LinearRegression()
    linear_reg.fit(X, y)

    # Ensure overall_score is a 1D array or a scalar value
    overall_score = np.array([overall_score]).reshape(-1, 1)

    overall_rank = linear_reg.predict(overall_score)
    return overall_rank


def predicted_rank_value_generator(predicted_rank):
    if predicted_rank > 200 and predicted_rank <= 250:
        predicted_rank_value = 200
    elif predicted_rank > 250 and predicted_rank <= 300:
        predicted_rank_value = 250
    elif predicted_rank > 300 and predicted_rank <= 350:
        predicted_rank_value = 300
    elif predicted_rank > 350 and predicted_rank <= 400:
        predicted_rank_value = 350
    else:
        predicted_rank_value = predicted_rank

    return predicted_rank_value


def predicted_custom_label_generator(predicted_rank):
    if predicted_rank > 200 and predicted_rank <= 250:
        predicted_custom_label = '201-250'
    elif predicted_rank > 250 and predicted_rank <= 300:
        predicted_custom_label = '251-300'
    elif predicted_rank > 300 and predicted_rank <= 350:
        predicted_custom_label = '301-350'
    elif predicted_rank > 350 and predicted_rank <= 400:
        predicted_custom_label = '351-400'
    else:
        predicted_custom_label = str(predicted_rank)
    
    return predicted_custom_label



def score_calculate():
    # st.title("Times Higher Education (THE) World University Ranking Predictive Dashboard")
    st.markdown("<h1 style='text-align: center;'> Times Higher Education (THE) World University Ranking Predictive Dashboard </h1>", unsafe_allow_html=True)
    # st.write("### Use the sliders to adjust the scores ###")

    overall_teaching_score = teaching_section()
    overall_research_score = research_section()
    overall_citation_score = citation_section()
    overall_industry_income_score = Industry_income_section()
    overall_international_outlook_score = international_outlook_section()


    overall_present_score = (default_teaching_score * teaching_weight) + (default_research_score * research_weight) + (default_citation_score * citation_weight) + (default_industry_income_score * industry_income_weight) + (default_international_outlook_score * international_outlook_weight)
    overall_predicted_score = (overall_teaching_score * teaching_weight) + (overall_research_score * research_weight) + (overall_citation_score * citation_weight) + (overall_industry_income_score * industry_income_weight) + (overall_international_outlook_score * international_outlook_weight)

    overall_present_rank = overall_rank_model(overall_present_score)
    overall_predicted_rank = overall_rank_model(overall_predicted_score)

    st.markdown("<h1 style='text-align: center;'> THE WUR Rankings </h1>", unsafe_allow_html=True)
    st.divider()

################################### Score Bar Chart (Higher is Better) ##########################################
    score_left_col, score_right_col = st.columns(2)
    with score_left_col:
        present_score_placeholder = st.empty()
        predicted_score_placeholder = st.empty()

    with score_right_col:
        score_right_1, score_right_2 = st.columns(2)
        with score_right_1:
            st.write("(Higher is better)")
            overall_present_score_bar_chart_placeholder = st.empty()
            st.subheader("THE WUR Present Score")

        with score_right_2:
            st.write("(Higher is better)")
            overall_predicted_score_bar_chart_placeholder = st.empty()
            st.subheader("THE WUR Predicted Score")
    st.divider()

################################### Rank Bar Chart (Lower is Better) ##########################################
    rank_left_col, rank_right_col = st.columns(2)
    with rank_left_col:
        present_ranking_placeholder = st.empty()
        predicted_ranking_placeholder = st.empty()
        

    with rank_right_col:
        rank_right_1, rank_right_2 = st.columns(2)
        with rank_right_1:
            st.write("(Lower is better)")
            overall_present_rank_bar_chart_placeholder = st.empty()
            st.subheader("THE WUR Present Ranking")

        with rank_right_2:
            st.write("(Lower is better)")
            overall_predicted_rank_bar_chart_placeholder = st.empty()
            st.subheader("THE WUR Predicted Ranking")
    st.divider()

    # st.subheader(f"Overall Score: {float(overall_score)}")
    # st.subheader(f"Overall Rank: {int(overall_rank)}")



    present_score_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Present Score: {float(overall_present_score):.2f}</h1>", unsafe_allow_html=True)
    predicted_score_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Predicted Score: {float(overall_predicted_score):.2f}</h1>", unsafe_allow_html=True)
    
    
    overall_present_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-float(overall_present_score)],
                      "b: achieved": [float(overall_present_score)]}, use_container_width=False, width=350, height=450, color=["#48ffff", "#ff7648"])


    overall_predicted_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-float(overall_predicted_score)],
                      "b: achieved": [float(overall_predicted_score)]}, use_container_width=False, width=350, height=450, color=["#48ffff", "#ff7648"])


    present_ranking_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Present Ranking Outcome: {int(overall_present_rank)}</h1>", unsafe_allow_html=True)
    predicted_ranking_placeholder.markdown(f"<h3 style='text-align: center;'>THE WUR Predicted Ranking Outcome: {int(overall_predicted_rank)}</h1>", unsafe_allow_html=True)
    
    overall_present_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [500 - int(overall_present_rank)],
                      "b: achieved": [int(overall_present_rank)]}, use_container_width=False, width=350, height=450, color=["#abdd87", "#a075c0"])

    overall_predicted_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [500 - int(overall_predicted_rank)],
                      "b: achieved": [int(overall_predicted_rank)]}, use_container_width=False, width=350, height=450, color=["#abdd87", "#a075c0"])

    ############################################ Line Graph ###########################################################
    # Sample data (you can replace this with your own data)
    st.markdown("<h1 style='text-align: center;'> THE WUR Rankings by Year </h1>", unsafe_allow_html=True)
    st.divider()

    predicted_rank_value = predicted_rank_value_generator(int(overall_predicted_rank))
    predicted_custom_label = predicted_custom_label_generator(int(overall_predicted_rank))
    # Sample data (you can replace this with your own data)
    data = pd.DataFrame({
    'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Value': [250, 200, 250, 300, 300, 250, 250, 200, predicted_rank_value]
    })


        # Create a figure with custom styling
    fig, ax = plt.subplots(figsize=(8, 4))
    # plt.style.use('seaborn-darkgrid')  # Apply a custom style
    sns.set_style('darkgrid')

    # Custom labels for each data point (you can customize these)
    custom_labels = ['251-300', '201-250', '251-300', '301-350', '301-350', '251-300', '251-300', '201-250', f'Predicted \n{predicted_custom_label}']

    # Plot the lines and markers with custom styling and colors
    for i in range(len(data) - 1):
        year_range = (data['Year'][i], data['Year'][i + 1])
        value_range = (data['Value'][i], data['Value'][i + 1])
        color = 'red' if year_range[1] == 2024 else 'blue'
        
        ax.plot(year_range, value_range, marker='o', markersize=8, linestyle='-', linewidth=2, color=color, label=f'Value {year_range[0]}-{year_range[1]}')

    # Annotate the data points with custom labels
    for year, value, label in zip(data['Year'], data['Value'], custom_labels):
        ax.annotate(label, xy=(year, value), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)  # Reduce font size to 8

    # Customize the chart
    ax.set_xlabel('Year', fontsize=10)  # Reduce X-axis label font size to 10
    ax.set_ylabel('Rank', fontsize=10)  # Reduce Y-axis label font size to 10
    # ax.set_title('THE WUR Rankings by Year', fontsize=12)  # Reduce title font size to 12
    ax.tick_params(axis='both', labelsize=8)  # Reduce tick label font size to 8

    # Invert the Y-axis
    ax.invert_yaxis()

    # Add grid lines
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add a legend
    # ax.legend()

    # Display the line chart in Streamlit
    st.pyplot(fig)


def main():
    score_calculate()

if __name__ == "__main__":
    main()
