---
title: "15761CapacityAnalysis2 2026"
course: "15.761"
course_name: "Introduction to Operations Management"
term: "Fall Term (AY 2026-2027)"
type: "slides"
module: "Queueing, Wed Sept 23rd"
date: "2026-09-24"
source: "canvas"
url: "https://canvas.mit.edu/courses/38556/files/6876886"
original: "raw/fall-term-ay-2026-2027/15.761/files/15761capacityanalysis2-2026.pptx"
locator_kind: "slide"
---

## Slide 1 — Announcements

  - Individual assignment on buildup diagrams is due NOW
  - Queuing individual assignment is posted and due September 30 at the beginning of class
  - Recitation this week, Friday, September 25 (E51-315, 1-2 pm) will cover queuing
  - Next two classes are on process innovation & re-engineering (including AI-enabled processes)

## Slide 2 — Last 7 Classes

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

## Slide 4 — Step 2: Demand/Capacity Analysis

- mi
- li
- For each process step i, determine:
- li : demand or input rate (in units of work per unit 	of time)
- mi : realistic maximum service rate, assuming no 	idle time (in units of work per unit of time)
- ri = li / mi : capacity utilization
- li - mi : build-up rate

## Slide 5 — Queuing Theory

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

## Slide 6 — G/G/N Queuing Model

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
- W

## Slide 7 — G/G/N Queuing Formula

- L		average number waiting
- r		capacity utilization ( = l / Nm )
- CA 	coefficient of variation: inter-arrival times
- CS 	coefficient of variation: service times
- N		number of servers
- Approximation with an infinite buffer size:

## Slide 8 — G/G/N Queuing Formula

- L		average number waiting
- r		capacity utilization ( = l / Nm )
- CA 	coefficient of variation: inter-arrival times
- CS 	coefficient of variation: service times
- N		number of servers
- Approximation with an infinite buffer size:

## Slide 9 — Little’s Law

- L = l x W
- Conservation of Flow (equilibrium):
- System
- throughput  l
- Average number
- of individuals/items
- in system  L
- Average time
- spent in system  W

## Slide 10 — Questions on Video?

## Slide 11 — A Deterministic Queue

- Server takes 45 sec. to process each job
- 1 job arrives
- every minute
- Queue
- initially
- empty
- l = 1
- m =        jobs / min
- 4/3

## Slide 12 — Example 1: A Queue with Bursty Arrivals

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
- CA=3/4

## Slide 13

## Slide 14 — Example 2

- Consider the Kendall BofA branch with 4 ATMs, which sees 110 customers per hour on average during a peak period. Each customer uses an ATM for 2 minutes on average. What is the average customer waiting time (assume that the coefficient of variation is equal to 1 for both the customer inter arrival time and service time)?
- What is l?
- What is m?
- What is N?
- What is r?

## Slide 15 — Example 2

- Consider the Kendall BofA branch with 4 ATMs, which sees 110 customers per hour on average during a peak period. Each customer uses an ATM for 2 minutes on average. What is the average customer waiting time (assume that the coefficient of variation is equal to 1 for both the customer inter arrival time and service time)?

## Slide 16 — Example 2 (Poll)

- Consider the Kendall BofA branch with 4 ATMs, which sees 110 customers per hour on average during a peak period. Each customer uses an ATM for 2 minutes on average. What is the average customer waiting time (assume that the coefficient of variation is equal to 1 for both the customer inter arrival time and service time)?
- How many ATMs should be added to cut down the wait time under 2 minutes?(1) At least 8 ATMs(2) 6 ATMs(3) 4 ATMs(4) 2 ATMs(5) 1 ATM

## Slide 17 — Example 2

- Consider the Kendall BofA branch with 4 ATMs, which sees 110 customers per hour on average during a peak period. Each customer uses an ATM for 2 minutes on average. What is the average customer waiting time (assume that the coefficient of variation is equal to 1 for both the customer inter arrival time and service time)?
- How many ATMs should be added to cut down the wait time under 2 minutes?

## Slide 18 — Main Queuing Insight

- 0
- 100%
- Capacity Utilization
- Wait Time (W=L/λ)
- Nonlinear reduction in delays

## Slide 19

## Slide 20 — Example 3

- 
- 2 x  = 2 cust/min
- 
-  = 1 cust/min
- 
- E[Service time]=55 sec, = service rate = 1.09 cust/min, r=utilization=0.917
- Average Wait:
- W1 =
- 
-  = 1 cust/min
- Average Wait W2?
- More than 50% less
- 25% less
- Same
- 25% more
- System 1:
- System 2:

## Slide 21

## Slide 22 — Service Pooling: Efficiency

- 
- 2
- L2
- 
- 1
- L1
- 
- 1
- L
- 2
- Mitigate the impact of unpredictable variability!
- Servers cannot help each other!!!

## Slide 23 — Service Pooling: Efficiency

- 
- 2 x  = 2 cust/min
- 
-  = 1 cust/min
- 
- E[S]=55 sec, = 1.09 cust/min, r=0.917
- Average Wait:
- W = 10 Min
- 
-  = 1 cust/min
- Average Wait:
- W = 4.87 Min

## Slide 24

## Slide 25 — Congestion Analysis Tools

- Build-Up Diagrams
- Predictable Variability
- (t) - (t) > 0 o.k.
- Short Run Analysis
- Variable rates o.k.
- Queuing Theory
- Unpredictable Variability
- / < 1 only
- Long Run Analysis
- Fixed rates only
- All other cases		Simulation / Experiments
- assumes workflow is continuous and deterministic
- stochastic analysis with inter-arrival and service time distributions

## Slide 26 — Capacity Lecture Wrap-Up

- Inventory/queuing buildup diagrams and predictable variability
- Queuing theory and unpredictable variability
- Non-linear relationship between W or L and r
- Add capacity to the bottleneck
- Flexibility (pooling) increases efficiency
