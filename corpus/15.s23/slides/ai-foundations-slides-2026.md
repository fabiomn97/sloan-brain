---
title: "AI Foundations Slides 2026"
course: "15.S23"
course_name: "SSIM: AI Builder Space Proseminar"
term: "Fall Term (AY 2026-2027)"
type: "slides"
module: "09.14_Class 1: Introduction & Vibe Coding Part I"
date: "2026-09-13"
source: "canvas"
url: "https://canvas.mit.edu/courses/40786/files/6829762"
original: "raw/fall-term-ay-2026-2027/15.s23/files/ai-foundations-slides-2026.pdf"
locator_kind: "page"
---

## Page 1

Austin van Loon   ·   Michiel Bakker MIT Sloan   ·   Incoming MBA Class of 2028   ·   September 2026

## Page 2

AI FOUNDATIONS  |  SESSION 2

Friday, September 11, 2026 12:00 – 2:00 PM Wong Auditorium

SCAN TO REGISTER

DESIGNING YOUR MIND FOR THE AI ERA

DESIGNING YOUR MIND FOR THE AI ERA

DESIGNING YOUR MIND FOR THE AI ERA

Are you using AI to outsource what makes you valuable?

Professor Eric So

Sloan Distinguished Professor of Global Economics and Behavioral Science

## Page 3

ONE OF THESE WAS WRITTEN BY CLAUDE

PASSAGE  A

PASSAGE  B

Artiﬁcial intelligence, a term that used to be primarily associated with science ﬁction, is now a facet of our everyday reality. It inﬂuences how we work, what we buy, and even who we love. It should come as no surprise, then, that artiﬁcial intelligence is also changing the tools and methods by which we learn about society.

Artiﬁcial intelligence has moved out of science ﬁction and into ordinary life, mediating how people search for information, apply for jobs, and receive medical care. This diffusion has made machine learning both an infrastructure of social life and an object of social inquiry. Less remarked upon is a third consequence: the same technologies are reshaping the methods of social science itself, altering what counts as data,

how evidence is interpreted, and which questions researchers can ask.

## Page 4

IT WAS PASSAGE “A”

PASSAGE  A

PASSAGE  B

THE MACHINE

Artiﬁcial intelligence, a term that used to be primarily associated with science ﬁction, is now a facet of our everyday reality. It inﬂuences how we work, what we buy, and even who we love. It should come as no surprise, then, that artiﬁcial intelligence is also changing the tools and methods by which we learn about society.

Artiﬁcial intelligence has moved out of science ﬁction and into ordinary life, mediating how people search for information, apply for jobs, and receive medical care. This diffusion has made machine learning both an infrastructure of social life and an object of social inquiry. Less remarked upon is a third consequence: the same technologies are reshaping the methods of social science itself, altering what counts as data,

how evidence is interpreted, and which questions researchers can ask.

Claude Opus 5 asked to write on the same topic. Opening three sentences of Austin’s dissertation.

## Page 5

HOW OFTEN DOES IT MATCH AN EXPERIENCED PROFESSIONAL?

On well-specified professional tasks, with the source files supplied — how often is the best frontier model judged as good as or better than an experienced professional?

100%

75%

50%

25%

10%

0%

Hands up.

## Page 6

AI MATCHES PROFESSIONALS FIVE IN SIX TIMES

OpenAI GDPval: Sept 2025 study + Mar 2026 update (GPT-5.4). One-shot, source files supplied; GPT-5.4 scores 70.8% when excl. ties.

## Page 7

1 2 3 4 5 6

THE NEXT TWO HOURS

What do we mean by “AI”?

Austin

HANDS ON

Learning with/about artifacts

Austin

How frontier systems work

Michiel

AI safety

Michiel

HANDS ON

One brief, one run

Michiel

Evaluation and responsible use

Austin

## Page 8

WHAT DO WE MEAN BY “AI”?

THE MOVING TARGET

“AI is whatever hasn’t been done yet.”

— Larry Tesler, c. 1970

THE HUMAN BENCHMARK

“Machines doing things that would require intelligence if done by people.”

— Marvin Minsky, 1968 — and every textbook since

OURS, FOR TODAY

Software whose behavior is learned from data, not written by hand.

-OR- Software that is “grown”, not “built”.

— Inspired by Samuel (1959); Mitchell (1997); Olah, in Amodei (2025)

## Page 9

THREE KINDS OF AI, ONE INBOX

PREDICTIVE AI

GENERATIVE AI

AGENTIC AI



1 PREDICT

CREATE

ACT

PLAN

NOT SPAM

SPAM

USE TOOLS CHECK

Write me a response to this email.

0% 90% 100%

Read my inbox and respond

Is this email spam?

Write me a response to this email.

to the low-importance ones.

TELLS YOU SOMETHING

DOES SOMETHING WRITES YOU SOMETHING

Classifies or scores a predefined target Generates new content on request Pursues a goal through multiple steps and tools

CLASSIFY GENERATE PLAN + USE TOOLS + ACT

Within permissions you set

## Page 10

WHO HOLDS THE WEIGHTS?

CLOSED

OPEN-WEIGHT

Access through an API. Provider

You hold the parameters. Run it

controls the model, updates it,

privately; you own the

can withdraw it.

maintenance.

## Page 11

1 2 3 4 5 6

THE DELIVERABLE WAS ALWAYS A CHOICE Count off around your table: 1, 2, 3.




a markdown document

a slide deck (.pptx)

an interactive web page

Same topic. Same model. Three deliverables.

## Page 12

TEN MINUTES

1 THE TOPIC


How context windows work, why long AI conversations degrade, and what to do about it.

10:00

2 THE FLOOR PROMPT

I want to learn about the following topic:

3 SETTINGS

How context windows work, why long AI conversations degrade, and what to do about it.

Claude Enterprise · Opus 5 · effort: Low

Can you produce ______ to teach me about this?

1 — a markdown document

2 — a slide deck (.pptx)

4 WHILE IT GENERATES

3 — an interactive web page

Share your prompts.

This is the floor. You can do better.

Share the instructions you gave the model around your table. What differences do you notice?

## Page 13

SAME TOPIC, SAME MODEL — DIFFERENT DELIVERABLES

Pass them around.

1 2 3

What’s something you learned about context windows?


How did you improve on the baseline prompt?


Which artifact would you most want the night before an exam? 3

## Page 14

1 2 3 4 5 6

HOW FRONTIER SYSTEMS WORK

PRE-TRAINING POST-TRAINING INFERENCE HARNESS

## Page 15

IT LEARNED TO PREDICT THE NEXT WORD

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

Prompt: The capital of France is ____

P(Paris) = 97%  P(Lyon) = 1.2%  P(Berlin) = 0.3%  P(pizza) = 0.0001%

-  No notion of true or false — only what tends to follow what.

-  However, to do this well, you will need to learn grammar, facts, logic, humor, code, syntax…

-  At sufficient scale, surprising capabilities emerge.

-  This same mechanism writes essays, debugs code, and generates business plans.

-  10 trillion+ words are used in training

## Page 16

THEN IT WAS SHAPED INTO SOMETHING USEFUL

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

01   PRE-TRAINING

Goal is to shape model behavior after pre-training. In each, the model tries, gets a signal, and is nudged toward what scored well.

1 SFT Supervised fine-tuning

2 RLHF / RLAIF RL from human / AI feedback

3 RLVR RL with verifiable rewards

Learn from examples

Learn from feedback

Learn from checking

The model attempts a task with a checkable

An expert writes the ideal answer to a prompt

The model writes two answers, A and B

answer

The model compares its own answer to the

A human (or an AI) judge picks the better one

An automatic checker says pass or fail

expert’s

Model learns to imitate the expert

Model learns to produce what judges prefer

Model learns what passes the check

WHO TEACHES

Expert-written examples

Human or AI judge

Automatic checker

THE SIGNAL

"Match this answer"

"A is better than B"

"Pass" or "fail"

BEST FOR

Format, tone, house style, following instructions

Helpfulness, judgment, refusals, feeling natural

Math, code, anything you can test automatically

## Page 17

IT WORKS ON YOUR TASK WITH A FINITE BUDGET

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

WHAT YOU SEE

“What is the capital of France?” “It is Paris.”

UNDER THE HOOD

QUERY 1 SYSTEM PROMPT + “What is the capital of France?” It

QUERY 2 SYSTEM PROMPT + “What is the capital of France?” + It is

QUERY 3 SYSTEM PROMPT + “What is the capital of France?” + It + is Paris.

## Page 18

A MODEL IS NOT A SYSTEM

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

THE HARNESS

RUN AGAIN

CONTEXT Files, data, prior work their onboarding folder

CONTROL LOOP Run again, or stop when they know it's done

WORK

MODEL

DONE

Rented THE TASK

PERMISSIONS What it may do alone what they can send alone

One instruction

TOOLS Search, code, systems their laptop and logins

MEMORY What carries over whether anyone writes it down

THE MODEL IS RENTED SO IDENTICAL FOR EVERYONE THE HARNESS IS BUILT AND SHAPES THE PRODUCT

The same weights your competitors are calling.

## Page 19

WHO PLAYS WHERE

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

The four stages are four businesses. A few labs do all of them; most companies pick one, and the cost of entry falls as you move right.

DO ALL FOUR frontier labs Anthropic OpenAI Google DeepMind

Train the model, serve it, and ship the chat app and agents on top SpaceX

Labs only

Post-training "neolabs"

Inference providers

Harness builders

Needs billions in compute and data

Start from an open model and shape it

Run models fast and cheaply at scale

Wrap a rented model in a product

Meta

Thinking Machines

Baseten

Lovable

Together AI

Harvey

DeepSeek

Nous Research

Fireworks AI

Cognition

Alibaba (Qwen)

Prime Intellect

Sierra

Anthropic/OpenAI/Google DeepMind

Factory

And every firm building agents in-house

Open-weight labs release the base model for others to build on

Plus specialists selling the training data and judges (e.g. Scale AI)

Hyperscalers too: AWS Bedrock, Azure, Google Cloud

COST OF ENTRY  $ 10 billion+

COST OF ENTRY  $ 10-100M+

COST OF ENTRY  $ 10-100M+

COST OF ENTRY  <1M

Most companies only ever play in the last column and that is also where most Sloan students are building

## Page 20

UNDERSTANDING THIS YEAR’S AI HEADLINES

01   PRE-TRAINING 02   POST-TRAINING 03   INFERENCE 04   HARNESS

“>$500B poured into data centers” Pre-training is a one-off burn of months on tens of thousands of chips. The industry is building factories before it has finished designing the product.

PRE-TRAINING



“Data companies like Mercor raise billions” Post-training runs on expert examples and expert judges: doctors, lawyers, engineers grading model answers. The scarce input is not compute but skilled human time, and a new industry sells it to the labs. POST-TRAINING

“Memory makers add ~$1T in value” Inference is sequential and re-reads its whole context every pass. Serving fast is a memory-bandwidth problem, so the bottleneck, and the money, moved.

INFERENCE


“Software stocks swing on every lab product launch” The harness is software around a rented model. Each time a lab ships its own agent, the market re-prices whether the application layer can stay separate.

HARNESS


All of you will use these systems. Some of you will build on them. But for everyone it’s important to understand the industry.

## Page 21

1 2 3 4 5 6

HOW DO WE ENSURE THESE SYSTEMS ARE SAFE?

01 TRAIN-TIME

02 RUN-TIME

03 ORGANIZATIONAL

## Page 22

WHAT DO WE MEAN BY “SAFETY”?

Safety means the system does what you intended and nothing you did not.

SOME EXAMPLES OF WHAT CAN GO WRONG


It hallucinates Invents a citation, a number, a policy. Sounds certain. Nobody checks. 3

It does harm Helps someone do something it should have refused: fraud, a weapon, a scam, a leak. 2

It goes further than you asked The agent sends the email, deletes the file, books the flight, before anyone said yes.

19 version 1

## Page 23

01 02 03 TRAIN-TIME

SOME OF IT IS BUILT IN DURING TRAINING

There is no separate safety module. The same post-training that made the model helpful also taught it what to refuse, using the same signals.

TRAINING SIGNALS: EACH TEACHES BOTH

ONE MODEL EVERY ANSWER COMES OUT OF THE SAME SET OF NUMBERS/WEIGHTS

“Draft the board memo.” Writes it. Clear, structured, on brief. capability

Demonstrations
- draft a good memo
- decline a bad request

constraint

“Make the numbers look better.” Pushes back and offers an honest framing.

MODEL one set of numbers

Preferences
- the clearer answer wins
- the honest "I am not sure" wins

Sorry, I cannot help with this. constraint

“Help me get into my colleagues email acccount”

Verified outcomes
- the code passes its tests
- the unsafe output fails the check

OPAQUE no rule you can read; you learn the behaviour by probing it

A TENDENCY, NOT A RULE weakens off-distribution; fine-tuning can strip it

design 1

## Page 24

01 02 03 RUN-TIME

SOME OF IT SITS AROUND THE MODEL AT RUNTIME

Checks wrapped around a model whose behavior has not changed. Policy can change without retraining anything.

RUNTIME SAFETY LAYER: SITS IN THE HARNESS

OUTPUT FILTER A classifier screens the

MODEL

INPUT FILTER A classifier screens the request

REQUEST what the user sends

RESPONSE what the user sees

unchanged

block, allow, or flag

response block, rewrite, or flag

THE RULES   constitutional methods An explicit policy document the filters (and the model itself) check against. Edit the document, change the behavior.

UPDATABLE WITHOUT RETRAINING new policy on Tuesday, live by Wednesday; auditable because it is written down

ALSO BYPASSABLE a filter can be talked around, and it is gone entirely if someone calls the model directly

## Page 25

01 02 03 ORGANIZATIONAL

THE LAYER YOU WILL ACTUALLY CONTROL

Ordinary management controls. The only novelty is how fast the system moves between checkpoints.

PERMISSIONS   What can it touch?

REVIEW   Who signs off before it counts?

In practice  Read the CRM and draft the email, but not send it. Query the ledger, but not post to it.

In practice  A person approves before anything reaches a customer, a contract or a payment.



What it prevents  an agent with more access than the intern would get

What it prevents  a confident, wrong output going out under your name

LOGGING   Can you reconstruct what happened?

SCOPE   Which decisions never get delegated?

In practice  Every input, tool call and action is recorded, so a bad outcome can be traced back.

In practice  Hiring, pricing, legal commitments stay with a person, whatever the model can do.



What it prevents  a failure nobody can explain, to a regulator or to yourself

What it prevents  delegation by default, one convenient step at a time

## Page 26

NO SINGLE LAYER IS SUFFICIENT

Each layer covers a gap the others leave. Only the third one is yours.

WHAT IT IS STRENGTH WEAKNESS

Opaque: no rule to audit, and only a tendency

Values and refusals learned into the weights during post-training

Durable: travels with the model everywhere

01 TRAIN-TIME owned by the labs

Fast: policy changes without retraining Bypassable: gone if the model is called directly

Filters and a written standard wrapped around the model

02 RUN-TIME owned by the labs, and harness builders

Only as good as the discipline behind it

Permissions, review, logging and scope set by the firm

Yours: ordinary controls you already know how to run

03 ORGANIZATIONAL owned by you

None of them is sufficient alone. We have talked about what the labs do. The next thirty minutes are about what you do.

## Page 27

CLAUDE NOW WATERMARKS ITS OWN OUTPUT (SINCE 9/1)

The mark lives in the model’s freedom to choose its words. Every strength and every limitation follows from that one fact.

1 It keeps choosing between near-equivalent words 2 A secret key tilts each choice 3 A detector replays the key

“Are these the picks the key would have made?”

The findings were …

SECRET KEY + THE WORDS SO FAR

notable

notable

- 
- 
- 
- ✗ ✗

striking

All four fit. The model picks one by a weighted coin flip, thousands of times per page.

striking

The coin is loaded. Same meaning, nothing added, no slowdown, but the pattern of picks is no longer random.

significant

significant

Enough matches and the odds of chance collapse. A statistical test, not a stamp: it needs many free choices to reach a verdict.

noteworthy

noteworthy

WHERE THE SIGNAL GETS THIN

Short passages too few choices to test

Factual, low-entropy text few words are actually free

Claude editing your writing nearly all the words are yours

A complete rewrite every replaced word removes the signal

Anthropic, Aug 2026 · based on Google DeepMind's SynthID-Text (Nature, 2024).

24 variant A

## Page 28

1 2 3 4 5 6

ONE BRIEF. ONE RUN. NO SECOND TRY.

hero-run-web.onrender.co m/

Laptops open. Join now.

## Page 29

PRACTICE — AS MANY RUNS AS YOU LIKE

hero-run-web.onrender.com/

8:00

Every run is graded.

Read the reasoning trace and the feedback. Adjust. Run again.

## Page 30

THE REAL ONE. UNSEEN TASK. ONE SUBMISSION.

6:00

hero-run-web.onrender.co m/

## Page 31

THE ROOM'S RESULTS

## Page 32

THERE WAS NO CLEVER WORDING

Hands up if you pasted

the whole task spec into the box.

## Page 33

1 2 3 4 5 6

EVALUATION AND RESPONSIBLE USE

## Page 34

YOU CANNOT DELEGATE ACCOUNTABILITY

Output carries your name.

1 Which claims would change my decision if they were wrong?

“Claude seemed confident”

is not an excuse.

2 What would that error cost, and to whom?

3 Can I check it against something authoritative?

## Page 35

CONSIDER THESE FOUR CHECKS

SPOT-CHECK

RED-TEAM

REPLICATE

TRACE

run it again, cold, and compare

verify a random sample and the edge cases

ask different models to argue against the output

numbers, quotes, citations, and causal claims back to a source

## Page 36

MATCH THE CHECK TO WHAT AN ERROR WOULD COST

the board memo

Stop thinking “is this good?”

And start thinking “good enough

for what?”

LOW COST → HIGH COST

your learning artifact

REVERSIBLE → IRREVERSIBLE

## Page 37

THREE THINGS TO TAKE WITH YOU

The deliverable format is a choice. Make it on purpose.

Think carefully about what the model needs to succeed.

Decide what you'd need to check before you need to have checked it.

## Page 38

WHAT SLOAN EXPECTS FROM YOU

- Use these tools in accordance with each class’s policies.

- Be mindful of with whom you share data and files.

- Be able to defend anything that carries your name.

## Page 39

KEEP AN EYE OUT FOR THE “THREE EXPERIMENTS” LAB

## Page 40

Austin van Loon  ·  vanloon@mit.edu      ·      Michiel Bakker  ·  bakker@mit.edu
