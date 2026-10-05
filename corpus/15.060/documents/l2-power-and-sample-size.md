---
title: "L2-power-and-sample-size"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "document"
module: "Lecture 2: Decisions Under Uncertainty - Experiments and A/B Testing"
date: "2026-09-16"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6841714"
original: "raw/fall-term-ay-2026-2027/15.060/files/class-material/lecture-2/l2-power-and-sample-size.html"
locator_kind: "section"
---

15.060 DMD · Class 2 · Experimentation

### Sizing an A/B test: how many visitors do you need?

Two bell curves for the difference in sample means, one if the variants truly perform the same and one if one variant truly beats the other by Δ. The result is statistically significant only when the observed difference lands beyond the margin of error, so that the 95% confidence interval for the difference excludes 0.

**The case from class.** The AI shopping assistant A/B test: Variant A averaged $7.43 (standard deviation $8.36), Variant B $7.86 ($12.28), 100 visitors each. The margin of error for the difference was $2.97, the interval (−$3.40, +$2.54) contained 0, and the 100 new visitors were best sent to the noisier Variant B. The sample-size formula from class, n = 16σ²/Δ², gave 1,160 visitors per group for a revenue metric with variance 18 and a minimum difference of $0.50.

#### How to use this page

- **Left column, top two panels:** the four inputs of the sample-size decision. Three you control (Δ, the significance level, the power) and one you don't (how noisy each variant is).
- **Left column, bottom panel:** the visitors in each group. "Equal split" and "Best split" set them to the fewest visitors that reach your target power. "Class example" and "Sample-size example" load the numbers from class.
- **Top chart:** the two bells. The dashed line is the margin of error, 2 × SE. Red is a false alarm (no real difference, but the interval excludes 0). Gold is a miss (a real difference, but the interval contains 0).
- **Cards:** standard error, margin of error, power, total visitors.
- **Sizing rule box:** compares how many standard errors wide Δ is with how many you need. Under, over, or just right.
- **Lower chart and table:** power against total visitors, and the visitors needed under the class formula, an exact equal split, and the best split.

#### The three factors you control

Δ minimum difference you want to detect ($ per visitor)

A business judgement: how big a lift would change your launch decision?

Significance level chance of a false alarm — lower is better 10% (multiplier 1.64) 5% (multiplier 2, as in class) 1% (multiplier 2.58)

Power chance of detecting Δ if it exists — higher is better

80% is the usual convention.

#### The factor you don't control

sA standard deviation, Variant A

sB standard deviation, Variant B

Estimate from historical data or an A/A test. The class formula assumes one variance for both groups; this page lets them differ.

#### Visitors in each group

NA Variant A

NB Variant B

"Best split" gives the noisier variant more visitors, in proportion to sA : sB.

 No real difference: x̄A − x̄B is bell-shaped around 0  Real difference: bell-shaped around Δ  False alarm (no real difference, but the CI excludes 0)  Miss (real difference, but the CI contains 0)

Both bells have width SE = √(sA²/NA + sB²/NB), the standard error of the difference from class. The dashed line is the margin of error,  × SE. Gold is a real $ lift that you miss: one minus the power.

Standard error of the difference

√(s_A²/N_A + s_B²/N_B)

Margin of error

Power

Total visitors

The sizing rule Δ = (zconfidence + zpower) · SE

| How many standard errors wide your true difference is Δ / SE |  |

| How many you need for the target power zconfidence + zpower |  |

With the class multiplier of 2 for 5% significance and 0.84 for 80% power, the right-hand side is 2.84. Squared and doubled for two groups: 16.1. **That is the 16 in the class formula n = 16σ²/Δ².**

Power against total visitors at the current A : B split. The curve flattens past the target: the last few points of power are the expensive ones.

#### Visitors needed to detect $ at this significance level and power

| How you split the visitors | Variant A | Variant B | Total |

| Class formula n = 16σ²/Δ², with σ² the average of the two variances |  |  |  |

| Exact, equal split (NA = NB) |  |  |  |

| Exact, best split (more visitors to the noisier variant) |  |  |  |

**References.** The picture, the sizing rule and the best split follow List, Sadoff & Wagner (2011), Section 3.1; the 16σ²/Δ² rule is their equation 6 and Lehr's "16 s² over d²".
1. List, J. A., Sadoff, S., & Wagner, M. (2011). So you want to run an experiment, now what? Some simple rules of thumb for optimal experimental design. *Experimental Economics*, 14(4), 439–457.
2. Lehr, R. (1992). Sixteen S-squared over D-squared: A relation for crude sample size estimates. *Statistics in Medicine*, 11(8), 1099–1102.
3. Kohavi, R., Longbotham, R., Sommerfield, D., & Henne, R. M. (2009). Controlled experiments on the web: survey and practical guide. *Data Mining and Knowledge Discovery*, 18(1), 140–181.
4. Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*. Cambridge University Press.

Technical notes. Normal approximation throughout, slightly optimistic below about 15 visitors per group. Both bells use the same SE, following List et al. The 5% significance level uses the multiplier 2, as in class; 10% and 1% use 1.64 and 2.58.

© 15.060 Data, Models, and Decisions, MIT Sloan. Prepared for Class 2 (Experimentation). Not for redistribution outside the course.
