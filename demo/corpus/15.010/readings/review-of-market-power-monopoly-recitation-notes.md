---
title: "Review of Market Power (Monopoly) — Recitation notes"
course: "15.010"
course_name: "Economic Analysis for Business Decisions"
term: "Fall 2004"
type: "reading"
module: "Recitations"
source: "MIT OpenCourseWare"
url: "https://ocw.mit.edu/courses/15-010-economic-analysis-for-business-decisions-fall-2004/235c362b58425d779647029a7566a587_time_uncrtn_mkt.pdf"
locator_kind: "page"
---

## Page 1

Sloan School of Management                                                                                                             15.010/15.011 Massachusetts Institute of Technology

RECITATION NOTES #5

Time and Uncertainty, Market Power

Friday - October 08, 2004 OUTLINE OF TODAY’S RECITATION

1. Basics of present value

2. Uncertainty and risk aversion

3. Option value

4. Market Power Models: definition and calculations

5. Numeric Examples: applying these concepts to exercises

1. BASICS OF PRESENT VALUE 1.1 Definition and Use 1.2 Net Present Value and Capital Budgeting 1.1 Definition and Use The concept of present value allows us to take a stream of future cash flows, profits, revenues, or costs and convert them to a single comparable value for the present.  This concept allows us to make decisions now based on what we expect to happen in the future. Specifically, present value tells us the value of some monetary amount at some point in the future.  We use an annual interest rate or discount rate (represented by R) to essentially “convert” these future cash flows into present values.  For example, if we have $1 today, then we could invest that $1 at the current annual interest rate, R, and receive (1+R) dollars one year from now.  This (1+R) dollars is known as the future value of $1 today.  Likewise, if we want to know the value of receiving $1 one year from now, we simply discount that $1 by the current

annual interest rate, or ) 1( 1 $

R + .  The $1 we receive in one year will be worth less to us than $1

now because we could have invested that $1 now and received (1+R) dollars one year from now.

## Page 2

It becomes straightforward to generalize this to additional years in the future, so that $1 two

today.  Expanding this out to n number of years, the present

years from now is worth 2) 1( 1 $

R +

value of $1 after n years is simply n R) 1( 1 $ +

1.2 Net Present Value and Capital Budgeting Net Present Value (NPV) is a concept that is used frequently in many business situations.  It is a financial tool that takes the discounted cash flows associated with a project and compares that to the cost investment to be made for the project.  It is often used when making capital budgeting decisions, such as deciding whether to build a new plant or to invest in some new technology that may not pay off for many years in the future. For example, if we have a capital investment that we expect to earn profits for 15 years, then the NPV of that investment can be shown as

15 15 2 2 1 ) 1( ) 1( ) 1( R R R C NPV + + + + + + + − = π π π "

where C represents the initial cost of the project (we assume the entire cost is incurred now).  In general, a firm would only want to make an investment decision when the NPV of a project is greater than 0.  This means that the stream of future profits—discounted to the present—is greater than the upfront cost of that investment.  If the NPV is negative, then the firm would not want to undertake that project.

As shown above, R represents the discount rate that we use to convert our future profits into present values.  Obviously, the discount rate chosen can significantly influence the present values of our future profits and hence the NPV.  In considering the appropriate discount rate, you should think about what alternative investments the firm could make with the money it would cost for the project.  Perhaps there are other projects that could yield different future profits and perhaps a higher rate of return.  Or the firm could invest in bonds or securities that yield a different, perhaps higher, return. The most important consideration for a discount rate is that an alternative investment must of similar risk.  An alternative investment may have a much higher return than a proposed project but the certainty of those cash flows may be much less than the certainty of the proposed project. Although this topic is covered in much more detail in corporate finance classes, often a firm will use a weighted average cost of capital (WACC) for a discount rate, which reflects both the opportunity cost of its debt and of its equity.

## Page 3

2. UNCERTAINTY AND RISK AVERSION 2.1 Uncertain Cash Flows and Calculating Expected Value 2.2 Risk Aversion 2.1 Uncertain Cash Flows and Calculating Expected Value When making capital budgeting decisions for events or cash flows that will happen in the future, we often are unsure about the certainty of these cash flows.  Depending on our assumptions, we may receive one cash flow but because future conditions are uncertain, we may receive a different cash flow if those conditions occur. We can factor in this uncertainty by considering the probabilities of these future cash flows or events.  For example, in a very simple case, we may have to decide whether to invest in a project that will either generate $1 million with a 40% probability or $2 million with a 60% probability. To account for these probabilities formally, we turn to a concept called expected value. Calculating the expected value considers both the alternative cash flows and their respective probabilities.  Given two potential payoffs, or cash flows, called X1 and X2, and two probabilities for those payoffs, called Pr1 and Pr2, the expected value of this scenario would simply be

2 2 1 1 Pr Pr ) ( X X X E + =

. We can also extend this to any number of payoffs and respective probabilities:

X E Pr ) ( 1 n n X X X Pr Pr 2 2 1 + + + " = .  In each case, the sum of the probabilities must equal one.

2.2 Risk Aversion Risk aversion also incorporates this concept of uncertainty.  Each person has a different willingness to accept risk, or a different willingness to accept an uncertain outcome over a certain outcome with the same expected value.  We usually classify people into one of three risk categories:

1. Risk averse: These people prefer a certain outcome over an uncertain, or risky, outcome with the same expected value. 2. Risk neutral: These people have no preference for a certain outcome over an uncertain, or risky, outcome with the same expected value. 3. Risk loving: These people prefer an uncertain, or risky, outcome over a certain outcome with the same expected value.

For instance, in your first job out of graduate school, you could be offered the following two types of compensation plans:

A. Guaranteed salary of $150,000. B. Guaranteed salary of $100,000 plus a potential bonus of $100,000 that you receive if

you meet certain performance goals and no bonus if you do not meet these goals. You also believe that there is about a 50% chance that you will meet these performance goals.

Both of these options have the same expected value of $150,000, but there is some uncertainty with Option B.  Those who prefer Option A would be risk-averse because they prefer the certain income.  Those who prefer Option B would be risk-loving because they prefer the uncertain

## Page 4

income, although there is a 50% chance they could receive a $100,000 bonus, or $50,000 more than the certain income of Option A.  Those who have no preference would be risk-neutral. 3. OPTION VALUE 3.1 Definition and Use 3.2 Example 3.1 Definition of Option Value Many times managers have to make decisions based on incomplete information.  As described above, expected value is a way of calculating the current value of taking an action in an uncertain situation using estimates of the probability of certain outcomes.  But if a manager could defer making a decision until he or she had more information, the outcome becomes more certain.  The ability to defer such a decision has value, and is known as option value. 3.2 Example For example, consider a project that could have two outcomes: a good outcome in which the firm gains $1 million, and a bad outcome in which the company loses $1 million.  The firm has to make a decision today, and is unsure of which outcome will occur.  The firm believes the good outcome has a 40% chance of happening, and the bad outcome has a 60% chance of happening. Should the firm undertake the project? The expected value of the project is .4*$1,000,000 + .6*-$1,000,000 = -$200,000.  The expected value of not doing the project is of course zero, so the firm should opt to not do the project and get payoff zero. Now suppose the firm has the option to defer making a decision until it knows whether the outcome of the project will be good or bad (which still will occur with 40% and 60% probability as before).  By postponing the decision, the firm can wait, then undertake the project if the good outcome is assured (netting $1,000,000) or not undertake the project if the bad outcome is assured (payout of zero).  The expected value is now .4*$1,000,000 + .6*$0 = $400,000.  By gaining the option to defer a decision, the firm gains $400,000 – so that option is worth $400,000 to the firm. The decision tree below describes these two scenarios:

## Page 5

Decision without option Decision with option

+$1,000,000 +$1,000,000 Good Yes

Yes Good -$1,000,000 $0 Bad No

$0 Good Yes -$1,000,000 No Bad

$0 $0 Bad No EV = $0 EV = .4 * $1,000,000 = $400,000 Note that the option can become “worthless” – in fact, in this example there is a 60% chance the firm will choose to not exercise its option.  The value of the option is created by the firm’s ability to postpone making the decision until it is more certain about the outcome. 4. MARKET POWER MODELS 4.1 One Plant Model 4.2 Two Plant Model 4.1 One Plant Model A monopolist, in order to maximize it profits, needs to follow the following process. Let’s assume that he faces a Cost Curve of C(Q) and a Demand Curve of Q(P).

1. Solve the demand curve equation Q(P) for P and write P as a function of Q (P(Q)). 2. Calculate the Marginal Revenue (MR) curve. For demand curves that are linear, the marginal revenue curve has the same intercept and a slope that is twice as steep as a demand curve expressed as a function of Q (e.g. for demand, P=40-100Q, MR=40- 200Q).  The marginal revenue curve can also be calculated by taking the first derivative of the equation for total revenue, where total revenue is expressed as a function of Q. 3. Calculate the Marginal Cost. This can be done by calculating MC = ∆C/ ∆Q. 4. Solve the equation MC = MR for Q. The resulting Q* is the optimal quantity. 5. Insert the resulting optimal quantity Q* in the demand curve P(Q) for determining the profit maximizing price P*. 6. Calculate the profits: Π = P* Q* - C(Q*)

## Page 6

As a rule of thumb the monopolist should price according to the so-called mark-up formula: P = MC / (1 + 1 / Ed), where Ed is the elasticity of demand. For example if the elasticity of demand is -4 and marginal cost is $9 per unit than the price should be: $9 / (1-1/4) = $12  per unit 4.2 Two Plants Model A monopolist with two plant faces not only the problem of determining the correct quantities to produce and the price to adopt, but also the amount of production needed to be produced in each plant. In order to maximize its profits, this monopolist needs to follow the following process. Let’s assume that the monopolist faces a Demand Curve of Q(P) and two different cost curves in the two different plants: C1(Q1) and C2(Q2).

1. Solve the demand curve equation Q(P) for P: P(Q) 2. Calculate the Marginal Revenue (MR) curve. For demand curves that are linear, the marginal revenue curve has the same intercept and a slope that is twice as steep as a demand curve expressed as a function of Q.  The marginal revenue curve can also be calculated by taking the first derivative of the equation for total revenue, where total revenue is expressed as a function of Q. 3. Calculate the Marginal Cost curves for the two plants. This can be done by calculating MC1 = ∆C1/ ∆Q1 and MC2 = ∆C2/ ∆Q2.. 4. Calculate the total Marginal Cost from the previous two MC functions. In order to do so, the monopolist needs to:

a. Solve MC1 for Q1; b. Solve MC2 for Q2, c. Sum the resulting Q1 + Q2, as MC1 = MC2 as long as production is occurring in

both plants (otherwise, production should shift to the lower cost plant until marginal costs are equal). d. Solve the QTOT = for MCTOT 5. Solve the equation MCTOT = MR for Q. The resulting Q* is the optimal total quantity the monopolist will produce. 6. Insert the resulting optimal quantity Q* in the demand curve P(Q) to determine the profit maximizing price P(Q*) 7. Calculate the quantities Q1 and Q2 produced in each plant. In order to do so he needs to: a. Equal the Profit maximizing Marginal Cost level MCTOT (Q*) to the first plant’s

marginal cost schedule MC1 (as MCTOT = MC1 = MC2) b. Solve for Q1. c. Calculate in a similar way Q2. d. Check for mistakes: Q1 + Q2 has to be equal to QTOT. 8. Calculate the profits: Π = P* Q* - C1(Q1) – C2(Q2)

## Page 7

5. NUMERIC EXAMPLES 5.1 Example of Net Present Value 5.2 Example of Market power with one plant 5.3 Example of Market power with two plants 5. 1 Example of Net Present Value As a new member of your company’s finance department, you are given the task of determining whether the company should invest in two product line expansions.  Project A has lower future cash flows than Project B, but because Project A is more related to your company’s existing product line, the company feels it is less risky than Project B.  You’ve done some more analysis and have formulated the following future profits for each project (with the first cash flow occurring one year from now).  Each project is expected to have a life of 5 years. Year 1 Year 2 Year 3 Year 4 Year 5 Project A $5MM $10MM $10MM $15MM $15MM Project B $5MM $10MM $15MM $20MM $20MM You also believe that each project will require about $40 million in upfront investment.  Finally, based on the different risk assumptions, you believe that Project A should use a discount rate of 7% while Project B will have a discount rate of 20%.  Which project(s) should the company undertake? To make this decision, you need to calculate the NPV of each project.  Project A would have an NPV of

= + + + + + + + + + + − = 5 4 3 2 1 ) 07 . 1( 15 $ ) 07 . 1( 15 $ ) 07 . 1( 10 $ ) 07 . 1( 10 $ ) 07 . 1( 5 $ 40 $ ) ( MM MM MM MM MM MM A NPV $3.7 MM

Project B would have an NPV of

= + + + + + + + + + + − = 5 4 3 2 1 ) 20 . 1( 20 $ ) 20 . 1( 20 $ ) 20 . 1( 15 $ ) 20 . 1( 10 $ ) 20 . 1( 5 $ 40 $ ) ( MM MM MM MM MM MM B NPV -$2.5 MM

We want to accept any project that has an NPV greater than 0, so we would accept Project A but would reject Project B.  This occurred even though Project B had greater future profits, but with greater risk around those profits.

## Page 8

5.2 Example of Market power with one plant We are the world’s only producers of the little red knobs on your laptop button mouse.  There is only one plant, and it has the following total cost structure (prices in $/knob and quantities in million knobs): TC(Q)  =  20*Q2 How will we price our products to maximize profits, assuming the following demand curve?

Qd  =  35 – P/20 Recall that a monopoly will choose the quantity produced so that MR = MC.  To solve for MR, we must find the formula for Total Revenue TR.  This requires us to rewrite the demand function as P = 700 – 20*Qd:

TR(Q)  =  P(Q) * Q  =  (700–20*Q)*Q  =  700*Q – 20*Q2 Marginal Revenue (MR) is the first derivative of Total Revenue (TR): MR  =  TR’(Q)  =  (700*Q – 20*Q2)’  =  700 – 40*Q (Note that for a linear demand curve, the marginal revenue curve has the same intercept as the demand curve and a slope that is twice as steep.) Now, MC  =  TC’(Q)  =  (20*Q2)’  =  40*Q By setting MR = MC we find that: 700 – 40*Q = 40*Q Q = 700/80 Q = 8.75 mm knobs Plugging this quantity in the demand equation, we get: P = 700 – 20*8.75

P = $525/knob And profits are: Π = TR(Q) – TC(Q) = P*Q – TC(Q) Π = 525*8.75 – 20*8.752 Π  = $3,063mm

## Page 9

5.3 Example of Market Power with two plants Our firm builds a new factory. The cost structure for each factory is as follows: Factory 1 : TC1(Q1) = 20*Q1

2 Factory 2 : TC2(Q2) = 10*Q2

2 The demand has remained unchanged.  Total production Q = Q1 + Q2. How will we set output from each plant, and what will profits be? Again, we have to set MR = MC.  This time, however, we have to find the company’s total marginal cost. We know, MC1  =  40*Q1 MC2  =  20*Q2 Writing the marginal cost equations in inverse form and horizontally sum them to obtain total marginal cost, MCT (which is equal to MC1 and MC2 because the firm will produce until MC is equal at both plants): Q  =  Q1 + Q2  =  MC1/40 + MC2/20  =  3*MCT/40, or MCT = 40 * Q / 3 Then, setting MCT = MR: 40 * Q / 3 = 700 – 40 * Q Q =13.1 mm knobs , and MR = 700 – 525 = $175/knob Since MR = MCT = MC1 =MC2, (MR equals MC at all plants), MC1 = 175 = 40* Q1,    =>    Q1 = 4.4 mm knobs MC2 = 175 = 20* Q2,    =>    Q2 = 8.75 mm knobs To find the monopoly price, substitute for Q in the demand equation: P = 700 – 20*13.1,   =>   P = $438/knob Profits will be Total Revenue minus Total Costs: Π = TR(Q) – TC(Q) = P*Q – TC1(Q1) – TC2(Q2) Π = 438*13.1– 20*4.42 – 10*8.752

Π =$4,585mm
