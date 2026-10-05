---
title: "Python Cheatsheet"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "reading"
date: "2026-09-11"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6821744"
original: "raw/fall-term-ay-2026-2027/15.060/files/software/python-cheatsheet.pdf"
locator_kind: "page"
---

## Page 1

Python Cheatsheet

v1.0 - Created cheatsheet - June 18, 2025 - Rama Ramakrishnan

v2.0 - Section 12 added - June 30, 2025 - Evan Yao

v3.0 - Multiple changes to sections 2 through 11 - August 22, 2025 - Rama Ramakrishnan

v4.0 - Fixed statsmodels issue - September 22, 2025 - Rama Ramakrishnan

1  Standard Setup

This should be the ﬁrst cell of your Colab.

import pandas as pd                    # for data manipulation import statsmodels.formula.api as smf  # for linear regression and logistic regression from scipy.stats import norm, binom    # for probability calculations

2  Create a dataframe from a CSV and get familiar with it


Read in CSV flights = pd.read_csv("optima_quanta.csv")

Basic stats for numeric columns flights.describe()

Basic stats for categorical columns flights.describe(include='object')

First few rows flights.head()

Last few rows flights.tail()

5 random rows flights.sample(5)

Spreadsheet‑like view flights

Correlation between all numerical columns flights.corr(numeric_only=True)

3  Work with a single column of the dataframe


Access a particular column flights["arrival_delay_minutes"]

col = flights["arrival_delay_minutes"]

col.mean()

Calculate mean / median / sd for a particular column

col.median()

col.std()

Summary / quantiles for a particular column col.describe()

col.quantile([0.25,0.5,0.75])

Histogram (for a numeric column) col.plot.hist()

## Page 2

Bar chart (for a categorical column) col.plot.bar()

4  Create new columns or delete existing columns

# Create new columns # If you want to create just one new column flights['not_on_time'] = flights['delayed'] + flights['cancelled'] + flights['diverted']

# If you want to create multiple new columns in one shot flights = flights.assign( padded_delay_minutes = flights["arrival_delay_minutes"] - 10, not_on_time = flights["diverted"] + flights["cancelled"] + flights["delayed"] )

# Delete two columns and save as a new dataframe flights2 = flights.drop(columns=["padded_delay_minutes", "not_on_time"])

5  Select only certain columns or rows

# Select columns flights[["airline","origin","destination","depart_date"]]

# Select columns and save as a new dataframe flights2 = flights[["airline","origin","destination","depart_date"]]

# Selection shortcut if the columns are contiguous flights.loc[:, "airline":"depart_date"]

# Select rows that satisfy certain filters flights.query("not_on_time == 1 and airline == 'Optima'")

6  Sort a dataframe

flights.sort_values(['airline', 'origin'])

# Save sorted copy in a new dataframe flights_sorted = flights.sort_values(['airline', 'origin'])

# Sort in ascending order on one column and # in descending order on the second column flights.sort_values(["airline","arrival_delay_minutes"],ascending=[True, False])

## Page 3

7  Summarize/slice-and-dice (pivot-table style)

# compute the fraction not on time BY airline flights.groupby('airline')['not_on_time'].mean()

# compute the fraction delayed BY route AND airline flights.groupby(['route_code', 'airline'])['delayed'].mean()

8  Probabilities

# Normal(μ=200, σ=100) norm.cdf(500,200,100)          # P(X ≤ 500) 1 - norm.cdf(500,200,100)      # P(X > 500) norm.ppf(0.98,200,100)         # 98th percentile

# Binomial(n=25, p=0.7) binom.cdf(20,25,0.7)           # P(X ≤ 20) 1 - binom.cdf(20,25,0.7)       # P(X > 20) binom.pmf(20,25,0.7)           # P(X = 20)

9  Linear regression (Blue Bikes example)

# Dependent variable:rentals # Independent variables: temp, rel_humidity model = smf.ols("rentals ~ temp + rel_humidity", data=df).fit() print(model.summary())

# Dependent variable:rentals # Independent variables: temp, rel_humidity, day_of_week, hour # Note that day_of_week and hour are categorical variables model = smf.ols("rentals ~ temp + rel_humidity + C(day_of_week) + C(hour)", data=df).fit() print(model.summary())

# Use the model to generate predictions preds = model.predict(df)

10  Split data into train / test

df_test = df.sample(frac=0.3, random_state=123) df_train = df.drop(df_test.index)

11  Logistic regression & confusion matrix (Loan

## Page 4

Defaults)

# default ~ inquiries + installment model = smf.logit("default ~ inquiries + installment", data=df_train).fit() model.summary()

# Use the model to generate probability predictions probs = model.predict(df_test)

# Use a cutoff to transform probabilities to class labels cutoff = 0.5 df_test = df_test.assign(predicted = (probs > cutoff) * 1)

# Calculate the confusion matrix cm = pd.crosstab(df_test["default"], df_test["predicted"])

# Extract values TP = cm.at[1, 1] FP = cm.at[0, 1] FN = cm.at[1, 0] TN = cm.at[0, 0]

# Compute metrics accuracy = (TP + TN) / (TP + FP + FN + TN) tpr = TP / (TP + FN) fpr = FP / (FP + TN)

12 Optional: Plotting and Visualizations

This is where Gemini can really help you out. You are not expected to understand how the code for generating plots works. However, you are expected to read the plot and ensure that the LLM is correct. If your prompt is not speciﬁc enough, the LLM may generate code for that plot that is not what you want.

Import the library for plotting

import matplotlib.pyplot as plt

Useful commands:


Scatter Plot plt.scatter(x, y)
