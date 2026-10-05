---
title: "[Please Read Carefully] Assignment 1 Grades & Feedback Released."
course: "15.761"
course_name: "Introduction to Operations Management"
term: "Fall Term (AY 2026-2027)"
type: "announcement"
date: "2026-09-29"
source: "canvas"
url: "https://canvas.mit.edu/courses/38556/discussion_topics/449648"
original: "raw/fall-term-ay-2026-2027/15.761/announcements/2026-09-29-please-read-carefully-assignment-1-grades-feedback-released.html"
locator_kind: "section"
---

*Posted 2026-09-29 by Natasha Patnaik*

Hi Everyone,

I am about to post the grades & feedback from the JetBlue Assignment last week. I have left comments on each individual submission - please review, so you can learn from the feedback. How to interpret the grades:

- Score 95+ = excellent performance, solid understanding of the concepts
- Score 90-95 = good performance, a few minor misconceptions that you should try to clarify for yourself
- Score 85-89 = good performance, at least one major misconception that you should review
- Score 80-84 = a mix of misconceptions, you should pinpoint where the issue is and try to correct it (good opportunities for this are Friday recitations and office hours)
- Score 79 or below = some fundamental misunderstandings, you should pinpoint where the issue is and try to correct it (good opportunities for this are Friday recitations and office hours)

Some common mistakes and comments across the submissions:

- **(Question 2a and 2b).** For questions about the average number of planes (i.e. - average queue length) or the average wait time of a plane in the system, it is important that EVERY plane's wait be taken as a datapoint when computing that average. Since delays extent beyond the 18 hours of standard operation, you need to use the full 19 hours in which there is ever a plane in the system. In a similar issue, some people tried to take these averages by dividing over the full 24 hours of a day. This is also incorrect, because we should not be considering "dead time" when a system is not operating or staffed. The analogy I gave in office hours was for a sandwich shop that is open from 9AM - 5PM, maybe with delays until 5:30PM sometimes. Would you average over the full 24 hours, even when the shop is closed? No - because no sandwiches are being produced at nighttime, and no employees or staff are operating. It's similar reasoning here for this case study, dividing by 24 deflates all the numbers artificially.
- **(Questions 2b and 2c).** Some of you had the really great insight about the "discrepancy" between wait time when calculated via Little's Law vs using the excel sheet to analyze on an individual plane-by-plane basis. This is because Little's Law gives a quick average-based estimate from just L and λ (throughput), while Excel tracks each plane's actual wait exactly. But Little's Law is still useful because it requires far less data and effort, and generalizes to situations where you don't have (or can't build) a full schedule (as is the case in many business contexts outside of airline industry).
- **(Questions 2c).** This was the question most people lost points on. Although you can compute the maximal waiting time by looking at every flight in excel independently, which will result in 3.25 hours. Although this is acceptable reasoning, we want you to use Little's Law and get comfortable with using system-level analysis to get these kinds of answers (think about settings where you don't have a historical log of perfect data).

 So the correct solution is:

Max queue length = 14 planes (max value in column L, including the 4 planes beginning de-icing)

Service rate = 4 planes/hr

Max wait time = 14 planes/(4 planes/hr) = 3.5 hours

- **(Question 4). The build-up diagram underestimates the anticipated delays because** we’ve assumed “departure times are kept with certainty and the deicing time is deterministic”. But there are many sources of unpredictable variability that are not captured, which can only exacerbate delays even further - mechanical errors, bad weather conditions causing additional delay, flight crew timeouts, etc.
