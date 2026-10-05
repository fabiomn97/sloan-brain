---
title: "15060 Deliverable 3"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "assignment"
date: "2026-09-29"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6893625"
original: "raw/fall-term-ay-2026-2027/15.060/files/deliverables/deliverable-3/15060-deliverable-3.pdf"
locator_kind: "page"
---

## Page 1

DELIVERABLE 3 Due by Monday, October 5th , 11:59 p.m.

Work with your assigned Core Team members only. Each team needs to upload its solutions to Canvas as a single pdf file (any team member can do so through their Canvas account). Make sure that only team members who contributed to the submission are listed on the cover page.

Problem 1 — Basic Calculations (25 points)

a) [5 points] The correlation coefficient between a variable y and a variable x is -0.8. If we build a

simple linear regression model to predict y using x, what is the R-Squared of the model?

b) [5 points] A company's linear regression model has the following actual and predicted values

for sales units. Calculate the Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE) for these predictions. Show your calculations.

Actual Sales Predicted Sales

52 45

60 62

55 50

67 75

c) [5 points] Using 150 data points, an analyst builds a regression model that has an R-squared

value of 0.92. If the SSR of the regression model is 250, what is the standard deviation of the dependent variable? Show your calculations.

d) [5 points] A regression model is built to estimate the effect of advertising spend on sales. The

estimated coefficient for advertising spend is 3, with a 95% confidence interval of [-1, 7]. Should advertising spend be considered significant (at the 95% level) in terms of its impact on sales? Briefly explain.

e) [5 points] A regression model predicts sales of 1000 units for a retail store for next week. The

standard deviation of the “error” term (i.e., the residual standard error) is 560. What is the probability that sales will exceed 2000 units?

## Page 2

Problem 2 — Length of Stay at Mystic Valley Medical Center (25 points)

Mystic Valley Medical Center (MVMC) is a 320-bed community hospital north of Boston. Its Chief Operating Officer, Dana Whitfield, is under pressure to reduce emergency-department boarding. That happens when admitted patients wait in the ED because no inpatient bed is free.

Every morning, the bed-management team must estimate how many beds will free up over the next several days, so it can decide how many elective surgeries to schedule and leave enough room for patients arriving through the ED. Today it assumes every patient stays the unit-wide average. Dana believes that if the team could predict each patient’s length of stay (LOS) from information available at admission, it could forecast discharges day by day. It could then book elective cases on days when beds are expected to open and avoid days when ED patients would otherwise end up boarding.

MVMC’s analytics team pulled a random sample of 2,400 adult inpatient discharges from calendar year 2025 across four service lines. The variables are:

Variable Description

LOS Length of stay, in days (admission to discharge)

Age Patient age in years at admission

Comorbidities Number of chronic conditions recorded at admission (e.g., diabetes, COPD, heart failure)

Emergency 1 if the patient was admitted through the Emergency Department, 0 if the admission was scheduled/elective

Weekend 1 if the patient was admitted on a Saturday or Sunday, 0 otherwise

CaseManager 1 if a nurse case manager was assigned at admission to coordinate the patient’s discharge, 0 otherwise

Diagnosis Service line: Cardiac, General Surgery, Orthopedic, or Respiratory

The team ran a linear regression in Python with LOS as the dependent variable, using the following command:

import statsmodels.formula.api as smf model = smf.ols( "LOS ~ Age + Comorbidities + Emergency + Weekend + CaseManager + C(Diagnosis)", data=df_los).fit() print(model.summary())

## Page 3

The output is in Exhibit A. The residual standard error of the model (i.e., the standard deviation of the error term), (model.mse_resid)**0.5, is 2.06 days. Exhibit B shows the correlation matrix of the numeric variables.

OLS Regression Results ============================================================================== Dep. Variable:                    LOS   R-squared:                       0.321 Model:                            OLS   Adj. R-squared:                  0.319 Method:                 Least Squares   F-statistic:                     141.5 No. Observations:                2400   Prob (F-statistic):          5.01e-195 Df Residuals:                    2391 Df Model:                           8 =================================================================================================== coef    std err          t      P>|t|      [0.025      0.975] --------------------------------------------------------------------------------------------------- Intercept                           2.2709      0.212     10.722      0.000       1.856       2.686 C(Diagnosis)[T.General Surgery]    -0.8861      0.116     -7.665      0.000      -1.113      -0.659 C(Diagnosis)[T.Orthopedic]         -1.1364      0.125     -9.074      0.000      -1.382      -0.891 C(Diagnosis)[T.Respiratory]         0.4700      0.127      3.713      0.000       0.222       0.718 Age                                 0.0261      0.003      8.648      0.000       0.020       0.032 Comorbidities                       0.4205      0.034     12.335      0.000       0.354       0.487 Emergency                           0.9939      0.093     10.712      0.000       0.812       1.176 Weekend                             0.0973      0.094      1.040      0.298      -0.086       0.281 CaseManager                         1.1945      0.095     12.551      0.000       1.008       1.381 =================================================================================================== Exhibit A: Regression Output

LOS Age Comorbidities Emergency Weekend CaseManager

LOS 1.00

Age 0.25 1.00

Comorbidities 0.30 0.32 1.00

Emergency 0.31 −0.04 −0.03 1.00

Weekend 0.02 −0.04 0.00 0.01 1.00

CaseManager 0.32 0.19 0.19 0.11 −0.01 1.00

Exhibit B: Correlation Matrix of Numeric Variables

a) [5 points] Interpret, in plain language, the coefficients on Age, Emergency, and

C(Diagnosis)[T.Orthopedic].

b) [4 points] Which variables, if any, are not statistically significant at the 95% confidence level?

Dana has read about a “weekend effect,” the claim that patients admitted on weekends stay longer because of reduced weekend staffing. What does this model say about that claim for MVMC?

c) [3 points] Based on Exhibit B, is multicollinearity a concern in this model? Identify the most

highly correlated pair of independent variables and explain whether you would drop either of them.

## Page 4

d) [4 points] A 78-year-old patient with 3 comorbidities is admitted through the ED on a Saturday

with a respiratory diagnosis, and a case manager is assigned. Use the model to predict her length of stay. Then provide a 95% confidence interval for your prediction.

e) [6 points] Next month (30 days), the Orthopedic unit expects 150 elective admissions. MVMC

sends emergency orthopedic patients (mostly hip fractures) to a separate trauma unit, so these elective patients are the only ones on the unit. The expected patient mix averages 67 years of age and 1.8 comorbidities; 20% will be admitted on a weekend and 15% will be assigned a case manager. Assume that patients who carry over into or out of the month roughly offset each other.

- Predict the total bed-days these patients will need for the next month, and explain why it’s valid to plug the group averages into the regression equation.

- The unit has 22 staffed beds, and MVMC’s target is to keep occupancy at or below 85%. Will the unit’s expected occupancy for the next month stay under that target? If it is not, what would you recommend to Dana to get it below the target?

f) [3 points] The Chief Medical Officer is skeptical about your analysis in part (e): “This model

explains only about a third of the variation in length of stay. It’s useless for planning.” Try to convince the chief medical officer that even if the model is not highly predictive for an individual patient, it could still be useful for aggregate planning. (HINT: Assuming that LOS predictions for individual patients are independent of each other, then the standard deviation of the total prediction error for N patients is 2.06 √𝑁).

## Page 5

Problem 3 — Predicting Diabetes Disease Progression (25 points)

It is estimated that 450 million people have diabetes worldwide. Diabetes is the 7th leading cause of death globally. The economic cost related to diabetes health expenditure in 2017 was estimated at US$727 billion globally and US$327 billion in the United States alone1.

There are significant benefits when diabetes is treated early. Healthcare professionals need accurate and reliable prediction models to diagnose diabetes and anticipate its progression over time. In this problem you will explore a dataset of diabetes patients containing patient-level demographic and clinical data, and you will use that dataset to develop several predictive models.

(Important note: The purpose of this analysis is simply to gain expertise in the application of analytics models. The purpose is not to draw medical conclusions. It does not replace the recommendations of healthcare providers!)

We will use a small dataset consisting of 442 patients2. A 70% train set sample. labelled diabetes_train.csv, and a 30% test set sample, labelled diabetes_test.csv, are available on Canvas. The dependent variable, y, is a quantitative measure of disease progression one year after baseline (the higher the value the worse the disease progression). The independent variables consist of 9 baseline variables: age, sex (0=female; 1=male), body mass index, average blood pressure and five blood serum measurements.

a) Identify the 4 baseline variables that have the strongest correlation with the dependent

variable in the train set.

b) Examine the correlation matrix among the 9 baseline variables in the train set. Do you see any

signs of multi-collinearity?

c) Construct a linear regression model. Your model should only include significant variables (at

the 95% confidence level). Provide a summary print-out of your model. What is the Rsquared?

d) What is the out-of-sample RMSE?

e) According to your linear regression model, holding everything else constant, do males or

females have the higher rate of disease progression?

1See https://en.wikipedia.org/wiki/Diabetes and the references therein.

2Source: https://web.stanford.edu/~hastie/StatLearnSparsity_files/DATA/diabetes.html (excludes “interaction” variables)

## Page 6

Problem 4 — Predicting the impact of advertising on sales (25 points)

You have been hired by a large consumer-goods firm to quantify the association between advertising and sales of a particular consumer product. The dataset (available in the file ad_spend.csv) consists of last year’s Revenue (in millions of $) for that product in 200 different geographies, along with advertising expenditure (in thousands of $) for the product in each of those markets for three different media: TV, Google Ads, and Facebook Ads.

a) [1 point] Calculate the correlation matrix of all the numeric variables. Are there any collinear

variables?

b) [10 points] Follow the process described in class and construct a linear regression model to

predict Revenue as a function of the other variables. Your model should only include significant variables (at the 95% confidence level). Provide a summary print-out of your model. Also show the confidence intervals for the coefficients.

c) [2 points] What is the % reduction in squared error achieved by this model compared to a

baseline model that uses mean Revenue as the prediction?

d) [2 points] If you had an ad budget of $1000, how would you spend it to maximize the impact

on Revenue? What is the Revenue impact of doing so?

e) [5 points] Now construct a linear regression model to predict Revenue as a function of each of

the independent variables, one by one (i.e., you need to build 3 models). Provide a summary print-out of the three models.

f) [5 points] Are any of the independent variables significant at the 95% level in its model from

(e) but not in the model built in (b)? If yes, identify those variable(s) and provide a plausible explanation for how this could happen i.e., how a variable can be significant in one model but not in another (Hint: use the correlation matrix from (a)).
