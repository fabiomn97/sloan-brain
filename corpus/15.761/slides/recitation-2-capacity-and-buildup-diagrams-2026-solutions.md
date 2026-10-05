---
title: "Recitation 2 - Capacity and Buildup Diagrams - 2026 Solutions"
course: "15.761"
course_name: "Introduction to Operations Management"
term: "Fall Term (AY 2026-2027)"
type: "slides"
module: "Recitations"
date: "2026-09-15"
source: "canvas"
url: "https://canvas.mit.edu/courses/38556/files/6837796"
original: "raw/fall-term-ay-2026-2027/15.761/files/recitation-2-capacity-and-buildup-diagrams-2026-solutions.pdf"
locator_kind: "page"
---

## Page 1

Capacity & Buildup

Diagrams

Recitation September 18, 2026

## Page 2

Congestion Analysis

Customers or

Finished

jobs arrive

work

server, machine

or service facility

waiting area / inventory

System Performance = F( System Parameters )

l Arrival rate µ Service rate per server

L Inventory level/Queue size/Line length W Waiting time

## Page 3

Congestion Analysis Tools

Build-Up Diagrams

- Predictable Variability

- Build-up rate l(t) - µ(t) > 0 o.k.

- Short Run Analysis

- Variable rates o.k.

- Assumes workflow is continuous and deterministic

## Page 4

How buildup works:

Step 3 – Reducing Inventory

Step 1 – Starting Point – No Inventory

Step 2 – Building up Inventory

1 gal / minute 5 gal / second





















09:00 09:05 09:10 09:14 0

09:00 09:05 09:10 09:14

09:00 09:05 09:10 09:14

## Page 5

From discrete to continuous

Buildup diagram:

How to get the Buildup diagram from the airplane maintenance schedule?

Plane ID Time In Time out 124 9:00 9:20 354 9:05 9:25 859 9:10 9:30 698 9:15 9:35 256 9:20 9:40 123 9:25 9:45 253 9:30 9:50

1) Mark down each time an element enters or leaves

Time State Increment in Queue Queue 9:00 In 1 1 9:05 In 1 2 9:10 In 1 3 9:15 In 1 4 9:20 Out -1 3 9:20 In 1 4 9:25 In 1 5 9:25 Out -1 4 9:30 Out -1 3 9:30 In 1 4 9:35 Out -1 3 9:40 Out -1 2 9:45 Out -1 1 9:50 Out -1 0

the system

2) Reorder the time steps chronologically. The

queue increases each time an element enters the

system and decreases each time an element leaves

the system

3) Get the Queue size in discrete times, then over

the period of interest

## Page 6

Inventory Buildup Diagram:

Airline Check-In Problem

Part a)

The check-in counter of an airline can service 6 people/ minute. Assume that 1 person arrived per minute between 9:00 and 9:15. At 9:15, a bus with 40 people all arrived at once. Then, from 9:15 until 9:30, 8 people arrived per minute. From 9:30 until 9:50, 4 people arrived per minute. No one arrived after 9:50 AM.

Please draw the queue buildup diagram for this scenario. What is the average number of people waiting in line from 9 to 9:55?

## Page 7

Inventory Buildup Diagram:

Airline Check-In Problem

Service rate = 6 ppl/min

Queue

Buildup rate = -2 ppl/min

Buildup rate = 2 ppl/min

Buildup rate = -6 ppl/min

Instantaneous arrival of 40 ppl

## Page 8

Inventory Buildup Diagram:

Airline Check-In Problem

Q: What is the average # of people waiting in line from 9 to 9:55?

Queue

Total queue volume = 0.5*(40+70)*15 + 0.5*(70+30)*20+0.5*30*5 = 1900 ppl*min

Area under the curve = Total queue volume over the entire duration

Average # of people waiting = Average queue volume = Total queue volume/Total time = 1900/55  =  34.5 ppl

## Page 9

Inventory Buildup Diagram:

Limited Queue Length

Part b)

-  What’s the average waiting time for the system?
- When does the maximum Waiting Time occur?

## Page 10

Use Little’s Law

- 50 new MBA’s/Year x 2 Years MBA = 100 students in Sloan

Average number of individuals/items

System throughput l

in system L

Average time spent in system W

- Conservation of Flow (equilibrium):

W = L / λ L = l x W

## Page 11

Inventory Buildup Diagram:

Airline Check-In Problem

Average Wait = Average #

Queue

people/ Average Throughput Rate Average # people = total

area under curve / time = 34.5 Average Throughput Rate

= (1*15 + 6*40)/55 = 4.64 customers/min

Average Wait = 34.5 / 4.64

= 7.44 minutes

Max. WT: at peak (not

always!) Wait time=70/6

## Page 12

Inventory Buildup Diagram:

Limited Queue Length

Part c)

The airline now caps the number of people who can wait in line at 30 (by offering a special check in process to all people beyond a certain point in line).

Draw the inventory buildup diagram for this scenario. What is the average number of people waiting in line between 9am and 9.55am?

## Page 13

Airline Check-In Problem

Limited Queue Length

Total queue volume = 30*15 + 0.5*15*30 = 675 ppl*min

Queue

Average queue length = 675/55 = 12.3 ppl

Buildup rate = 0 ppl/min (reach max. capacity of the queue)

Buildup rate = -2 ppl/min

Instantaneous arrival of 40 ppl But only 30 are kept

## Page 14

Airline Check-in Problem – Limited Queue Length (v2)

Part d)

The airline removes the cap, but instead sets a 50-person line as a maximum the employees must stay under.

Draw the inventory buildup diagram for this scenario. What service rate do they need? How did you calculate it?

What happens to the utilization under this scheme (numbers optional)? What’s the business implication?

## Page 15

Airline Check-in Problem – Limited Queue Length (v2)

Positive Buildup

Slope = Target Buildup Rate

## Page 16

Airline Check-in Problem – Limited Queue Length (v2)

- Target Buildup Rate = Slope of Green Line
- Target Buildup Rate = (50-40)/15 = 2/3 ppl/min

- Recall: Buildup Rate (b) = Arrival (𝝀) – Service (𝝁)
- 𝝁= 𝝀- b = 8 – 2/3 = 22/3 ppl/min

- Effect on Utilization?
- Decreases
- Business implications?

## Page 17

Process Flow Analysis: Ceramics Line

Consider the following three stage production process of glass ceramics, which is operated as a worker-paced line.

Finished

5 min/unit

4 min/unit

Components6 min/unit

Goods




Rework

## Page 18

Process Flow Analysis:

Ceramics Line

The process is experiencing severe quality problems related to

insufficiently trained workers.  Specifically, 20 percent of the parts going through Op 1 are badly processed by the operator.

Rather than scrapping the unit, it is moved to a highly skilled rework

operator, who can correct the mistake and finish up the unit completely within 10 minutes.

The same problem occurs at Op 2, where 25 percent of the parts are badly

processed. Ops 3 also has a 1/6 ratio of badly processed parts.  All badly processed parts require 10 minutes to correct and finish up the unit completely.

A. What is the utilization of Op 2 if work is released into the process at a rate of 5 units/hour?

B. Where in the process is the bottleneck?  Why?

C. What is the process capacity?

## Page 19

Process Flow Analysis:

Ceramics Line

μ ρ

General Analysis:

Op 1: λ1= 5 pc/hr, μ1=10 pc/hr, ρ1= λ1/μ1= 5/10 = 1/2 Op 2: λ2= 0.8*λ1 = 0.8*5 pc/hr =4 pc/hr, μ2=12 pc/hr,           ρ2= λ2/μ2 = 4/12 = 1/3 Op 3: λ3= 0.75* λ2 = 0.75* 4 pc/hr = 3 pc/hr,   μ3=15 pc/hr, ρ3= λ3/μ3=3/15= 1/5

Rework:  λR= 0.2*λ1+ 0.25*λ2 + 1/6* λ3 = 0.2*5 pc/hr+ 0.25*4 pc/hr + 1/6* 3 pc/hr

= 2.5 pc/hr, μR= 6 pc/hr ρR= λR/μR=2.5/6= 5/12

ANSWERS:

A. ρ2 = λ2/μ2 = 1/3

B. Compare ρ’s: Op 1 is the Bottleneck!  It has the highest capacity utilization…

C. 10 Unit/hour : the capacity of the bottleneck.
