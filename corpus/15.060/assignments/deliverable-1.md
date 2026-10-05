---
title: "Deliverable 1"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "assignment"
date: "2026-09-15"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6835457"
original: "raw/fall-term-ay-2026-2027/15.060/files/deliverables/deliverable-1/deliverable-1.pdf"
locator_kind: "page"
---

## Page 1

MIT Sloan School of Management

15.060: Data, Models, and Decisions – Fall 2026

Podimata, Ramakrishnan, Yao

DELIVERABLE 1

Due by Monday, September 21st, 11:59 p.m.

Work with your assigned Core Team members only. Each team needs to upload its solutions to Canvas as a single PDF file (any team member can do so through their Canvas account). Make sure that only team members who contributed to the submission are listed on the cover page.

Problem 1 (30 points): Day passes at The Foundry

The Foundry is a co-working space in Kendall Square with 30 hot desks. It sells exactly 30 monthly memberships (one per desk), so every member is guaranteed a desk on any business day. Not every member comes in every day, however. Over the past 250 business days, The Foundry has recorded the number of members who badged in each day. The data is in coworking_showups.csv.

Dataset description: Each row in the dataset corresponds to one business day. The columns have the following definitions: date: the date (business days only; The Foundry is closed on weekends) day_of_week: the day of the week members_showed_up: the number of members (out of 30) who badged in that day

Because desks often sit empty, management is considering selling day passes to non-members. Under the proposed policy, every morning at 8:00 a.m. The Foundry sells k day passes at $35 each. (There is a long waitlist of people who want day passes, so all k passes always sell.) Day-pass holders arrive at 8:00 a.m. and each takes a desk, leaving 30 − k desks for members. Members arrive later in the morning. If more than 30 − k members show up, the extra members are “bumped”: they are sent to a partner co-working space across the street, which costs The Foundry $120 per bumped member (the partner’s fee plus an estimated goodwill cost).

a) (4 Points) Using Python, plot the empirical distribution (histogram) of the daily number of

members who showed up, and report the mean, the standard deviation, the median, and the 90th percentile. Based on the data, what is the probability that all 30 desks are occupied on a given day? What is the probability that at least 5 desks are empty? b) (6 Points) Suppose The Foundry sells k = 3 one-day passes. Using the empirical distribution

from part (a), compute by hand the expected number of bumped members per day. Repeat for k = 4. Management’s initial policy is that, on average, no more than 1 member should be bumped every 10 business days. What is the largest number of day passes that satisfies this policy?

1/6

## Page 2

c) (8 Points) Now let’s take profit into account. The expected daily profit from the day-pass

program is

Profit(k) = 35 × k − 120 × (expected number of bumped members per day).

Using Python, compute Profit(k) for k = 0, 1, …, 10 and find the k that maximizes it. For that k, report the expected daily profit, the expected number of bumped members per day, and the probability that at least one member is bumped on a given day.

d) (3 Points) The general manager argues: “The average number of members who show up is

about 24. So if we sell 6 day passes, we still have 24 desks for members, and on average nobody gets bumped.” Is there something wrong with the manager’s argument? Please explain briefly using numbers from the data. Would you sell 6 day passes, financially speaking? e) (5 Points) The Foundry’s data analyst suspects that attendance is different on Fridays. Using

Python, compute the average number of members who showed up on each day of the week. Is she right?

She proposes a day-specific policy: sell kFri passes on Fridays and kMTWT passes on Monday through Thursday. Find the profit-maximizing kFri and kMTWT (evaluate each on the corresponding subset of the data), and compute how much more expected profit per year (250 business days) the day-specific policy generates compared to the single-k policy of part (c).

f) (4 Points) For each of the following three proposals, state whether the historical data in

coworkingshowups.csv alone is enough to estimate the proposal’s expected daily profit, and explain why or why not in 2–3 sentences. (You do not need to compute anything.)

o The partner space raises its fee, so that each bumped member now costs The Foundry

$150 instead of $120. o The Foundry keeps its 30 desks but sells 5 additional memberships, for a total of 35

members, and continues to sell k day passes every morning. o Members must reserve a desk through an app by 7:00 a.m.; at 8:00 a.m., every desk

that was not reserved is sold as a day pass.

2/6

## Page 3

Problem 2 (30 points): Optimizing Checkout Recommendations

A large online retailer D.M.D is looking to redesign its checkout experience to increase sales. A natural way to boost revenue at checkout is to recommend additional products that may go well with the products you are already about to purchase. The team has two ideas on how to do this:

- Variant A: Ask an LLM to generate complementary products to those in your cart. Although highly personalized, this is slow and introduces additional latency that some customers may not want to wait for.
- Variant B: Show popular products from categories that are frequently co-purchased with the items in the user’s cart. The suggestions are more generic, but they render instantly.

The status quo right now is that there’s nothing on the cart page at all. The historical benchmark for revenue per visitor is $18.28.

In the past 10 days, D.M.D experimented with Variant A and Variant B on a total of 5,000 visitors and recorded each visitor's revenue for that session. For this experiment, a user is assigned to Variant A or B upon arriving to the site and their revenue is recorded. Hence, a user who never reaches the checkout page will still be included in the analysis even though they never experienced Variant A or B.

Here is a summary of the results of the experiment.

Variant A Variant B Total Visitors 2500 2500 Mean revenue per visitor $22.47 $21.30 Standard deviation $28.28 $28.12

a) (6 points) Construct a 95% confidence interval for the mean revenue per visitor under each

variant. Report the margin of error for each. b) (2 points) Is there evidence at the 95% confidence level that Variant A beats the $18.28 status

quo? What about for Variant B? c) (8 Points) Construct a 95% confidence interval for the difference in mean revenue, A − B. Can

you conclude which variant is better?

You decide from (c) that more data is needed. Each day, you can experiment with 500 more visitors, 250 in each group. Assume the mean and standard deviation of revenues from each variant stay the same as you collect more data, and that you always allocate traffic evenly to A and B.

d) (6 Points) How many more days will you have to run this experiment before you see a

statistically significant difference between the two groups at the 95% confidence level?

3/6

## Page 4

Sadly, the VP of Growth says that he cannot wait so long. As you are reviewing your data, you suddenly have a realization: many visitors do not see the checkout page at all, yet they were included in your earlier analysis. You quickly pull the data from the 5000 visitors and see that:

- Variant A: 1180 out of 2500 (47.2%) saw the checkout page
- Variant B: 1210 out of 2500 (48.4%) saw the checkout page

Anyone who did not see the checkout page has a revenue of $0.

Variant A Variant B Visitors who saw checkout 1180 1210 Mean revenue per visitor $47.61 $44.01 Standard deviation $22.29 $25.19

e) (8 Points) Using this information, please recompute your answer from (c) using only visitors

who saw the checkout page. Summarize your takeaways from this exercise.

4/6

## Page 5

Problem 3 (15 points): Confidence Intervals for Proportions

In class, we calculated confidence intervals for an unknown mean of a population, but a common related use case is to calculate confidence intervals for a proportion within the population. For example, we may want to estimate the proportion of shoppers who reach the checkout page in Problem 2. A proportion is simply a special case of the average where the values are 0 (i.e., don’t reach the checkout page) or 1 (reached the checkout page).

For example, the below data shows whether each of the 5000 users reached the checkout page. The Reached Checkout column is 1 if the user does and 0 otherwise.

User ID Variant Group Revenue Reached Checkout 1 A $5.80 1 2 B $12.87 1 3 B $0.00 0 … … … 5000 A $0.00 0

We’d like to validate that the proportion of users who see the checkout page is approximately the same across users assigned to Variant A or B.

Since the variant is only shown after the user reaches the checkout screen, the proportion of users who see the checkout page should be about the same in each variant. Currently, the proportion is 47.2% for Variant A and 48.4% for variant B.

Variant A Variant B

Total visitors assigned to this variant 2500 2500 Number who reached checkout page 1180 1210 Proportion who reached checkout page 47.2% 48.4%

You’d like to confirm that there is no significant difference at the 95% level between these two groups—otherwise there might be an issue with the experiment setup (Think of this as an A/A test that we discussed in lecture).

a) (5 points) For group A, what is the mean and standard deviation of the “Reached Checkout”

column? Feel free to use Excel or an AI tool to answer this question. You do not need the dataset itself. Do the same for group B. b) (10 points) Construct a 95% confidence interval for the difference in the means of the

“reached checkout” column (i.e., proportion of users who checked out). Validate that there is no significant difference at the 95% level between the proportion of users who reached checkout.

5/6

## Page 6

Problem 4 (25 points): Power Experiments

You are working on a new ranking algorithm for a short-form video platform. Under the current algorithm, the number of minutes users spend on the platform per day has the following statistics:

- Mean: 37.2 mins
- Standard Deviation: 12.5 mins

You’d like to size an experiment for a new ranking algorithm that you expect will increase time spent by 2 minutes

(a) (6 points) Approximately how many samples are needed to detect this increase in time spent

with 80% power* and 5% significance? (b) (8 points) Run an experiment using Claude that validates your answer from (a) indeed has a

power of about 80%. You may assume that the distribution of time spent is Normal under both ranking algorithms, and that the new algorithm achieves exactly 2 more minutes of time spent on average with no change in standard deviation. Show the prompt and the results. Ask Claude to run an experiment rather than use any formulas. What is Claude’s estimate of the power of this experiment? (c) (8 points) Ask Claude to generate a plot of how the power of the experiment changes for

various sample size N from N = 100 to N = 2000. Show that plot and provide an interpretation. Again, ask Claude to perform an experiment instead of using formulas. If you wanted to achieve a power of 90%, approximately how many samples would you need? (d) (3 points) Is it possible to achieve a power of 100%? Why or why not?

* Recall that the power of a test is the probability that it can correctly detect the presence of a given effect.

6/6
