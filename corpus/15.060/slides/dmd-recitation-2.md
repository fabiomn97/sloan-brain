---
title: "DMD Recitation 2"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "slides"
module: "Recitation 2: Simulation"
date: "2026-09-17"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6846967"
original: "raw/fall-term-ay-2026-2027/15.060/files/recitations/recitation-2/dmd-recitation-2.pdf"
locator_kind: "page"
---

## Page 1

DMD Recitation 2 Introduction to the Binomial Distribution + @Risk Walkthrough

DMD Recitation 2

Introduction to the Binomial Distribution + @Risk Walkthrough

## Page 2

Managing Patient Appointments

Managing Patient Appointments

- Consider a physician whose ideal workload is 20 patient appointments per day (the rest of her workday is spent on other clinical and administrative duties).

- Because of high demand, the doctor’s appointment calendar is fully booked several weeks in advance.

- Unfortunately, despite automated appointment reminder texts the day before, a significant proportion of patients (about 25%) fail to show up for their scheduled appointment. This creates two problems:

i. It leads to revenue loss. ii. It takes longer for patients to get an appointment.

- How can analytics help?

## Page 3

The Binomial Distribution

The Binomial Distribution

Setup 1. Consider n “trials” (appointments booked) 2. Each trial results in either “success” or “failure” (“show” or “no show”) 3. Trials are independent of each other (patients do not coordinate with each other)

4. Each trial has same probability of success, p, and of failure, 1 - p (here p = 0.75)

Notation

- X = number of successes in n trials (i.e., number of patients who show up for their appointment)
- We say: The distribution of the random variable X is a Binomial distribution with parameters n and p

- We write: “ X ~ Binomial(n,p) ”. For the patient example, X ~ Binomial(20, 0.75)

## Page 4

Binomial(20, 0.75) Distribution Bar Chart

Binomial(20, 0.75) Distribution Bar Chart

## Page 5

Binomial(20, p) for Various values of p

Binomial(20, p) for Various values of p

## Page 6

Key Probabilities related to the Binomial Distribution

Key Probabilities related to the Binomial Distribution

Suppose that X is distributed Binomial(n, p). There are three typical probability questions.

1. Probability that X is exactly equal to k o Example: Probability that exactly 15 patients show up

2. Probability that X is less than or equal to k o Example: Probability that 15 or fewer patient show up

3. Probability that X is greater than k o Example: Probability that more than 15 patients show up

## Page 7

With Python, these three probabilities can be computed very easily

With Python, these three probabilities can be computed very easily

1. Probability that X is exactly equal to k

= binom.pmf(k,n,p)

2. Probability that X is less than or equal to k

= binom.cdf(k,n,p)

3. Probability that X is greater than k

= 1-binom.cdf(k,n,p)

## Page 8

Computing Binomial Distribution Probabilities in Python

Computing Binomial Distribution Probabilities in Python

To compute the probability that exactly 15 patients show up for their appointment:

binom.pmf(15,20,0.75) # answer: 0.202

You can excute this code in Colab, or give it to Claude to run:

## Page 9

binom.pmf(15, 20, 0.75) ~ 0.202

## Page 10

Computing Binomial Distribution Probabilities in Python

Computing Binomial Distribution Probabilities in Python

To compute the probability that exactly 15 patients show up for their appointment:

binom.pmf(15,20,0.75) # answer: 0.202

To compute the probability that 15 patients or fewer show up for their appointment:

binom.cdf(15,20,0.75) # answer: 0.585

## Page 11

binom.cdf(15, 20, 0.75) ~ 0.585

## Page 12

Computing Binomial Distribution Probabilities in Python

Computing Binomial Distribution Probabilities in Python

To compute the probability that exactly 15 patients show up for their appointment:

binom.pmf(15,20,0.75) # answer: 0.202

To compute the probability that 15 patients or fewer show up for their appointment:

binom.cdf(15,20,0.75) # answer: 0.585

To compute the probability that more than 15 patients show up for their appointment:

1 - binom.cdf(15,20,0.75) # answer: 0.415

## Page 13

1 - binom.cdf(15, 20, 0.75) ~ 0.415

## Page 14

Analyzing the Current Prarctice

Analyzing the Current Prarctice

- What is the probability of operating under capacity? o = Probability of seeing <= 19 patients on a given day o = P(X <= 19) o = binom.cdf(19, 20, 0.75) = 0.997

- What is the probability of seeing exactly 20 patients on a given day?
- = P(X = 20) = binom.pmf(20, 20, 0.75) = 0.003

- You’re operating under capacity 99.7% of the time o Missed revenue opportunity, Longer wait times

## Page 15

@Risk Walkthrough

@Risk Walkthrough

## Page 16

Answers to Key Questions

Answers to Key Questions

Partnership

Monthly analysis

Consulting Full Ownership

Expected earnings [$]

6,667 10,810

7,664


8,544

2,702

Standard deviation of earnings [$]

0%

26.8%

26.8%

Probability of not meeting $5000 threshold

Probability of a loss 0% 9.2% 0%

66.3%

66.3%

Probability of meeting or exceeding consulting salary

33.7% 79.3%

Probability of meeting or exceeding partnership earnings

Based on this information, what would you choose if you were Sanjay?

## Page 17

Answers to Key Questions - ANNUAL

Answers to Key Questions - ANNUAL

Annual analysis

Consulting Full Ownership Partnership

Expected earnings [$]

80,004 130,025 91,585

0 64,115 19,816

Standard deviation of earnings [$]

0% 15% 9.4%

Probability of not meeting $60,000 threshold

Probability of a loss 0% 0.5% 0%

73.9%

71.1%

Probability of meeting or exceeding consulting salary

75.6%

28.9%

Probability of meeting or exceeding partnership earnings
