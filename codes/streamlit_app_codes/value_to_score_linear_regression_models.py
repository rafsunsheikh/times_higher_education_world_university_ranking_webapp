import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

url_metric_scores = "https://raw.githubusercontent.com/rafsunsheikh/THE_WUR/main/Metric_Results/2022-10-13_wur_metrics_2023/metric%20scores.csv"
url_metric_values = "https://raw.githubusercontent.com/rafsunsheikh/THE_WUR/main/Metric_Results/2022-10-13_wur_metrics_2023/metric%20values.csv"

df_metric_scores = pd.read_csv(url_metric_scores)
df_metric_values = pd. read_csv(url_metric_values)




df_doctorate_student_awarded = pd.DataFrame({'values': df_metric_values['Doctorate \nBachelor Awarded'].iloc[:27], 'scores': df_metric_scores['Doctorate Bachelor Awarded'].iloc[:27]})
df_doctorate_awarded_to_academic_staff = pd.DataFrame({'values': df_metric_values['Doctorate awarded \nto academic staff'].iloc[:27], 'scores': df_metric_scores['Doctorate awarded to academic staff'].iloc[:27]})
df_teaching_reputation = pd.DataFrame({'values': df_metric_values['Teaching \nreputation'].iloc[:27], 'scores': df_metric_scores['Teaching reputation'].iloc[:27]})
df_institutional_income_to_academic_staff = pd.DataFrame({'values': df_metric_values['Institutional income \nto academic staff'].iloc[:27], 'scores': df_metric_scores['Institutional income to academic staff'].iloc[:27]})
df_student_to_academic_staff_ratio = pd.DataFrame({'values': df_metric_values['Students to \nacademic staff ratio'].iloc[:27], 'scores': df_metric_scores['Students to academic staff ratio'].iloc[:27]})
df_publications_per_staff = pd.DataFrame({'values': df_metric_values['Publications per staff'].iloc[:27], 'scores': df_metric_scores['Publications per staff'].iloc[:27]})
df_research_income_to_academic_staff = pd.DataFrame({'values': df_metric_values['Research income \nto academic staff'].iloc[:27], 'scores': df_metric_scores['Research income to academic staff'].iloc[:27]})
df_research_reputation = pd.DataFrame({'values': df_metric_values['Research \nreputation'].iloc[:27], 'scores': df_metric_scores['Research reputation'].iloc[:27]})
df_industry_income_to_academic_staff = pd.DataFrame({'values': df_metric_values['Industry income \nto academic staff'].iloc[:27], 'scores': df_metric_scores['Industry income to academic staff'].iloc[:27]})
df_proportion_of_international_academic_staff = pd.DataFrame({'values': df_metric_values['Proportion of international \nacademic staff'].iloc[:27], 'scores': df_metric_scores['Proportion of international academic staff'].iloc[:27]})
df_international_co_authroship = pd.DataFrame({'values': df_metric_values['International \nco-authorship'].iloc[:27], 'scores': df_metric_scores['International co-authorship'].iloc[:27]})
df_proportion_of_international_students = pd.DataFrame({'values': df_metric_values['Proportion of \ninternational students'].iloc[:27], 'scores': df_metric_scores['Proportion of international students'].iloc[:27]})



# Remove the percentage sign and convert to float
df_proportion_of_international_academic_staff['values'] = df_proportion_of_international_academic_staff['values'].str.rstrip('%').astype(float)
df_international_co_authroship['values'] = df_international_co_authroship['values'].str.rstrip('%').astype(float)
df_proportion_of_international_students['values'] = df_proportion_of_international_students['values'].str.rstrip('%').astype(float)



def doctorate_awarded_to_academic_staff(value):
    # Extract the x and y values for regression
    X_doctorate_awarded_to_academic_staff = df_doctorate_awarded_to_academic_staff['values'].values.reshape(-1, 1)
    y_doctorate_awarded_to_academic_staff = df_doctorate_awarded_to_academic_staff['scores'].values

    degree = 4
    poly_features_doctorate_awarded_to_academic_staff = PolynomialFeatures(degree=degree)
    X_poly_doctorate_awarded_to_academic_staff = poly_features_doctorate_awarded_to_academic_staff.fit_transform(X_doctorate_awarded_to_academic_staff)

    # Fit a linear regression model
    poly_regression_model_doctorate_awarded_to_academic_staff= LinearRegression()
    poly_regression_model_doctorate_awarded_to_academic_staff.fit(X_poly_doctorate_awarded_to_academic_staff, y_doctorate_awarded_to_academic_staff)
    
    
    poly_pred_doctorate_awarded_to_academic_staff = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_doctorate_awarded_to_academic_staff = poly_features_doctorate_awarded_to_academic_staff.transform(poly_pred_doctorate_awarded_to_academic_staff)
    predicted_y_poly_doctorate_awarded_to_academic_staff = poly_regression_model_doctorate_awarded_to_academic_staff.predict(new_data_poly_doctorate_awarded_to_academic_staff)

    return predicted_y_poly_doctorate_awarded_to_academic_staff


def doctorate_student_awarded(value):
    # Extract the x and y values for regression
    X_doctorate_student_awarded = df_doctorate_student_awarded['values'].values.reshape(-1, 1)
    y_doctorate_student_awarded = df_doctorate_student_awarded['scores'].values

    degree = 2
    poly_features_doctorate_in_respect_to_bachelor = PolynomialFeatures(degree=degree)
    X_poly_doctorate_in_respect_to_bachelor = poly_features_doctorate_in_respect_to_bachelor.fit_transform(X_doctorate_student_awarded)

    # Fit a linear regression model
    poly_regression_model_doctorate_in_respect_to_bachelor = LinearRegression()
    poly_regression_model_doctorate_in_respect_to_bachelor.fit(X_poly_doctorate_in_respect_to_bachelor, y_doctorate_student_awarded)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_doctorate_in_respect_to_bachelor = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_doctorate_in_respect_to_bachelor = poly_features_doctorate_in_respect_to_bachelor.transform(poly_pred_doctorate_in_respect_to_bachelor)
    predicted_y_poly_doctorate_in_respect_to_bachelor = poly_regression_model_doctorate_in_respect_to_bachelor.predict(new_data_poly_doctorate_in_respect_to_bachelor)

    return predicted_y_poly_doctorate_in_respect_to_bachelor
    

    
def teaching_reputation(value):
    # Extract the x and y values for regression
    X_teaching_reputation = df_teaching_reputation['values'].values.reshape(-1, 1)
    y_teaching_reputation = df_teaching_reputation['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 2
    poly_features_teaching_reputation = PolynomialFeatures(degree=degree)
    X_poly_teaching_reputation = poly_features_teaching_reputation.fit_transform(X_teaching_reputation)

    # Fit a linear regression model
    poly_regression_model_teaching_reputation = LinearRegression()
    poly_regression_model_teaching_reputation.fit(X_poly_teaching_reputation, y_teaching_reputation)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_teaching_reputation = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_teaching_reputation = poly_features_teaching_reputation.transform(poly_pred_teaching_reputation)
    predicted_y_poly_teaching_reputation = poly_regression_model_teaching_reputation.predict(new_data_poly_teaching_reputation)

    return predicted_y_poly_teaching_reputation

def institutional_income_to_academic_staff_model(value):
    # Extract the x and y values for regression
    X_institutional_income_to_academic_staff = df_institutional_income_to_academic_staff['values'].values.reshape(-1, 1)
    y_institutional_income_to_academic_staff = df_institutional_income_to_academic_staff['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 4
    poly_features_institutional_income_to_academic_staff = PolynomialFeatures(degree=degree)
    X_poly_institutional_income_to_academic_staff = poly_features_institutional_income_to_academic_staff.fit_transform(X_institutional_income_to_academic_staff)

    # Fit a linear regression model
    poly_regression_model_institutional_income_to_academic_staff = LinearRegression()
    poly_regression_model_institutional_income_to_academic_staff.fit(X_poly_institutional_income_to_academic_staff, y_institutional_income_to_academic_staff)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_institutional_income_to_academic_staff = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_institutional_income_to_academic_staff = poly_features_institutional_income_to_academic_staff.transform(poly_pred_institutional_income_to_academic_staff)
    predicted_y_poly_institutional_income_to_academic_staff = poly_regression_model_institutional_income_to_academic_staff.predict(new_data_poly_institutional_income_to_academic_staff)

    return predicted_y_poly_institutional_income_to_academic_staff

def student_to_academic_staff_ratio(value):
    # Extract the x and y values for regression
    X_student_to_academic_staff_ratio = df_student_to_academic_staff_ratio['values'].values.reshape(-1, 1)
    y_student_to_academic_staff_ratio = df_student_to_academic_staff_ratio['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 4
    poly_features_students_to_academic_staff_ratio = PolynomialFeatures(degree=degree)
    X_poly_students_to_academic_staff_ratio = poly_features_students_to_academic_staff_ratio.fit_transform(X_student_to_academic_staff_ratio)

    # Fit a linear regression model
    poly_regression_model_students_to_academic_staff_ratio = LinearRegression()
    poly_regression_model_students_to_academic_staff_ratio.fit(X_poly_students_to_academic_staff_ratio, y_student_to_academic_staff_ratio)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_students_to_academic_staff_ratio = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_students_to_academic_staff_ratio = poly_features_students_to_academic_staff_ratio.transform(poly_pred_students_to_academic_staff_ratio)
    predicted_y_poly_students_to_academic_staff_ratio = poly_regression_model_students_to_academic_staff_ratio.predict(new_data_poly_students_to_academic_staff_ratio)

    return predicted_y_poly_students_to_academic_staff_ratio

def publications_per_staff_model(value):
    # Extract the x and y values for regression
    X_publications_per_staff = df_publications_per_staff['values'].values.reshape(-1, 1)
    y_publications_per_staff = df_publications_per_staff['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 2
    poly_features_publication_per_staff = PolynomialFeatures(degree=degree)
    X_poly_publication_per_staff = poly_features_publication_per_staff.fit_transform(X_publications_per_staff)

    # Fit a linear regression model
    poly_regression_model_publication_per_staff = LinearRegression()
    poly_regression_model_publication_per_staff.fit(X_poly_publication_per_staff, y_publications_per_staff)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_publication_per_staff = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_publication_per_staff = poly_features_publication_per_staff.transform(poly_pred_publication_per_staff)
    predicted_y_poly_publication_per_staff = poly_regression_model_publication_per_staff.predict(new_data_poly_publication_per_staff)

    return predicted_y_poly_publication_per_staff

def research_income_to_academic_staff_model(value):
    # Extract the x and y values for regression
    X_research_income_to_academic_staff = df_research_income_to_academic_staff['values'].values.reshape(-1, 1)
    y_research_income_to_academic_staff = df_research_income_to_academic_staff['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 2
    poly_features_research_income_to_academic_staff = PolynomialFeatures(degree=degree)
    X_poly_research_income_to_academic_staff = poly_features_research_income_to_academic_staff.fit_transform(X_research_income_to_academic_staff)

    # Fit a linear regression model
    poly_regression_model_research_income_to_academic_staff = LinearRegression()
    poly_regression_model_research_income_to_academic_staff.fit(X_poly_research_income_to_academic_staff, y_research_income_to_academic_staff)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_research_income_to_academic_staff = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_research_income_to_academic_staff = poly_features_research_income_to_academic_staff.transform(poly_pred_research_income_to_academic_staff)
    predicted_y_poly_research_income_to_academic_staff = poly_regression_model_research_income_to_academic_staff.predict(new_data_poly_research_income_to_academic_staff)

    return predicted_y_poly_research_income_to_academic_staff

def research_reputation_model(value):
    # Extract the x and y values for regression
    X_research_reputation = df_research_reputation['values'].values.reshape(-1, 1)
    y_research_reputation = df_research_reputation['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 2
    poly_features_research_reputation = PolynomialFeatures(degree=degree)
    X_poly_research_reputation = poly_features_research_reputation.fit_transform(X_research_reputation)

    # Fit a linear regression model
    poly_regression_model_research_reputation = LinearRegression()
    poly_regression_model_research_reputation.fit(X_poly_research_reputation, y_research_reputation)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_research_reputation = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_research_reputation = poly_features_research_reputation.transform(poly_pred_research_reputation)
    predicted_y_poly_research_reputation = poly_regression_model_research_reputation.predict(new_data_poly_research_reputation)

    return predicted_y_poly_research_reputation

def industry_income_to_academic_staff_model(value):
    # Extract the x and y values for regression
    X_industry_income_to_academic_staff = df_industry_income_to_academic_staff['values'].values.reshape(-1, 1)
    y_industry_income_to_academic_staff = df_industry_income_to_academic_staff['scores'].values

    # Fit a linear regression model
    regression_model_industry_income_to_academic_staff = LinearRegression()
    regression_model_industry_income_to_academic_staff.fit(X_industry_income_to_academic_staff, y_industry_income_to_academic_staff)

    pred_industry_income_to_academic_staff = np.array([[value]])
    score_industry_income_to_academic_staff = regression_model_industry_income_to_academic_staff.predict(pred_industry_income_to_academic_staff)

    return score_industry_income_to_academic_staff

def proportion_of_international_academic_staff_model(value):
    # Extract the x and y values for regression
    X_proportion_of_international_academic_staff = df_proportion_of_international_academic_staff['values'].values.reshape(-1, 1)
    y_proportion_of_international_academic_staff = df_proportion_of_international_academic_staff['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 3
    poly_features_proportion_of_international_academic_staff = PolynomialFeatures(degree=degree)
    X_poly_proportion_of_international_academic_staff = poly_features_proportion_of_international_academic_staff.fit_transform(X_proportion_of_international_academic_staff)

    # Fit a linear regression model
    poly_regression_model_proportion_of_international_academic_staff = LinearRegression()
    poly_regression_model_proportion_of_international_academic_staff.fit(X_poly_proportion_of_international_academic_staff, y_proportion_of_international_academic_staff)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_proportion_of_international_academic_staff = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_proportion_of_international_academic_staff = poly_features_proportion_of_international_academic_staff.transform(poly_pred_proportion_of_international_academic_staff)
    predicted_y_poly_proportion_of_international_academic_staff = poly_regression_model_proportion_of_international_academic_staff.predict(new_data_poly_proportion_of_international_academic_staff)

    return predicted_y_poly_proportion_of_international_academic_staff

def proportion_of_international_co_author_model(value):
    # Extract the x and y values for regression
    X_international_co_authroship = df_international_co_authroship['values'].values.reshape(-1, 1)
    y_international_co_authroship = df_international_co_authroship['scores'].values

    # Fit a linear regression model
    regression_model_international_co_authroship = LinearRegression()
    regression_model_international_co_authroship.fit(X_international_co_authroship, y_international_co_authroship)

    pred_international_co_authroship = np.array([[value]])
    score_international_co_authroship = regression_model_international_co_authroship.predict(pred_international_co_authroship)

    return score_international_co_authroship

def proportion_of_international_students_model(value):
    # Extract the x and y values for regression
    X_proportion_of_international_students = df_proportion_of_international_students['values'].values.reshape(-1, 1)
    y_proportion_of_international_students = df_proportion_of_international_students['scores'].values

    ######################################################################### Fit a Polynomial regression model ###############################################################################
    degree = 3
    poly_features_proportion_of_internationa_students = PolynomialFeatures(degree=degree)
    X_poly_proportion_of_internationa_students = poly_features_proportion_of_internationa_students.fit_transform(X_proportion_of_international_students)

    # Fit a linear regression model
    poly_regression_model_proportion_of_internationa_students = LinearRegression()
    poly_regression_model_proportion_of_internationa_students.fit(X_poly_proportion_of_internationa_students, y_proportion_of_international_students)

    ########################################### Predict Single Scores Polynomial Regression #########################################################
    poly_pred_proportion_of_internationa_students = np.array([[value]])  # Replace x_value with the value for which you want to predict y
    new_data_poly_proportion_of_internationa_students = poly_features_proportion_of_internationa_students.transform(poly_pred_proportion_of_internationa_students)
    predicted_y_poly_proportion_of_internationa_students = poly_regression_model_proportion_of_internationa_students.predict(new_data_poly_proportion_of_internationa_students)

    return predicted_y_poly_proportion_of_internationa_students




