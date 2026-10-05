---
title: "15060 Decision Trees Worked Example"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "reading"
module: "Recitation 3: A/B Testing, Regression"
date: "2026-09-23"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6871557"
original: "raw/fall-term-ay-2026-2027/15.060/files/recitations/recitation-3/15060-decision-trees-worked-example.pdf"
locator_kind: "page"
---

## Page 1

DECISION TREES WORKED EXAMPLE

Your “wind forecasting” startup, Airlytics, has built a DMD-powered solution for electric utilities. By deploying your solution, utilities can more accurately forecast next-day energy supply from wind farms and thereby better optimize the mix of energy supply sources to meet demand.

The venture accelerator that provided you seed capital has invited you to participate in their famous “Demo Day” wherein startups come up on stage one after the other and demo their product, while an audience of hundreds of venture capital investors watch. The day after “Demo Day”, the accelerator runs the following process to match startups with the VCs interested in funding them. The process has been designed to secure funding for as many of the accelerator’s startups, as quickly as possible (since “time kills all deals”).

Your demo on “Demo Day” was a resounding success and 3 VC firms want to invest in Airlytics.

- You will get to meet the 3 VCs one after the other for 30 minutes, in random order
- In the allotted 30 minutes, the VC firm will present their “term sheet” (i.e., the financial terms of their investment) and will make their pitch for why they are the best partner for you
- You must immediately accept or reject a firm’s offer before you see the next firm’s offer.
- If you accept a firm’s offer, the process ends for you
- If you reject a firm’s offer, you cannot go back to them later.
- If you reject the first two, you have to accept the third offer.
- The VC firms are all equally likely to make the best offer. a) Draw a decision tree to find the accept/reject strategy that maximizes the probability of choosing

the best offer. b) Summarize the optimal strategy in 1-2 sentences c) If you follow the optimal strategy, what is the probability of choosing the best offer?

Hints:

- A decision node should correspond to whether you accept or reject an offer. Your tree should have three decision nodes.
- You may find it helpful to think of the payoff at the terminal nodes as 1 if the offer you accept is the best one, 0 if not.
- Note that you can compare an offer being presented to earlier offers before you have to decide whether to accept or reject the offer. In particular, this implies that you will never accept a 2nd offer that you know to be worse than the 1st, since that leads to a payoff of 0.
- The probability than an offer is better than another is ½. If the second offer is better than the first one, the probability that it is also better than the third one is 2/3.

1/3

## Page 2

SOLUTION

a) The decision tree for finding the best accept/reject strategy is below.

1/3

b) “Reject the 1st offer. Accept the 2nd offer if it is better than the 1st, otherwise accept the 3rd

offer”. c) If the optimal strategy is followed, the probability of choosing the best offer is 50%. In

contrast to this dynamic strategy, a “static” strategy that always chooses the first, second or the third offer only has a 33% chance of choosing the best offer.

(Completely optional reading: If there are numerous VC firms lined up to meet you, the optimal strategy is to reject the first 37% of offers, then accept the first offer that’s better than any seen so

2/3

## Page 3

far and if none appear, accept the last offer. For an elegant but mathematical proof, see section 2.4 of http://www.statslab.cam.ac.uk/~rrw1/oc/oc2016.pdf).

3/3
