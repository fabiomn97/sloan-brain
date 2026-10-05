---
title: "Class 5 slides"
course: "15.010"
course_name: "Economic Analysis for Business Decisions: BE"
term: "Fall Term (AY 2026-2027)"
type: "slides"
date: "2026-09-27"
source: "canvas"
url: "https://canvas.mit.edu/courses/38498/files/6885695"
original: "raw/fall-term-ay-2026-2027/15.010/files/slides/class-5-slides.pdf"
locator_kind: "page"
---

## Page 1

PLEASE SIT WITH YOUR TEAMS!

15.010 Economic Analysis for Business Decisions

Class 5: Electricity Markets

Investment Case

## Page 2

Price Theory & Applications

## Page 3

Electricity Markets

## Page 4

Electricity Markets in the US

In these markets, prices are determined by supply and demand curves.

## Page 5

Are Electricity Markets Perfectly Competitive?

Yes

Homogeneous product buyers do not care where the electron came from

Many buyers and sellers hundreds of generating companies and utilities

Firms are price takers no single plant can move the market price

So we can use the competitive model from Class 3: plants bid marginal cost and the market clears where supply meets demand.

## Page 6

The Dataset You Were Given

- Real data from Hitachi Energy, the Bloomberg of electricity markets

## Page 7

File 1: Every Operating Plant in New England

plant_name fuel_type capacity capacity_factor fuel_cost_per_mwh

Name of the plant One of 8 fuel types

Maximum output, MW

Average share of capacity it can produce, %

Marginal cost, $ per MWh

2 Millstone nuclear 2114.08 100 6.31

3 Lake Road Generating Plant natural gas 803.74 100 37.65

4 Canal Plant (oil) oil 1118.25 100 93.34

5 Somerset (SDWRN) biofuels 99.8 100 8.51

6 SEMASS Resource Recovery waste 70.65 100 6.32

7 Bingham Wind Project wind 191 43.01 0

8 S C Moore water 195.75 6.25 0.24

9 Gravel Pit Solar solar 120 Depends on Time of Day 0

⋮ … 1,164 rows in all

## Page 8

File 2: Every Plant Under Construction

plant_name fuel_type expected_online_year capacity

Name of the plant Solar, water or wind First year it generates Maximum output, MW

2 Gardiner Rd solar 2026 4.99

3 River Road Solar solar 2026 3.9

4 OffshoreMW MA Wind wind 2026 1000

5 Pennamaquan Tidal Power Plant water 2027 21.1

6 Freedom Pine Solar solar 2029 250

7 Commonwealth Wind wind 2030 1232

8 Western Maine Energy Storage water 2033 500

⋮ … 336 rows in all

## Page 9

Lab: Investment Decision Using Supply and Demand

Question 1 For each of the eight fuel types in the data, provide a few sentences on what sorts of costs would enter into an estimate of marginal cost. Is there anything unique about any of them?

Question 2 For each of the same eight fuel types, provide a few sentences on the nature of capacity. For example, how is the capacity of solar changing over time? Is the same true for a natural gas power plant?

## Page 10

Overview of the Lab

- The goal of the lab is to make an investment decision for a data center

- Electricity is the main input

- We use supply and demand to understand electricity prices in New England

## Page 11

Lab: Investment Decision Using Supply and Demand

Question 1 For each of the eight fuel types in the data, provide a few sentences on what sorts of costs would enter into an estimate of marginal cost. Is there anything unique about any of them?

Question 2 For each of the same eight fuel types, provide a few sentences on the nature of capacity. For example, how is the capacity of solar changing over time? Is the same true for a natural gas power plant?

## Page 12

What Is a Power Plant’s Marginal Cost?

Fuel-driven: gas, oil, biofuels

Near zero: solar, wind, hydro,

They burn fuel to make each MWh. The cost of that fuel is the marginal cost.

nuclear, waste Little or no fuel to buy: $0 for solar and wind, a few dollars a MWh for the rest.

Capital costs are irrelevant here, however large. Marginal cost is the cost of one more MWh from a plant that already exists.

## Page 13

What Is a Power Plant’s Marginal Cost?

Fuel-driven: gas, oil, biofuels

Near zero: solar, wind, hydro,

They burn fuel to make each MWh. The cost of that fuel is the marginal cost.

nuclear, waste Little or no fuel to buy: $0 for solar and wind, a few dollars a MWh for the rest.

Capital costs are irrelevant here, however large. Marginal cost is the cost of one more MWh from a plant that already exists.

## Page 14

Average Marginal Cost by Fuel Type

## Page 15

Average Marginal Cost by Fuel Type

## Page 16

Capacity Factors

The share of its maximum capacity a plant can produce on average

High: gas, oil, nuclear, biofuels, waste

Low: wind, solar, water

Runs only when the wind blows, the sun shines or the water flows.

Can run whenever the operator wants.

## Page 17

Capacity Factors

The share of its maximum capacity a plant can produce on average

High: gas, oil, nuclear, biofuels, waste

Low: wind, solar, water

Runs only when the wind blows, the sun shines or the water flows.

Can run whenever the operator wants.

## Page 18

Average Capacity Factor

## Page 19

Average Capacity Factor

## Page 20

Solar Capacity Factor

What is special about solar? Its capacity factor is high in the daytime and zero at night

To find what a plant can actually produce Effective capacity = maximum capacity × capacity factor

## Page 21

Solar Capacity Factor

What is special about solar? Its capacity factor is high in the daytime and zero at night

To find what a plant can actually produce Effective capacity = maximum capacity × capacity factor

## Page 22

Total Adjusted Capacity, Day and Night

Daytime Nighttime

## Page 23

Total Adjusted Capacity, Day and Night

Daytime Nighttime

## Page 24

In Reality, Capacity Factors Are More Complex

Note Capacity factors vary by the hour of the day, and the two technologies

peak at opposite times

## Page 25

In Reality, Capacity Factors Are More Complex

Note Capacity factors vary by the hour of the day, and the two technologies

peak at opposite times

## Page 26

Lab Questions

Question 3 Construct a supply curve using the plants in New England during daytime hours and nighttime. How would solar supply change daytime and nighttime hours?

## Page 27

Lab Questions

Question 3 Construct a supply curve using the plants in New England during daytime hours and nighttime. How would solar supply change daytime and nighttime hours?

## Page 28

Hourly Daytime Supply Curve

## Page 29

Hourly Daytime Supply Curve

## Page 30

Zooming In

Hover anywhere on the chart to read the capacity, the price and the marginal fuel.

## Page 31

Zooming In

Hover anywhere on the chart to read the capacity, the price and the marginal fuel.

## Page 32

The Same Curve, Coloured by Fuel

## Page 33

The Same Curve, Coloured by Fuel

## Page 34

Daytime and Nighttime

## Page 35

Daytime and Nighttime

## Page 36

Lab Questions

Question 4 Suppose the hourly demand for electricity is perfectly inelastic and is equal to 17,000 MW during the daytime and 9,000 MW during the nighttime. What are the daytime and nighttime electricity prices in New England in 2025? What are the fuel types of marginal plants during daytime and nighttime?

## Page 37

Lab Questions

Question 4 Suppose the hourly demand for electricity is perfectly inelastic and is equal to 17,000 MW during the daytime and 9,000 MW during the nighttime. What are the daytime and nighttime electricity prices in New England in 2025? What are the fuel types of marginal plants during daytime and nighttime?

## Page 38

Daytime: Where Does Demand Land?

## Page 39

Daytime: Where Does Demand Land?

## Page 40

Nighttime: Where Does Demand Land?

## Page 41

Nighttime: Where Does Demand Land?

## Page 42

Nighttime Price

## Page 43

Nighttime Price

## Page 44

What Determines Electricity Demand?

Several factors can affect electricity demand

## Page 45

What Determines Electricity Demand?

Several factors can affect electricity demand

## Page 46

Demand Depends on the Hour of the Day

ISO New England, 2025. EIA Hourly Electric Grid Monitor, series ISNE.

## Page 47

Demand Depends on the Hour of the Day

ISO New England, 2025. EIA Hourly Electric Grid Monitor, series ISNE.

## Page 48

Daily and Monthly Variation

ISO New England, 2025. EIA Hourly Electric Grid Monitor, series ISNE.

## Page 49

Daily and Monthly Variation

ISO New England, 2025. EIA Hourly Electric Grid Monitor, series ISNE.

## Page 50

Is Inelastic Demand a Good Assumption?

- Would consumers change their electricity use with the price?

- Long-run versus short-run elasticity

- Long-run responses: efficient appliances, retrofitting buildings, substituting to other energy sources

Within the hour, almost perfectly inelastic. Over ten years, not at all.

## Page 51

Is Inelastic Demand a Good Assumption?

- Would consumers change their electricity use with the price?

- Long-run versus short-run elasticity

- Long-run responses: efficient appliances, retrofitting buildings, substituting to other energy sources

Within the hour, almost perfectly inelastic. Over ten years, not at all.

## Page 52

Lab Questions

Question 5 Using the provided data, construct the supply curve in 2031 for New England during a daytime hour. What assumptions did you make to do so?

Question 6 Suppose the daytime demand for electricity is perfectly inelastic and is equal to 20,000 MW. What is the change in daytime price from using the 2025 supply curve compared to the 2031 supply curve?

## Page 53

Lab Questions

Question 5 Using the provided data, construct the supply curve in 2031 for New England during a daytime hour. What assumptions did you make to do so?

Question 6 Suppose the daytime demand for electricity is perfectly inelastic and is equal to 20,000 MW. What is the change in daytime price from using the 2025 supply curve compared to the 2031 supply curve?

## Page 54

The Assumptions Behind the 2031 Curve

- Every planned plant online by 2031 is added

- No retirements

- No new construction beyond the planned file

- No cancellations of planned projects

- Marginal costs remain the same

## Page 55

Entry Shifts the Curve Right

## Page 56

The Assumptions Behind the 2031 Curve

- Every planned plant online by 2031 is added

- No retirements

- No new construction beyond the planned file

- No cancellations of planned projects

- Marginal costs remain the same

## Page 57

Entry Shifts the Curve Right

## Page 58

What Is Each Assumption Worth?

Dashboard 1

Click to open the interactive dashboard (Dashboard 1.html)

The 2031 daytime supply curve at 20,000 MW of demand (Question 6). Demand growth compounds from 2025.

## Page 59

What Is Each Assumption Worth?

Dashboard 1

Click to open the interactive dashboard (Dashboard 1.html)

The 2031 daytime supply curve at 20,000 MW of demand (Question 6). Demand growth compounds from 2025.

## Page 60

Question 7: The Data Center

## Page 61

Question 7: The Data Center

## Page 62

Question 7

Item Value

GPUs 500,000 H100

Power draw 1,500 W each, continuous

GPU price $28,000 each

Construction $2.0bn + $16m per MW

Other operating cost $375m a year

You are a developer planning a data center in New England to serve AI inference. The facility will house 500,000 NVIDIA H100 GPUs and comes online in 2027. Table 1 gives what is known about the project.

## Page 63

Question 7

Item Value

GPUs 500,000 H100

Power draw 1,500 W each, continuous

GPU price $28,000 each

Construction $2.0bn + $16m per MW

Other operating cost $375m a year

You are a developer planning a data center in New England to serve AI inference. The facility will house 500,000 NVIDIA H100 GPUs and comes online in 2027. Table 1 gives what is known about the project.

## Page 64

Question 7

Part (a) How much electricity does this facility consume in an hour, and over a full year?

## Page 65

(a) How Much Electricity?

Power draw 500,000 GPUs × 1,500 W = 750 MW , drawn continuously

## Page 66

Question 7

Part (a) How much electricity does this facility consume in an hour, and over a full year?

## Page 67

(a) How Much Electricity?

Power draw 500,000 GPUs × 1,500 W = 750 MW , drawn continuously

## Page 68

Question 7

Part (b) Using the supply curve you build for 2027, what price will the data center pay for electricity in a daytime hour, and in a nighttime hour? Does connecting this facility change the price that everyone else in New England pays? Figure 1 gives twenty years of New England demand if you want to project it forward.

## Page 69

(b) Daytime: the Load Lands on the Plateau

## Page 70

Question 7

Part (b) Using the supply curve you build for 2027, what price will the data center pay for electricity in a daytime hour, and in a nighttime hour? Does connecting this facility change the price that everyone else in New England pays? Figure 1 gives twenty years of New England demand if you want to project it forward.

## Page 71

(b) Daytime: the Load Lands on the Plateau

## Page 72

(b) Nighttime: the Same 750 MW Lands on a Cliff

## Page 73

(b) Nighttime: the Same 750 MW Lands on a Cliff

## Page 74

Yes, It Changes What Everyone Else Pays

## Page 75

Yes, It Changes What Everyone Else Pays

## Page 76

Question 7

Part (c) What is the data center’s annual electricity bill?

## Page 77

A Bill Needs a Price for Every Year

Supply, every year

Demand, every year

Demand has to be projected forward from the history.

The planned plants come online year by year, so the supply curve shifts right each year.

## Page 78

Question 7

Part (c) What is the data center’s annual electricity bill?

## Page 79

Supply Curve Through 2034

## Page 80

A Bill Needs a Price for Every Year

Supply, every year

Demand, every year

Demand has to be projected forward from the history.

The planned plants come online year by year, so the supply curve shifts right each year.

## Page 81

Supply Curve Through 2034

## Page 82

Twenty-One Years of New England Demand

## Page 83

Twenty-One Years of New England Demand

## Page 84

Daytime, Year by Year

Dashed line: regional demand on the 2020–2025 trend, 17,000 MW in 2027 and up 345 MW a year, plus the facility’s 750 MW.

## Page 85

Daytime, Year by Year

Dashed line: regional demand on the 2020–2025 trend, 17,000 MW in 2027 and up 345 MW a year, plus the facility’s 750 MW.

## Page 86

Nighttime, Year by Year

The same walk at night: demand on the 2020–2025 trend from 9,000 MW in 2027, plus the facility’s 750 MW, with no solar in the stack.

## Page 87

Nighttime, Year by Year

The same walk at night: demand on the 2020–2025 trend from 9,000 MW in 2027, plus the facility’s 750 MW, with no solar in the stack.

## Page 88

The Bill, Year by Year

Year Daytime price Nighttime price Electricity bill

2027 $36.25 $32.05 $224.4m

2028 $36.25 $32.05 $224.4m

2029 $36.25 $32.05 $224.4m

2030 $36.25 $31.11 $221.3m

2031 $36.25 $32.05 $224.4m

2032 $36.65 $32.05 $225.7m

2033 $36.65 $32.05 $225.7m

2034 $37.11 $32.05 $227.2m

2035 $37.25 $33.85 $233.6m

2036 $37.65 $33.85 $234.9m

Total $2265.7m

## Page 89

What Assumptions Did We Make?

- Supply forecast. Every planned plant is built, on time, and nothing is built after the file ends

- Cancellations. None. Will all planned projects actually be completed?

- Demand forecast. The 2020–2025 trend, extended in a straight line: about 2% a year. Will it continue?

- Gas price. Held at 2025 levels, and gas is the marginal plant nearly every hour

## Page 90

The Bill, Year by Year

Year Daytime price Nighttime price Electricity bill

2027 $36.25 $32.05 $224.4m

2028 $36.25 $32.05 $224.4m

2029 $36.25 $32.05 $224.4m

2030 $36.25 $31.11 $221.3m

2031 $36.25 $32.05 $224.4m

2032 $36.65 $32.05 $225.7m

2033 $36.65 $32.05 $225.7m

2034 $37.11 $32.05 $227.2m

2035 $37.25 $33.85 $233.6m

2036 $37.65 $33.85 $234.9m

Total $2265.7m

## Page 91

What Assumptions Did We Make?

- Supply forecast. Every planned plant is built, on time, and nothing is built after the file ends

- Cancellations. None. Will all planned projects actually be completed?

- Demand forecast. The 2020–2025 trend, extended in a straight line: about 2% a year. Will it continue?

- Gas price. Held at 2025 levels, and gas is the marginal plant nearly every hour

## Page 92

Question 7

Part (d) Based on your analysis, would you recommend building this data center in New England? You will have to take a stand on things Table 1 does not give you: how much of its capacity it actually sells, what it earns per GPU-hour, and how long it operates. Figure 2 gives the market price of renting one H100 for one hour, in dollars per GPU-hour, for every month from January 2025 to July 2026; use it to build your revenue assumption. State your assumptions and say why you chose them. Which of these assumptions matters most to your answer, and how would you go about pinning it down?

## Page 93

The Cost Side: Building It and Running It

Table 1 of the assignment. The fixed cost is spent before the facility opens in 2027.

## Page 94

Question 7

Part (d) Based on your analysis, would you recommend building this data center in New England? You will have to take a stand on things Table 1 does not give you: how much of its capacity it actually sells, what it earns per GPU-hour, and how long it operates. Figure 2 gives the market price of renting one H100 for one hour, in dollars per GPU-hour, for every month from January 2025 to July 2026; use it to build your revenue assumption. State your assumptions and say why you chose them. Which of these assumptions matters most to your answer, and how would you go about pinning it down?

## Page 95

The Cost Side: Building It and Running It

Table 1 of the assignment. The fixed cost is spent before the facility opens in 2027.

## Page 96

Electricity Cost Under Different Assumptions

Dashboard 2

Click to open the interactive dashboard (Dashboard 2.html)

750 MW drawn every hour, 2027 to 2036, on top of demand on the 2020–2025 trend (17,000 MW by day and 9,000 MW at night in 2027).

## Page 97

Electricity Cost Under Different Assumptions

Dashboard 2

Click to open the interactive dashboard (Dashboard 2.html)

750 MW drawn every hour, 2027 to 2036, on top of demand on the 2020–2025 trend (17,000 MW by day and 9,000 MW at night in 2027).

## Page 98

The Cost Side, Summarised

## Page 99

The Revenue Side

We also need revenue: what the data center earns renting out its GPUs

## Page 100

The Cost Side, Summarised

## Page 101

The Revenue Side

We also need revenue: what the data center earns renting out its GPUs

## Page 102

What an H100 Actually Rents For

## Page 103

The Revenue Side: Assumptions

Utilisation 90% Share of GPU-hours actually rented. High, but standard for capacity built against contracts

Rental price in 2027 $2.27 The nineteen-month mean of Figure 2; July 2026 was $2.70

Price decline 10% a year Each new generation (B200, then its successor) pushes down what an H100 rents for

Useful life 5 years The GPUs are worth nothing after 2031: no resale, no second life

## Page 104

What an H100 Actually Rents For

## Page 105

Revenue, Year by Year

Year Rental price, $/GPU-hour GPU-hours sold Revenue

2027 $2.27 3.94bn $8.95bn

2028 $2.04 3.94bn $8.05bn

2029 $1.84 3.94bn $7.25bn

2030 $1.65 3.94bn $6.52bn

2031 $1.49 3.94bn $5.87bn

Total $36.64bn

500,000 GPUs × 8,760 hours × 90% = 3.94bn GPU-hours a year

## Page 106

The Revenue Side: Assumptions

Utilisation 90% Share of GPU-hours actually rented. High, but standard for capacity built against contracts

Rental price in 2027 $2.27 The nineteen-month mean of Figure 2; July 2026 was $2.70

Price decline 10% a year Each new generation (B200, then its successor) pushes down what an H100 rents for

Useful life 5 years The GPUs are worth nothing after 2031: no resale, no second life

## Page 107

Discounted Cash Flow

Year Revenue Electricity Other operating Cash flow Discounted at 6%

Build −$28.00bn −$28.00bn

2027 $8.95bn −$224m −$375m $8.35bn $7.88bn

2028 $8.05bn −$224m −$375m $7.45bn $6.63bn

2029 $7.25bn −$224m −$375m $6.65bn $5.58bn

2030 $6.52bn −$221m −$375m $5.93bn $4.69bn

2031 $5.87bn −$224m −$375m $5.27bn $3.94bn

Net present value $0.73bn

## Page 108

Revenue, Year by Year

Year Rental price, $/GPU-hour GPU-hours sold Revenue

2027 $2.27 3.94bn $8.95bn

2028 $2.04 3.94bn $8.05bn

2029 $1.84 3.94bn $7.25bn

2030 $1.65 3.94bn $6.52bn

2031 $1.49 3.94bn $5.87bn

Total $36.64bn

500,000 GPUs × 8,760 hours × 90% = 3.94bn GPU-hours a year

## Page 109

Discounted Cash Flow

Year Revenue Electricity Other operating Cash flow Discounted at 6%

Build −$28.00bn −$28.00bn

2027 $8.95bn −$224m −$375m $8.35bn $7.88bn

2028 $8.05bn −$224m −$375m $7.45bn $6.63bn

2029 $7.25bn −$224m −$375m $6.65bn $5.58bn

2030 $6.52bn −$221m −$375m $5.93bn $4.69bn

2031 $5.87bn −$224m −$375m $5.27bn $3.94bn

Net present value $0.73bn

## Page 110

NPV Under Different Assumptions

Assumption Total revenue Net present value

Base case $36.64bn $0.73bn

Rental price stays at $2.27 $44.74bn $7.17bn

Start at July 2026’s $2.70 $43.59bn $6.65bn

Utilisation 70% $28.50bn −$6.22bn

Useful life 6 years $41.93bn $4.03bn

Useful life 4 years $30.77bn −$3.21bn

Electricity price doubles $36.64bn −$0.22bn

## Page 111

NPV Under Different Assumptions

Assumption Total revenue Net present value

Base case $36.64bn $0.73bn

Rental price stays at $2.27 $44.74bn $7.17bn

Start at July 2026’s $2.70 $43.59bn $6.65bn

Utilisation 70% $28.50bn −$6.22bn

Useful life 6 years $41.93bn $4.03bn

Useful life 4 years $30.77bn −$3.21bn

Electricity price doubles $36.64bn −$0.22bn

## Page 112

Question 7

Part (e) Build an interactive dashboard for this decision. A user should be able to vary the assumptions that matter — the number of GPUs, how much of its capacity it sells, the rental price per GPU-hour, the price of electricity, and how long the project lasts — and see whether the project should be built, along with the numbers behind that verdict. Use an AI coding assistant. Submit your dashboard as an HTML file with your slides.

## Page 113

(e) The Dashboard

Dashboard 3

Click to open the interactive dashboard (Dashboard 3.html)

## Page 114

Question 7

Part (e) Build an interactive dashboard for this decision. A user should be able to vary the assumptions that matter — the number of GPUs, how much of its capacity it sells, the rental price per GPU-hour, the price of electricity, and how long the project lasts — and see whether the project should be built, along with the numbers behind that verdict. Use an AI coding assistant. Submit your dashboard as an HTML file with your slides.

## Page 115

Takeaways

- Supply and demand predict future electricity prices and forecast revenue

- The marginal plant sets the price: gas, day and night, even where renewables are most of the fleet

- A new load moves the price by the local slope of supply, which is why 750 MW is 16 cents by day and $2.88 at night

- A very difficult decision: high uncertainty and long-lived capital

## Page 116

(e) The Dashboard

Dashboard 3

Click to open the interactive dashboard (Dashboard 3.html)

## Page 117

Takeaways

- Supply and demand predict future electricity prices and forecast revenue

- The marginal plant sets the price: gas, day and night, even where renewables are most of the fleet

- A new load moves the price by the local slope of supply, which is why 750 MW is 16 cents by day and $2.88 at night

- A very difficult decision: high uncertainty and long-lived capital
