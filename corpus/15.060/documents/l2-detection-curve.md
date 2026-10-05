---
title: "L2-detection-curve"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "document"
module: "Lecture 2: Decisions Under Uncertainty - Experiments and A/B Testing"
date: "2026-09-16"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6841713"
original: "raw/fall-term-ay-2026-2027/15.060/files/class-material/lecture-2/l2-detection-curve.html"
locator_kind: "section"
---

15.060 DMD · Class 2 · Experimentation

### How big a difference can your A/B test actually detect?

The **power curve**: for every possible true difference between two variants, the chance that your experiment returns a statistically significant result (a 95% confidence interval for the difference that excludes 0).

**The case from class.** The AI shopping assistant A/B test, 100 visitors per variant:

|  | Variant A | Variant B |

| Sample mean revenue per visitor | $7.43 | $7.86 |

| Sample standard deviation | $8.36 | $12.28 |

| Visitors | 100 | 100 |

 The variants differed by **$0.43**; the 95% confidence interval for the difference, (−$3.40, +$2.54), contains 0, so we could not name a winner. *Could a test of this size ever have detected a $0.43 difference?*

#### How to use this page

1. **Drag "Visitors per variant."** More visitors slide the curve left: smaller differences become detectable.
2. **Drag "Spread."** This is the standard deviation of revenue per visitor, the one input you don't control. Noisier revenue slides the curve right.
3. **Hover over the curve** to read the power at any true difference.
4. **Presets** load the class A/B test and the two sample-size examples from class (variance 18, detect a $0.50 change, then a $0.05 change).

**What you see.** The blue curve is the power. The grey dashed lines mark 50%, 80% and 99% power, with the smallest difference detectable at each level. The red marker is the $0.43 from class. The curve never drops below 5%: with no real difference at all, 5% of tests still come out "significant". That is the 5% significance level, the false-alarm rate.

Visitors per variant 100 200 visitors in total

2501,40038,0001,000,000

Spread of revenue per visitor (standard deviation σ) $10.50 class A/B test: $8.36 (A), $12.28 (B), pooled ≈ $10.50 · sample-size example: variance 18 → $4.24

$2$8$14$20

Only the ratio (difference ÷ spread) matters.

50% power

smallest difference you'd detect half the time

80% power — the usual target

the minimum detectable difference Δ this sample size buys you

99% power

a difference you would essentially never miss

The $0.43 from class

#### The sample-size formula from class

 For 80% power at the 5% significance level, each group needs

n = 16 σ2 / Δ2

 with σ2 the variance of revenue per visitor and Δ the minimum difference you want to detect. It is this curve read backwards: find where the curve crosses 80% and solve for n. Variance 18, Δ = $0.50: 16 · 18 / 0.25 = 1,152 ≈ 1,160 per group. Δ = $0.05: 115,200. A difference 10× smaller costs 100× the visitors. For the $0.43 from class you would need about  visitors per variant, roughly 90× what the team used.

**Behind the curve.** With N visitors per group and spread σ, the standard error of the difference is SE = σ·√(2/N) and the margin of error is 2·SE, the same multiplier as in class. A true difference Δ is detected with probability Φ(Δ/SE − 2) + Φ(−Δ/SE − 2), Φ being the normal cumulative probability. The x-axis is linear up to $0.10 and logarithmic beyond.

**References.** The 16σ²/Δ² formula is equation 6 of reference 1 (NBER working paper w15701 is its earlier version) and Lehr's "16 s² over d²".
1. List, J. A., Sadoff, S., & Wagner, M. (2011). So you want to run an experiment, now what? Some simple rules of thumb for optimal experimental design. *Experimental Economics*, 14(4), 439–457. (Section 3.1: sample size and power for comparing two means.)
2. Lehr, R. (1992). Sixteen S-squared over D-squared: A relation for crude sample size estimates. *Statistics in Medicine*, 11(8), 1099–1102.
3. Kohavi, R., Longbotham, R., Sommerfield, D., & Henne, R. M. (2009). Controlled experiments on the web: survey and practical guide. *Data Mining and Knowledge Discovery*, 18(1), 140–181. (The same 16·(s/Δ)² rule, applied to online A/B tests.)
4. Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*. Cambridge University Press.
5. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum. (Origin of the 80%-power convention and of measuring differences in units of the standard deviation.)

© 15.060 Data, Models, and Decisions, MIT Sloan. Prepared for Class 2 (Experimentation). Not for redistribution outside the course.
