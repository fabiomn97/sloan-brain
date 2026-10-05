---
title: "Deliverable 2"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "assignment"
date: "2026-09-22"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6863987"
original: "raw/fall-term-ay-2026-2027/15.060/files/deliverables/deliverable-2/deliverable-2.pdf"
locator_kind: "page"
---

## Page 1

MIT Sloan School of Management

15.060: Data, Models, and Decisions – Fall 2026

Podimata, Ramakrishnan, Yao

DELIVERABLE 2

Due by Monday, September 28th, 11:59 p.m.

Work with your assigned Core Team members only. Each team needs to upload its solutions to Canvas as a single PDF file (any team member can do so through their Canvas account). Make sure that only team members who contributed to the submission are listed on the cover page.

Problem 1 (25 points)

Harbor Air (Airline A) and Empire Shuttle (Airline B) fly the same 7:00am Boston (BOS) to New York (LGA) route each day. Airline A has 20 seats and currently books 22 passengers. Airline B has 30 seats and currently books 34. Assume both airlines sell all their bookings every day on this popular route.

Passengers on Airline A show up independently with probability 0.85 while passengers on Airline B show up independently with probability 0.80.

Both airlines collect $400 per booking. If the flight is overbooked, every bumped passenger is refunded their $400 and then paid another $600 in cash compensation by the airline. This is $600 is deducted from the airline’s total revenue.

a) [3 points] Write down a Python expression for the probability that Airline A will bump at least 1

passenger. Write down the same for Airline B. b) [3 points] What is the expected number of passengers who are bumped for Airline A? Show your

work, including any Python expressions used to compute probabilities. Do the same for Airline B. c) [3 points] Compute the expected revenue for both airlines under their current overbooking

policies.

To reduce the cost of bumped passengers, the two airlines have negotiated a seat-sharing agreement: if one airline is oversold and the other has empty seats, overflow passengers are walked down the hall and seated on the partner flight. Assume that passengers moved to the other airline do

1/5

## Page 2

not receive any bumped compensation and that their fare is always paid to the airline that they booked with.

d) [10 points] Using @Risk, create a simulation model with cells for the following quantities:

- Number of passengers who arrive for Airline A
- Number of passengers who arrive for Airline B
- Number of bumped passengers for Airline A (i.e., passengers in excess of 20)
- Number of bumped passengers for Airline B (i.e., passengers in excess of 30)
- Number of empty seats available on Airline A
- Number of empty seats available on Airline B
- Number of bumped Airline A’s passengers who are accommodated on Airline B
- Number of bumped Airline B’s passengers who are accommodated on Airline A
- Number of bumped Airline A’s passengers given compensation
- Number of bumped Airline B’s passengers given compensation

Run the simulation model for 1000 iterations. Please submit your @Risk spreadsheet to Canvas along with your PDF. What is the expected revenue for Airline A and Airline B respectively under the seat-sharing agreement? How does it compare to your response from c)? Explain intuitively what the managerial takeaway is.

e) [6 points] In what proportion of days is at least 1 passenger flowing from Airline A to Airline B? In

what proportion of days is at least 1 passenger flowing from Airline B to Airline A? Which airline is benefiting more from this seat-sharing agreement?

2/5

## Page 3

Problem 2 (35 points)

Sanjay (of Gentle Lentil fame) has done more market research on the strength of the Harvard Square restaurant market and discovered that the random variable Meals is dependent on the random variable Price in an interesting way: When the market is stronger, more people tend to dine out (implying a higher value for Meals) AND are willing to pay more for a meal (implying that a higher Price can be charged for each meal). In other words, Price and Meals are positively correlated.

The details of this relationship are specified in the table below. At each Price, Meals is still a Normal random variable but its mean changes as the Price changes. For example, if the Price for a month is (say) $16.50, the Meals for that month will be normally distributed with mean 2500 and SD 750.

Market Strength Probability Price Meals

Very  Healthy 0.25 20.00 Normal(4000, 1000)

Healthy 0.35 18.50 Normal(3000, 800)

Not So Healthy 0.30 16.50 Normal(2500, 750)

Unhealthy 0.10 15.00 Normal(1500, 500)

(Note that the probabilities above are unchanged from the case)

Modify the “Simulation Model” tab of the Gentle Lentil spreadsheet from Recitation to incorporate this change, simulate 10,000 trials using @Risk, and answer the questions below (Note: @Risk may run for 30-45 minutes). Please submit your new spreadsheet on Canvas.

a) [10 points] Include a screenshot of the @Risk output histogram for the “Full Ownership” option .

b) [2 points] Using the chart in (a), determine in what % of months Sanjay will experience a loss.

c) [8 points] In the “Full Ownership” scenario discussed in class, Sanjay experiences a loss in 9.2% of

months. Compare this number to the number in (b). If they are significantly different, offer a brief explanation.

d) [10 points] Include a screenshot of the @Risk output histogram for the Partnership option.

e) [5 points] Using the chart in (d), answer these questions:

- In what % of months will Sanjay be unable to meet his $5000 payment obligation?

- In what % of months will he earn more than his consulting salary?

3/5

## Page 4

Problem 3 (20 points)

Presidential Candidate X needs to decide on where to spend her time campaigning during the final week of the election campaign and has one of two choices: either to campaign in Ohio (OH) or to campaign in Florida (FL), but not in both. A candidate needs at least 270 electoral votes to win the election1. If she wins Ohio then she wins 18 electoral votes. If she wins Florida then she wins 29 electoral votes. The chances of her winning each of these States depend not only on where she will campaign during the last week but also on where her competitor, Candidate Y, will campaign. We have the following scenarios:

0.6 0.2

Scenario Probability Candidate X wins FL Probability Candidate X wins OH X campaigns in FL and Y campaigns in FL

1 0

X campaigns in FL and Y campaigns in OH

0 1

X campaigns in OH and Y campaigns in FL

0.6 0.8

X campaigns in OH and Y campaigns in OH

Currently, there is a 60% chance that Candidate Y campaigns in Florida and a 40% chance that he campaigns in Ohio. Candidate X’s campaign manager has rudimentary knowledge of decision trees and suggests that Candidate X selects the decision that maximizes the expected number of electoral votes she wins in both of these states.

a) [10 points] Draw a suitable decision tree of the problem faced by Candidate X, clearly indicating

all probabilities and payoffs.

b) [8 points] Fold back the tree. According to the campaign manager’s objective, where should

Candidate X spend her campaign time?

c) [2 points] Is maximizing expected number of electoral votes in these two states the right

objective?

1 For a description of electoral votes, see: https://www.archives.gov/electoral-college/about or https://en.wikipedia.org/wiki/United_States_Electoral_College

4/5

## Page 5

Problem 4 (20 points)

20 years after graduating from MIT Sloan, you are an accomplished (and wealthy) businessperson who has decided to become an angel for aspiring entrepreneurs. A Sloanie (class of 2046) has approached you with a new idea, and you would like to decide whether or not to invest in the venture.

Based on past experience with similar ventures, there is a 25% chance that it is “gold” (a worthwhile venture that will yield a profit), and there is a 75% chance that it is a “lemon” (a failure that will incur losses). If you invest in a gold venture, then you will profit about $8M. However, if, unfortunately, you invest in a lemon venture, then you will incur a loss of $4/3M (one and a third million dollars).

You can decide whether to invest or not right away, or you can first run a due diligence analysis (DDA) and then decide whether to invest or not.  The DDA is 100% accurate: it reliably indicates whether a venture is “gold” or “lemon,” but it costs $3M.

a) [15 points] Draw a decision tree and find the best course of action to maximize your expected

profit

b) [5 points] What is the maximum price you are willing to pay for the DDA?

5/5
