---
title: "15761CapacityAnalysis12026"
course: "15.761"
course_name: "Introduction to Operations Management"
term: "Fall Term (AY 2026-2027)"
type: "slides"
module: "Capacity and Process Analytics, Wed Sept 16th"
date: "2026-09-19"
source: "canvas"
url: "https://canvas.mit.edu/courses/38556/files/6853932"
original: "raw/fall-term-ay-2026-2027/15.761/files/15761capacityanalysis12026.pptx"
locator_kind: "slide"
---

## Slide 1 — Announcements

  - Recitation this week, Friday Sep 18 (315 1-2 pm) will cover build up diagrams
  - First individual assignment is due Sep 23 at the beginning of class (no AI-assistance is allowed)
  - No class on Monday September 21
  - Prep for next class (September 23) video on queuing

## Slide 2 — Next 7 Classes

- Process analysis of business environments (strategy positioning and process design)
- Process performance (quantitative tools):- Capacity analysis & variability- Quality

## Slide 3 — Capacity Lecture

- CAPACITY
- too high:
- too low:
- Customer wait / death
- Brand damage
- Customer dissatisfaction
- Lost sales
- Low employee morale
- High turnover
- Capital expenses
- Labor expenses
- Resource waste
- Environmental damage
- Cash flow issues
- QUALITY
- FLEXIBILITY
- TIME
- COST

**Speaker notes:** Afternoon: Matthew Selove, Saurabh Tandon, Manav Maheshwari, Jose Marco

## Slide 4 — Methodology

- Step 1:	Process Flow Diagram
- Step 2:	Demand and Capacity Analysis
- Step 3:	Congestion Analysis
- Step 4:	Financial/Decision Analysis
- This
- lecture

## Slide 5 — Step 2: Demand/Capacity Analysis

- mi
- li
- For each process step i, determine:
- li : demand or input rate (in units of work per unit 	of time) – in today’s class we will use di
- mi : realistic maximum service rate, assuming no 	idle time (in units of work per unit of time)
- ri = li / mi : capacity utilization
- li - mi : build-up rate

## Slide 6 — Throughput

- m1
- l1
- m2
- l2
- 50 cust/hr
- 10 cust/hr
- 10 cust/hr
- 50 cust/hr
- 500 cust/hr
- 50 cust/hr
- l2 = min(l1, m1)
- After waiting for long enough:

## Slide 7 — Network

- m1
- l1
- m3
- l3
- m2
- l2
- min(l1, m1)
- min(l2, m2)
- l3 = min(l1, m1)+min(l2, m2)

## Slide 8 — Buildup Diagrams

- Think of work as being liquid
- No rocket science, but requires a little care
- Predictable Variability
- (t) - (t) > 0 ok
- Short Run Analysis
- Variable rates ok

## Slide 9 — Buildup Example: Fish Processing

- Fish
- processing
- facility
- Ships arrive
- input rate d(t)
- Processed
- Fish
- 4
- 8
- 12
- 0
- 4800
- 3600
- 600
- Time (Months)
- Input Rate d(t)
- (Tons / Month)
- Freezer
- Capacity R
- Processing rate m = 3000
- (Tons / Month)
- t

## Slide 10 — Freezer Inventory Diagram

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- Assume Infinite Freezer Capacity
- buildup rate =
- buildup rate =
- buildup rate =
- d = 3600 then 4800 then 600, m = 3000
- Av. Monthly Throughput = how much plant processAv. Monthly Inventory =

## Slide 11 — Freezer Inventory Diagram

- 4
- 8
- 12
- 0
- 2400
- Time (Months)
- Inventory
- (Tons)
- 9600
- Assume Infinite Freezer Capacity
- buildup rate = 600
- buildup rate = 1800
- buildup rate = -2400
- Av. Throughput = 3000 Tons/MonthAv. Monthly Inventory = 4000 Tons
- d = 3600 then 4800 then 600, m = 3000

## Slide 12 — Limited Storage Capacity?

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- Freezer capacity R = 2400
- 9
- d = 3600 then 4800 then 600, m = 3000
- Av. Throughput=
- Av. Inventory=

## Slide 13 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- Freezer capacity R = 2400
- 9
- b.up rate =
- b. up rate =
- d = 3600 then 4800 then 600, m = 3000

## Slide 14 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- Freezer capacity R = 2400
- 9
- b.up rate = 600
- b. up rate = -2400
- Av. Throughput= (9*3000 + 3*600)/12=2400 Tons/Month
- Av. Inventory=(2400*2 + 2400*4 + 2400*0.5)/12=1300 Tons
- Av. Wait time = ?
- d = 3600 then 4800 then 600, m = 3000

## Slide 15 — Little’s Law

- L = l x W
- Conservation of Flow (equilibrium):
- System
- throughput  l
- Average number
- of individuals/items
- in system  L
- 300 new MBA’s/Year x 2 Years MBA = 600 students in Sloan
- Average time
- spent in system  W

## Slide 16 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- Freezer capacity R = 2400
- 9
- b.up rate = 600
- b. up rate = -2400
- Av. Throughput= (9*3000 + 3*600)/12=2400 Tons/Month
- Av. Inventory=(2400*2 + 2400*4 + 2400*0.5)/12=1300 Tons
- Av. Wait time = ?
- d = 3600 then 4800 then 600, m = 3000

## Slide 17 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- Freezer capacity R = 2400
- 9
- b.up rate = 600
- b. up rate = -2400
- Av. Throughput= (9*3000 + 3*600)/12=2400 Tons/Month
- Av. Inventory=(2400*2 + 2400*4 + 2400*0.5)/12=1300 Tons
- Av. Wait time = Av. Inventory/Av. Throughput
- d = 3600 then 4800 then 600, m = 3000

## Slide 18 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- Freezer capacity R = 2400
- 9
- b.up rate = 600
- b. up rate = -2400
- Av. Throughput= (9*3000 + 3*600)/12=2400 Tons/Month
- Av. Inventory=(2400*2 + 2400*4 + 2400*0.5)/12=1300 Tons
- Av. Wait time = Av. Inventory/Av. throughput rate to freezer=1,300/2,400 Months
- d = 3600 then 4800 then 600, m = 3000

## Slide 19 — Limited Storage Capacity

- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- Freezer capacity R = 2400
- 9
- b.up rate = 600
- b. up rate = -2400
- Av. Throughput= (9*3000 + 3*600)/12=2400 Tons/Month
- Av. Inventory=(2400*2 + 2400*4 + 2400*0.5)/12=1300 Tons
- Av. Wait time = Av. Inventory/Av. throughput rate to freezer=1,300/2,400 Months
- Av. Arrival rate = (4*3,600 + 4*3,000 + 4*600)/12=2,400 Tons/Month
- d = 3600 then 4800 then 600, m = 3000

## Slide 20 — A Smarter Policy!

- Inventory = 233 Tons
- Throughput = 2400 Tons / Month
- 4
- 8
- 12
- 0
- Time (Months)
- Inventory
- (Tons)
- 2400
- average
- inventory
- is 233 tons
- 9
- 6.66
- l = 3600 then 4800 then 600, m = 3000

## Slide 21 — The Ideal Demand Pattern?

## Slide 22 — Queuing Theory

- Sophisticated analysis (but easy formulas)
- predicting long-term impact of
- unpredictable variability on congestion.
- G/G/N queuing formula
- Little’s law (flow balance)
- Managerial insights
- Unpredictable Variability
- / < 1 only
- Long Run Analysis
- Fixed rates only
- COVERED

## Slide 23 — A Deterministic Queue

- Server takes 45 sec. to process each job
- 1 job arrives
- every minute
- Queue
- initially
- empty
- l = 1
- m =        jobs / min
- 0
- Time
- (min)
- Queue
- Length ?
- 1
- 2
- 3
- 4
- 5
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 4/3
- NO QUEUE

## Slide 24 — A Queue with Bursty Arrivals

- Server takes 45 sec. to process each job
- Next job arrives:
- - after 15 sec. with probability 1/2
- - after 1 min 45 sec. with probability 1/2
- Queue
- initially
- empty
- l =
- m =
- 4/3
- 1

## Slide 25 — A Queue with Bursty Arrivals

- Server takes 45 sec. to process each job
- 1 job arrives
- every minute
- on average
- Queue
- initially
- empty
- l = 1
- m = 4/3
- 0
- Time
- (min)
- Queue
- Length
- 1
- 2
- 3
- 4
- 5
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- This model captures unpredictable variability

## Slide 26 — G/G/N Queuing Model

- N servers,
- capacity utilization
- r = l / (N x m)
- arrival
- rate l = 1/E[A]
- service time
- distribution S
- CS = s[S] / E[S]
- inter-arrival time
- distribution A
- CA = s[A] / E[A]
- individual
- service rate m = 1/E[S]
- FIFO
- Average queue length L
- Manufacturing
- Call centers
- 911 response
- …
- Examples:
- Airline check-in counters
- Bank ATMs
- Retail cashiers
- Computer processing

## Slide 27 — Predictable Variability

- 27

## Slide 28 — Unpredictable Variability

- 28

## Slide 29 — Capacity Lecture 1 Wrap-Up

- Inventory buildup diagrams and predictable variability
- Queuing theory and unpredictable variability (lecture on Sep 24 – watch prep video)
- The simulation game had both!
- Takeaway: Understanding and accounting for variability (predictable and unpredictable) is key!
