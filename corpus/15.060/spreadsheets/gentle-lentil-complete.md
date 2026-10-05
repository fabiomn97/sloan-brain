---
title: "Gentle Lentil complete"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "spreadsheet"
module: "Recitation 2: Simulation"
date: "2026-09-17"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6846968"
original: "raw/fall-term-ay-2026-2027/15.060/files/recitations/recitation-2/gentle-lentil-complete.xlsx"
locator_kind: "sheet"
---

## Sheet ReadMe

| Gentle Lentil Model |
| --- |
| Model is based on the "Gentle Lentil Restaurant" case at the end of Chapter 5 of the DMD textbook |
| The model explore 3 career paths facing Sanjay Thomas, a second year Sloan MBA: |
|  | 1) Consulting: | Sanjay has a job offer in hand with an annual salary of $80,000 (p.s.: this case was written a while back!) |
|  | 2) Ownership: | Sanjay is thinking of starting his own restaurant business with full ownership of the business |
|  | 3) Partnership: | If Sanjay chooses to open the restaurant business he has the option of a partnership. |
|  |  | The partnership guarantees a minimum monthly income, but leaves him with only 10% of any monthly income in excess of $9,000 |
|  | In order to maintain a reasonable lifestyle while paying off his loans after graduation, Sanjay would need to earn approximately $5,000 per month |
| Source of uncertainty: |
|  | i) Number of meals sold each month |
|  | ii) Prix fixe meal price (based on four possible market scenarios) |
|  | iii) Labor cost |
| The "model without uncertainty" worksheet sets these uncertain inputs to their expected (or average) values |
| The annual model generates 12 monthly (uncorrelated) draws of the number of meals and evaluates the total annual income. The partnership contract, however, is applied monthly. |
| Simulation parameters: |  | Number of trials = |  | 10000 |
|  |  | Seed (fixed) = |  | 1 |

## Sheet Model without uncertainty

| Model Without Uncertainty |
| --- |
| Model Constants |  |  | Model Uncertainties |  |  |  | Restaurant Profit Model |
| Minimum acceptable salary per month [$] | 5000 |  | Number of meals sold | Distribution (Normal) |  |  | Monthly revenue [$] | 53775 |
|  |  |  | Mean | 3000 |  |  | Costs per month |
| Consulting salary per month [$] | 6666.666666666667 |  | Standard deviation | 1000 |  |  | Fixed Costs [$] | 3995 |
|  |  |  |  |  |  |  | Variable Food Cost [$] | 33000 |
| Restaurant non-labor fixed costs per month |  |  | Monthly number of meals sold (to be simulated) | 3000 |  |  | Labor Costs [$] | 5950 |
| Rent [$] | 3000 |  |  |  |  |  | Total costs per month [$] | 42945 |
| Leased equipment [$] | 275 |  | Revenue per meal | Distribution (Discrete) |
| Utilities [$] | 265 |  |  | Meal Price [$] | Probability |  | Summary |
| Insurance [$] | 155 |  | Very Healthy Market | 20 | 0.25 |
| Loan repayment [$] | 125 |  | Healthy Market | 18.5 | 0.35 |  |  | Monthly income [$] |
| Advertising/Promotion [$] | 100 |  | Not So Healthy Market | 16.5 | 0.3 |  | Consulting [$] | 6666.666666666667 |
| Miscellaneous [$] | 75 |  | Unhealthy Market | 15 | 0.1 |  | Ownership [$] | 10830 |
| Total [$] | 3995 |  |  |  |  |  | Partnership [$] | 9183 |
|  |  |  | Revenue per meal [$] (to be simulated) | 17.925 |
| Variable cost of food per meal [$] | 11 |  |  |  |  |  | Partnership - Ownership[$] | -1647 |
|  |  |  | Monthly labor costs | Distribution (Uniform) |
| Financial partnership agreement |  |  | Minimum | 5040 |
| Monthly salary minimum [$] | 3500 |  | Maximum | 6860 |
| Profit sharing percentage | 0.9 |
| Monthly profit sharing threshold [$] | 9000 |  | Monthly labor costs [$] (to be simulated) | 5950 |
| Key: |
| Model Constants |
| Random Variables |
| Model Equation |
| Major Forecasted Outputs |

## Sheet Simulation model

| Simulation Model |
| --- |
| Model Constants |  |  | Model Uncertainties |  |  |  | Restaurant Profit Model |
| Minimum acceptable salary per month [$] | 5000 |  | Number of meals sold | Distribution (Normal) |  |  | Monthly revenue [$] | #NAME? |
|  |  |  | Mean | 3000 |  |  | Costs per month |
| Consulting salary per month [$] | 6666.666666666667 |  | Standard deviation | 1000 |  |  | Fixed Costs [$] | 3995 |
|  |  |  |  |  |  |  | Variable Food Cost [$] | #NAME? |
| Restaurant non-labor fixed costs per month |  |  | Monthly number of meals sold (to be simulated) | #NAME? |  |  | Labor Costs [$] | #NAME? |
| Rent [$] | 3000 |  |  |  |  |  | Total costs per month [$] | #NAME? |
| Leased equipment [$] | 275 |  | Revenue per meal | Distribution (Discrete) |
| Utilities [$] | 265 |  |  | Meal Price [$] | Probability |  | Summary |
| Insurance [$] | 155 |  | Very Healthy Market | 20 | 0.25 |
| Loan repayment [$] | 125 |  | Healthy Market | 18.5 | 0.35 |  |  | Monthly income [$] |
| Advertising/Promotion [$] | 100 |  | Not So Healthy Market | 16.5 | 0.3 |  | Consulting [$] | #NAME? |
| Miscellaneous [$] | 75 |  | Unhealthy Market | 15 | 0.1 |  | Ownership [$] | #NAME? |
| Total [$] | 3995 |  |  |  |  |  | Partnership [$] | #NAME? |
|  |  |  | Revenue per meal [$] (to be simulated) | #NAME? |
| Variable cost of food per meal [$] | 11 |  |  |  |  |  | Partnership - Ownership [$] | #NAME? |
|  |  |  | Monthly labor costs | Distribution (Uniform) |
| Financial partnership agreement |  |  | Minimum | 5040 |
| Monthly salary minimum [$] | 3500 |  | Maximum | 6860 |
| Profit sharing percentage | 0.9 |
| Monthly profit sharing threshold [$] | 9000 |  | Monthly labor costs [$] (to be simulated) | #NAME? |
| Key: |
| Model Constants |
| Random Variables |
| Model Equation |
| Major Forecasted Outputs |

## Sheet RiskSerializationData

| 7 | 1 |
| --- | --- |
| #NAME? | False | 1 | 1 | GF1_rK0qDwEAEAD1AAwjACYAOQCBAJUAlgCkALIAzwDxAOsAKgD//wAAAAAAAQQAAAAABSMsIyMwAAAAAUJNb250aGx5IGxhYm9yIGNvc3RzIFskXSAodG8gYmUgc2ltdWxhdGVkKSAvIERpc3RyaWJ1dGlvbiAoVW5pZm9ybSkBAAEBEAACAAEKU3RhdGlzdGljcwMBAQD/AQEBAQEAAQEBAAQAAAABAQEBAQABAQEABAAAAAG2AAAXAA9Vbmlmb3JtKC0xMCwxMCkAACUBAAIA1wDhAAEBAgGamZmZmZmpPwAAZmZmZmZm7j8AAAUAAQEBAAEBAQA= | 1 | #NAME? | 0 | 1 | True | False | 1 | False | #NAME? |
| 0 |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEADsAAwjACYAOQBiAHYAdwCFAJMAxgDoAOIAKgD//wAAAAAAAQQAAAAABSMsIyMwAAAAASNDb25zdWx0aW5nIFskXSAvIE1vbnRobHkgaW5jb21lIFskXQEAAQEQAAIAAQpTdGF0aXN0aWNzAwEBAP8BAQEBAQABAQEABAAAAAEBAQEBAAEBAQAEAAAAAZcAAisAI0NvbnN1bHRpbmcgWyRdIC8gTW9udGhseSBpbmNvbWUgWyRdAAAvAQACAAIAzgDYAAEBAgGamZmZmZmpPwAAZmZmZmZm7j8AAAUAAQEBAAEBAQA= | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAALAgwjACYAPQCIAAUBBgFJAYwBvgEHAu4BKgCkIwACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEiT3duZXJzaGlwIFskXSAvIE1vbnRobHkgaW5jb21lIFskXQEAAQABBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAIzQAAQIAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAALU3RhdHNMZWdlbmQDAQABRHtNaW4sTWF4LE1lYW4sLU1lYW5DSSg5MCksTWVkaWFuLFNELC1QKDEwKSwtUCgyNSksLVAoNzUpLC1QKDkwKSxDbnR9pQEBAQEBAAEBACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAAAAQAAAABAQAAAQABAQAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAAAEAAAAAZABAioAIk93bmVyc2hpcCBbJF0gLyBNb250aGx5IGluY29tZSBbJF0AAC8BAAIAAgDcAeUBAQACAADDAAAAAQZUYWhvbWEAAKBBAAAAAAAAAAAAAAAAAAEAAAAAAIizQAEYAAEBAKQjAQZUYWhvbWEAAKBBAAAAAAAAAQEBAA== | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAAPAgwjACYAPQCKAAcBCAFLAY4BwgELAvIBKgD//wACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEkUGFydG5lcnNoaXAgWyRdIC8gTW9udGhseSBpbmNvbWUgWyRdAQABAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAjNAABAAAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAtTdGF0c0xlZ2VuZAMBAAFEe01pbixNYXgsTWVhbiwtTWVhbkNJKDkwKSxNZWRpYW4sU0QsLVAoMTApLC1QKDI1KSwtUCg3NSksLVAoOTApLENudH3/AQEBAQEAAQEAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAAABAAAAAEBAAABAAEBACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAAAAQAAAABkgECLAAkUGFydG5lcnNoaXAgWyRdIC8gTW9udGhseSBpbmNvbWUgWyRdAAAvAQACAAIA4AHpAQEAAgAAwwAAAAEGVGFob21hAACgQQAAAAAAAAAAAAAAAAABAAAAAACIs0ABGAABAQCkIwEGVGFob21hAACgQQAAAAAAAAEBAQA= | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAAUAgwjACYAPQCWABMBFAFXAZoB2gEQAgoCKgD//wACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEwUGFydG5lcnNoaXAgLSBPd25lcnNoaXAgWyRdIC8gTW9udGhseSBpbmNvbWUgWyRdAQABAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAjNAABAAAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAtTdGF0c0xlZ2VuZAMBAAFEe01pbixNYXgsTWVhbiwtTWVhbkNJKDkwKSxNZWRpYW4sU0QsLVAoMTApLC1QKDI1KSwtUCg3NSksLVAoOTApLENudH3/AQEBAQEAAQEAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAAABAAAAAEBAAABAAEBACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAAAAQAAAABngECOAAwUGFydG5lcnNoaXAgLSBPd25lcnNoaXAgWyRdIC8gTW9udGhseSBpbmNvbWUgWyRdAAAvAQACAAIA+AEBAgEAAgAAwwAAAAEGVGFob21hAACgQQAAAAAAAAAAAAAAAAABAAAAAAAAAAABBQABAQEAAQEBAA== | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAD2AQwjACYAPQCHAAQBBQFIAYsBvAHyAewBKgD//wACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEhT3duZXJzaGlwIFskXSAvIEFubnVhbCBpbmNvbWUgWyRdAQABAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAjNAABAAAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAtTdGF0c0xlZ2VuZAMBAAFEe01pbixNYXgsTWVhbiwtTWVhbkNJKDkwKSxNZWRpYW4sU0QsLVAoMTApLC1QKDI1KSwtUCg3NSksLVAoOTApLENudH3/AQEBAQEAAQEAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAAABAAAAAEBAAABAAEBACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAAAAAQAAAABjwECKQAhT3duZXJzaGlwIFskXSAvIEFubnVhbCBpbmNvbWUgWyRdAAAvAQACAAIA2gHjAQEAAgAAwwAAAAEGVGFob21hAACgQQAAAAAAAAAAAAAAAAABAAAAAABM7UABBQABAQEAAQEBAA== | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAD6AQwjACYAPQCJAAYBBwFKAY0BwAH2AfABKgD//wACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEjUGFydG5lcnNoaXAgWyRdIC8gQW5udWFsIGluY29tZSBbJF0BAAEAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAACM0AAEAACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAC1N0YXRzTGVnZW5kAwEAAUR7TWluLE1heCxNZWFuLC1NZWFuQ0koOTApLE1lZGlhbixTRCwtUCgxMCksLVAoMjUpLC1QKDc1KSwtUCg5MCksQ250ff8BAQEBAQABAQAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAAAEAAAAAQEAAAEAAQEAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAAABAAAAAGRAQIrACNQYXJ0bmVyc2hpcCBbJF0gLyBBbm51YWwgaW5jb21lIFskXQAALwEAAgACAN4B5wEBAAIAAMMAAAABBlRhaG9tYQAAoEEAAAAAAAAAAAAAAAAAAQAAAAAATO1AAQUAAQEBAAEBAQA= | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| #NAME? | True | 0 | 1 | GF1_rK0qDwEAEAASAgwjACYAPQCVABIBEwFWAZkB2AEOAggCKgD//wACAAAAAAQCRjAAAkYwAAUjLCMjMAAAAAEvUGFydG5lcnNoaXAgLSBPd25lcnNoaXAgWyRdIC8gQW5udWFsIGluY29tZSBbJF0BAAEAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAACM0AAEAACMBBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAC1N0YXRzTGVnZW5kAwEAAUR7TWluLE1heCxNZWFuLC1NZWFuQ0koOTApLE1lZGlhbixTRCwtUCgxMCksLVAoMjUpLC1QKDc1KSwtUCg5MCksQ250ff8BAQEBAQABAQAjAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAEGVGFob21hAACgQQAAAAAAAAAEAAAAAQEAAAEAAQEAIwEGVGFob21hAACgQQAAAAAAAQZUYWhvbWEAAKBBAAAAAAABBlRhaG9tYQAAoEEAAAAAAAAABAAAAAGdAQI3AC9QYXJ0bmVyc2hpcCAtIE93bmVyc2hpcCBbJF0gLyBBbm51YWwgaW5jb21lIFskXQAALwEAAgACAPYB/wEBAAIAAMMAAAABBlRhaG9tYQAAoEEAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAQUAAQEBAAEBAQA= | 1 | 0 | 0 |  | >75% | <25% | >90% |  |  |  |  |  |  |  |  |
| 0 |
| False | 15680 | 7345 | 3520 | 0 |
| False | 15680 | 7345 | 3520 | 0 |
| False | 15680 | 7345 | 3520 | 0 |
| False | 15680 | 7345 | 3520 | 0 |
| False | 15680 | 7345 | 3520 | 0 |
| 0 |
| 0 | False | False | 10 | 0.95 | 1 |

## Sheet Simulation model (annual)

| Annual Simulation Model |
| --- |
| Model Constants |  |  | Model Uncertainties |  |  |  | Restaurant Profit Model |
| Minimum acceptable salary per month [$] | 5000 |  | Number of meals sold | Distribution (Normal) |  |  | Full earnings by month [$] | #NAME? | #NAME? |
|  |  |  | Mean | 3000 |  |  |  | #NAME? | #NAME? |
| Consulting salary per month [$] | 6666.666666666667 |  | Standard deviation | 1000 |  |  |  | #NAME? | #NAME? |
|  |  |  |  |  |  |  |  | #NAME? | #NAME? |
| Restaurant non-labor fixed costs per month |  |  | Monthly number of meals sold (to be simulated) | #NAME? | #NAME? |  |  | #NAME? | #NAME? |
| Rent [$] | 3000 |  |  | #NAME? | #NAME? |  |  | #NAME? | #NAME? |
| Leased equipment [$] | 275 |  |  | #NAME? | #NAME? |
| Utilities [$] | 265 |  |  | #NAME? | #NAME? |  | Partnership earnings by month [$] | #NAME? | #NAME? |
| Insurance [$] | 155 |  |  | #NAME? | #NAME? |  |  | #NAME? | #NAME? |
| Loan repayment [$] | 125 |  |  | #NAME? | #NAME? |  |  | #NAME? | #NAME? |
| Advertising/Promotion [$] | 100 |  |  |  |  |  |  | #NAME? | #NAME? |
| Miscellaneous [$] | 75 |  | Revenue per meal | Distribution (Discrete) |  |  |  | #NAME? | #NAME? |
| Total [$] | 3995 |  |  | Meal Price [$] | Probability |  |  | #NAME? | #NAME? |
|  |  |  | Very Healthy Market | 20 | 0.25 |
| Variable cost of food per meal [$] | 11 |  | Healthy Market | 18.5 | 0.35 |  | Summary |
|  |  |  | Not So Healthy Market | 16.5 | 0.3 |
| Financial partnership agreement |  |  | Unhealthy Market | 15 | 0.1 |  |  | Annual income [$] |
| Monthly salary minimum [$] | 3500 |  |  |  |  |  | Consulting [$] | #NAME? |
| Profit sharing percentage | 0.9 |  | Revenue per meal [$] (to be simulated) | #NAME? |  |  | Ownership [$] | #NAME? |
| Monthly profit sharing threshold [$] | 9000 |  |  |  |  |  | Partnership [$] | #NAME? |
|  |  |  | Monthly labor costs | Distribution (Uniform) |
| Key: |  |  | Minimum | 5040 |  |  | Partnership - Ownership [$] | #NAME? |
| Model Constants |  |  | Maximum | 6860 |
| Random Variables |
| Model Equation |  |  | Monthly labor costs [$] (to be simulated) | #NAME? |
| Major Forecasted Outputs |
