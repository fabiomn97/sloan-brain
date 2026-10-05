---
title: "MIT LEAD - Analytics for Social Impact (Data Dangerous) Deck Make Up Day 2"
course: "15.002"
course_name: "Leadership Challenges for an Inclusive World"
term: "Fall Term (AY 2026-2027)"
type: "slides"
date: "2026-07-20"
source: "canvas"
url: "https://canvas.mit.edu/courses/38492/files/6621213"
original: "raw/fall-term-ay-2026-2027/15.002/files/mit-lead-analytics-for-social-impact-data-dangerous-deck-make-up-day-2.pdf"
locator_kind: "page"
---

## Page 1

Code: NE22H

Analytics for Social Impact

LEAD at MIT Sloan

Jeremy Ney

## Page 2

Analytics for Social Impact

LEAD at MIT Sloan

Jeremy Ney

## Page 3

Analytics for Social Impact

The 6 measures

Becoming data

Learning from the

The biggest social issues of our time

Stories, stats, and convincing others

The future and why we still fail

[Problems]

of impact [Analysis]

[Communication]

dangerous [Technical]

industry [Solutions]

[Vision]

## Page 4

Hands-on keyboard

activity

Go to datawrapper.de and create an account if you haven’t already

## Page 5

Where the data comes from

## Page 6

“Open with”

“Transportation inequality…”

“Ctr-C / Ctr-V”

“=text(A1,”00000”)

“DOT county data .csv”

“Data is plural”

“Df = requests.get()”

## Page 7

api.census.gov/data/2016/acs/acs1?get=NAME,B01001_001E&for=state*

Census API Geography Function Variable list Predicate Geography

PREDICATE ACTION

&for=state:* All states

&for=state:01 Include only Alabama (state code 01)

&for=county:*&in=state:01 All counties in Alabama

&for=county:001&in=state:01 Only Autauga County (county 001) in Alabama

&for=county:*&in=state:01+place:62328 All counties (or portions of counties) within Prattville city (place 62328) in Alabama

&for=county:073&in=sttate:01+place:07000 Portions of Jefferson County (county 073) in Alabama that are within Birmingham City (place 07000)

## Page 8

//Population of all states: https://api.census.gov/data/2016/acs/acs1?get=NAME ,B01001_001E&for=state:*

//Population of all counties in California: https://api.census.gov/data/2016/acs/acs1?get=NAME ,B01001_001E&for=county&in=state:06

//Income of all counties: https://api.census.gov/data/2019/acs/acs5?get=NAME,B19013_ 001E&for=county:*

## Page 9

bit.ly/jney-datasets

## Page 10

Millions of rows of cleaned county data already extracted from government agency portals

americaninequality.io

## Page 11

Visualizing income inequality across regions

## Page 15

🎉 JACKPOT! 🎉

## Page 16

🧹CLEANUP TIME 🧹

MAKE SURE YOUR NUMBERS ARE NUMBERS AND YOUR FIPS CODES ARE NOT

## Page 19

DASHBOARD → CREATE NEW → MAP

## Page 23

At 5pm on Friday, January 31st, more than 8,000 government websites that host public data went dark
