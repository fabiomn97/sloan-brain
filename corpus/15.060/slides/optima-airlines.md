---
title: "Optima Airlines"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "slides"
date: "2026-09-25"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6878625"
original: "raw/fall-term-ay-2026-2027/15.060/files/class-material/lecture-7/optima-airlines.pdf"
locator_kind: "page"
---

## Page 1

15.060 Data, Models, and Decisions

OPTIMA AIRLINES*

Introduction

Marion Volero, Flight Operations Manager at Optima Airlines, a contracted regional carrier, did not know what to tell her Chief Operations Officer (COO) Robert Rohan. The Federal Aviation Administration (FAA) had released to the media the August airline flight delay rankings, which showed Optima ranked below their most important client, Quanta Airlines, despite their best efforts to improve turnaround times at airports. Robert had forwarded to Marion the following e-mail from Quanta’s COO Jane Lente:

September 5 Dear Robert:

As you are no doubt aware, the FAA has released its monthly commercial airline flight delay statistics, which show Optima ranked worse than Quanta in percentage of delayed flights for the month of August.  Moreover, Optima’s average flight delay in minutes is significantly greater than that of Quanta. As outlined in your regional carrier service contract, you are required to maintain on-time performance comparable to, if not exceeding, that of Quanta.  Flight delays on Optima flights translate into delays for Quanta customers. Please treat this matter with the utmost urgency to maintain the mutually beneficial relationship Quanta and Optima have shared over the past decade. Warm regards, Jane Lente COO, Quanta Airlines Optima was at risk of losing Quanta as a client unless they could figure out what was causing their poor apparent on-time performance. Optima and Quanta Airlines

Optima, a small regional airline, is a contracted regional carrier for Quanta, a major US airline. In the airline industry, major airlines often contract smaller regional airlines to provide service on short-haul routes.  Optima provides regional jet service between various airports in the northeastern US.  Quanta is Optima’s largest client, accounting for over half of Optima’s revenue.

* This is an adaptation of the case “Flight Delays at RegionEx” by Professors Amr Farahat and Susan Martonosi (INFORMS Transactions on Education, Volume 11, Issue 3). The narrative and data are fictitious. The purpose of the case is to support classroom discussion.

## Page 2

Quanta has been plagued by allegations from the media over the past year that their quality of service, and in particular their flight delay record, is abominable. Although flight delay data reported by the FAA differentiates between flights operated by the major carrier and flights operated by contracted carriers, in the customer’s mind no such distinction is made.  A customer flying from Boston to Orlando via Washington DC who purchases a ticket on Quanta often does not realize that the Boston to Washington DC leg is operated by Optima Airlines and not by Quanta itself.  A delay on that leg that results in a missed connection in Washington DC gets marked in the customer’s mind as a delayed Quanta flight, regardless of how it is counted by the FAA. Quanta relies heavily on regional carriers, over whose flight operations it has no control.  Therefore, Quanta has been putting pressure on its regional carriers, including Optima, to improve their on-time performance or risk losing Quanta as a client. Airline Performance Measures

One aspect of an airline’s quality of service is its on-time performance. Each flight falls into one of four categories: delayed, diverted, canceled or on-time.  The FAA defines a flight to be delayed if it arrives at its scheduled destination 15 or more minutes later than its scheduled arrival time. Flights can also be diverted to another airport, or canceled. A flight that arrives at its scheduled destination within 15 minutes of its scheduled arrival time (that is, a flight that is not delayed, diverted or canceled) is considered on-time. Two commonly used metrics to assess airline performance are the percentage of scheduled flights that were delayed and the percentage of scheduled flights that arrived on-time. Another metric is the average arrival delay, in minutes, of an airline’s flights. Optima’s Network

To simplify the problem, Marion Volero decided to compare Optima’s and Quanta’s performance on the four most important of Optima’s routes:  Boston (BOS) to/from New York (LGA), and Boston (BOS) to/from Washington DC (DCA). Between BOS and LGA, Optima operates three flights in each direction daily, while Quanta operates only one. Between BOS and DCA, both carriers operate one flight in each direction daily. The Data

Marion needed to take a quick look at some data before her afternoon meeting with COO Rohan.  She downloaded the publicly available August flight statistics from the FAA website and cleaned the data, focusing only on the four main routes and the essential quantities. An excerpt and description of the data is provided in the Appendix. Marion is sitting in her office examining the spreadsheet, wondering whether the flight delay rankings as reported in the news tell the whole story.

## Page 3

Appendix: Description of the data Below are the first five rows of the case data set.  Each row corresponds to a flight flown by one of the two airlines in the four-airport network described above.

Des0na0on

Departure

Arrival delay

Day of

Route

Airline Origin airport

airport

date

Scheduled departure 0me

Scheduled arrival 0me

Actual arrival 0me

in minutes

Delay indicator

Week

Code

Number of passengers Quanta DCA BOS 8/1/2018 6:35 8:15 8:07 -8 0 5 4 Op9ma BOS LGA 8/1/2018 7:45 9:00 9:08 8 0 4 1 166 Op9ma LGA BOS 8/1/2018 9:10 10:25 10:49 24 1 4 2 224 Op9ma LGA BOS 8/1/2018 13:10 14:25 14:44 19 1 4 2 217 Quanta BOS LGA 8/1/2018 13:35 15:00 15:31 31 1 4 1

Airline: This column contains “Optima” if the flight was flown by Optima, and “Quanta” if it was flown by Quanta Airlines.

Origin airport: This is the official airline code for the origin of the flight.

Destination airport: This is the official airline code for the destination of the flight.

Departure date: The date on which the flight departed.  All flights took place during the month of August.

Scheduled departure time: This is the time at which the flight was scheduled to depart its origin airport, on a 24-hour clock (e.g. 6:10 = 6:10 AM, and 18:10 = 6:10 PM).  All flights in this data set occur in the same time zone.  There are no overnight flights in this data set.

Scheduled arrival time: This is the time at which the flight was scheduled to arrive at its destination airport.

Actual arrival time: This is the time at which the flight actually arrived at its destination airport, unless it is marked “Canceled” or “Diverted”.

Arrival delay in minutes: This is the difference between the actual arrival time and scheduled arrival time. Negative delays correspond to flights arriving earlier than scheduled.  Canceled or diverted flights are assigned the value “N\A” in this field.

Delay indicator: This assigns a value of 1 to any flight with an arrival delay of at least 15 minutes, and 0 to flights with an arrival delay less than 15 minutes.  Canceled or diverted flights are assigned the value “N\A” in this field.

Day of week: This provides the day of the week corresponding to the flight date. 1 = Sunday, 2 = Monday, …, 7 = Saturday.

Route code: This is a code corresponding to each flight’s Origin/Destination pair. 1 = BOS/LGA, 2 = LGA/BOS, 3 = BOS/DCA, 4 = DCA/BOS.

Number of passengers: For Optima flights only, the number of passengers on each flight is provided.
