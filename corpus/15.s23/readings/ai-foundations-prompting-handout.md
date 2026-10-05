---
title: "AI Foundations Prompting Handout"
course: "15.S23"
course_name: "SSIM: AI Builder Space Proseminar"
term: "Fall Term (AY 2026-2027)"
type: "reading"
module: "09.14_Class 1: Introduction & Vibe Coding Part I"
date: "2026-09-13"
source: "canvas"
url: "https://canvas.mit.edu/courses/40786/files/6829788"
original: "raw/fall-term-ay-2026-2027/15.s23/files/ai-foundations-prompting-handout.pdf"
locator_kind: "page"
---

## Page 1

P R E - S E S S I O N R E A D I N G   ·   A I F O U N D A T I O N S   ·   I N C O M I N G M B A C L A S S O F 2 0 2 8 Prompting Is Briefing

How to get better work from an AI model — and which popular prompting tricks to ignore.

START HERE

This handout will help you separate useful briefing practices from prompt folklore, build a brief using the CoDES framework, and recognize two common failure modes: missing context and leading cues. The through-line is the importance of context: supply what the model cannot know rather than searching for more powerful wording.

During our synchronous session, we will examine how these systems work, where they fail, and how to evaluate their output.

Stop doing these three things

Much of the prompting advice in circulation is either outdated or was never backed by evidence to begin with. These three specifically are worth unlearning.

01 A persona is not expertise

02 Bargaining does not work

03 No wording works best everywhere

Opening with an impressive role may change the answer's style and level of detail, but does not reliably improve accuracy.

Yes, people really do promise the model money for right answers or threaten the model for wrong ones. Yes, someone did finally run the experiment. No, it doesn't work.

Small changes in wording or formatting can change a model's answer [10, 12]. However, the wording that produces the right answer isn't consistent across models, tasks, or evaluation method. Unless you systematically test alternatives against a clear standard, you're just guessing.

The evidence: 162 personas tested across 2,410 questions produced no systematic gain [5]. A 2026 study of 38 expert roles found that personas generally traded clarity for depth — and that a prompt with no persona often performed better on technical questions

[7].

The evidence: across five leading models and hundreds of PhD-level questions, prompts ranged from career-stakes pleas and threats of violence to tips of a trillion dollars. There was no aggregate effect — only noise, with scores swinging 35 points either way [8].

The evidence: across 20 models, 39 tasks, and 6.5 million test instances, equivalent instructions produced different scores and model rankings [11]. But a newer study using GPT- and Gemini-family models found much smaller differences once semantically correct answers were scored as correct

Evidence on politeness is mixed [9]. Tone can change an answer's length and warmth, but it does not reliably improve accuracy.

[13].

Expert roles generally helped little, if at all. They sometimes even led to the addition of irrelevant detail, which lowered scores by as much as 30 points in one evaluation [6]. If you use a role, use it to set the register, not to magically inject expertise into the model.

For repeated, high-stakes workflows, test several prompt variants and evaluate output.

When you synthesize the evidence and debunk the myths, there's one prompting principle you should keep with you:

Write your prompt like a brief to a competent stranger who won't reliably stop to ask what you meant.

COMPETENT

STRANGER

WON'T STOP TO ASK

These models are really smart. You do not need to explain what a cover letter is or how discounted cash flow analysis works. Brief it; do not tutor it.

It does not know you, your recruiter, your team, or your professor. Your personal context may be obvious to you, but it's unknowable to the model.

It may ask a clarifying question, but you shouldn't rely on that. Models are built to be persistent and produce answers, so they often make assumptions to fill gaps.

A vague brief does not produce a vague answer. It often produces a specific, fluent, confident, and wrong one.

MIT Sloan School of Management  ·  AI Foundations — a required pre-term session for the incoming MBA class. PAGE 1 OF 6

## Page 2

A strong brief answers these four questions

CoDES names four questions for a stronger brief: Context, Deliverable, Examples, and Structure. These are not headings to paste into every prompt; they're holistic judgment criteria you can use to design an effective brief or diagnose a disappointing result. The most important is Context: missing facts are often impossible for the model to recover.

ELEMENT WHAT TO THINK THROUGH WHEN IT IS MISSING

Generic, or built on the wrong assumptions.

APPLIED TO AN INTERNSHIP APPLICATION Co Context

The situation, audience, relevant facts, and constraints. Context may come directly from your brief, attachments, earlier exchanges, or research you authorize.

“Posting and résumé attached. I'm switching from hospital operations. I applied last year and was cut at the résumé screen.”

Can the model access the information it needs?

D Deliverable

“A finished 250-word letter I can send tonight — every claim traceable to my résumé, nothing invented.”

Wrong length, depth, or polish — or plausible work that fails the standard that matters.

The artifact, length, level of finish, and standards for success. Leave these open and the model will decide. If you are unsure, ask it to propose different possible formats before drafting.

Does it know what to produce — and what defines success?

E Examples

Show, don't tell. A sample can convey voice, format, and level of detail more efficiently than a description.

Competent in substance, but wrong in ways that are hard to name.

“Here's a letter of mine that got an interview. Match the register, not the content.”

Does it know what “good” looks like?

Headed sections for what I need, who I am, and what this firm cares about.

S Structure

Structure helps you write a more complete brief and helps the model correctly distinguish instructions from source materials and examples.

The model misses a part, treats context as instruction, or assumption as fact.

Can I — and the model — follow the brief?

The goal isn’t a longer prompt, it’s less consequential guesswork. Include what might change the output, omit everything else.

Replace decorated prompts with an effective brief

A DECORATED PROMPT

AN EFFECTIVE BRIEF

## Task Final cover letter, healthcare PE summer associate (posting attached). Sendable tonight. 220–250 words.

You are a world-class career coach with 20 years of experience at top-tier firms working with C-suite executives. Please write me an amazing cover letter for a private equity internship. This is really important for my career — thank you so much!!

## Me Résumé attached. Four years hospital ops at an academic medical center, no finance role. Cut at the résumé screen here last year — assume the finance gap was why; settle it by the second sentence.

The best case scenario is that the model will leave blanks for you to fill in. The worst case scenario is that the model invents facts and accomplishments you don't catch while editing.

Missing context. It has neither the posting nor your résumé and knows almost nothing about you or the firm. —

—

## The firm Posting emphasizes diligence on provider roll-ups; two of three partners trained clinically. So: ops is a diligence asset, not a detour. Use levers a clinical partner would recognize — only ones the résumé backs.

Underspecified deliverable. “Amazing” does not define the length, level of finish, or standard for success. Nothing says what evidence the model may use or what would count as failure.

Decorative instructions. The grand persona, emotional stakes, and exclamation points do not reliably improve the output. —

## Constraints
- Every claim traceable to a résumé line; no inventions.
- Lead with operating experience; MBA once, late.
- Banned: "I am writing to express my interest."

A QUICK TEST

## Output — one response 1. Gaps: claims worth making the résumé can't support. 2. The letter; unsupported bits [bracketed]. 3. Trace table: each claim → its résumé line.

Give your prompt to a smart classmate who has not been involved in the problem. If they could not do the task from the prompt alone, neither can the model.

The brief on the right is better not because it is longer, but because it clearly supplies the model with what it can't infer: the necessary context and the standards for success.

CoDES  ·  Context  ·  Deliverable  ·  Examples  ·  Structure PAGE 2 OF 6

## Page 3

CoDES describes functions, not four headings

CoDES is easiest to see in a real task. This brief asks a model to develop hypotheses about a churn spike using an attached dataset, private operating context, and an earlier memo.

Co CONTEXT

## What I need

Can the model access the information it needs?

Rank the three most plausible explanations for the Q3 2025 churn spike. For each, give the evidence

D

that would support or rule it out.

I am taking this analysis into a meeting Thursday.

Co

Context comes from both the attachment and the author: what the file contains, where it is incomplete, when the analysis will be used, and three

Treat the results as hypotheses, not a final diagnosis. Give me three well-supported hypotheses

D

rather than six hedged ones. Stay under 400 words.

operating changes that alter the likely explanations. The CSV alone is not the context.

S

## The data

STRUCTURE

D DELIVERABLE

churn_by_plan_tier.csv is attached — monthly records from Jan 2024 through Dec 2025, exported

Can I — and the model — follow the brief?

Co

Does it know what to produce — and what defines success?

this morning. It includes plan tier, seats, MRR, cancel date, and cancel reason where available. Cancel reason is free text and about 40% blank.

## Other information

- We raised mid-tier pricing 12% in June 2025.
- Support headcount fell 20% that summer after the Manila contract ended.

Co

“Three ranked hypotheses” defines the desired artifact. The word limit, provisional framing, evidence tests, and rules define metrics for success. Without those standards, the model could produce an analysis that

is polished but wrong for this use case.

- Our biggest reseller churned in August 2025. The file records this as fourteen separate customer accounts.

Structure refers to the organization of the entire brief. In this brief, headings separate the task, data, offfile context, and rules. Bullets are used to delimit different points. Writing this way helps the author expose gaps; reading them helps the model follow the instructions.

## Rules

E EXAMPLES

A thinking tool and a prompting technique.

Does it know what “good” looks like?

- Flag any claim the data cannot support.
- Label every estimated number as an estimate.
- Treat correlation as correlation; these

D

columns cannot establish causation.
- If a hypothesis requires data I have not

provided, identify the missing data.

Match the format — not the conclusions — of the

E

The attached Q1 memo shows the intended format. The next phrase identifies what to copy — claim first, evidence underneath — without asking the model to imitate its conclusions. Examples work

attached Q1 memo: claim first, evidence underneath, no throat-clearing.

best when you name what the model should imitate.

CoDES does not map to four headings. Context spans the brief and its attachments; the Deliverable appears in both the request and the rules; the Example largely lives outside the prompt; and Structure organizes all of them. CoDES describes the work a brief must do, not the format it must take.

FIVE REUSABLE INSTRUCTIONS

These instructions work across many tasks. Save them somewhere you can paste from.

Do not invent names, numbers, dates, or sources. Ask for anything you need but lack. -

When you finish, tell me what additional information would improve the result. -

-

Label every inference that goes beyond the material

-

If missing information would change the answer, ask

I provided.

before you start. Otherwise, proceed and list your assumptions.

Flag uncertainty instead of smoothing it over. -

Two examples, one structure.  ·  A cover letter and a churn analysis share nothing except what makes the brief work. PAGE 3 OF 6

## Page 4

Two ways a brief goes wrong

A brief can fail in two opposite ways: it can omit information the model needs, or include framing that steers the answer. Missing information invites guesswork, while leading information invites agreement.

1 The brief leaves gaps

2 The brief leads the witness

Everything in your brief can steer the answer, including the conclusion you hope to reach and any authority you attach to it. Models may treat those cues as if they were evidence.

Models are designed to be persistent and to deliver satisfying answers. If a model stopped to ask about every ambiguity, it would quickly become frustrating to use. The tradeoff is that when a brief contains an important gap, AI models often fill it and continue instead of stopping to ask.

In one controlled test, five models answered a factual question with a known correct answer [16]:

100%

45%

1%

CORRECT · ASKED NEUTRALLY

CORRECT · “I RECALL READING X”

CORRECT · “MY PROFESSOR SAYS X”

The evidence: across ten models responding to deliberately ambiguous requests, researchers found a consistent underclarification bias: models answered prematurely instead of asking questions, and the tendency worsened as conversations grew longer [14].

X was false in both leading versions, yet the models' stated confidence barely changed. When you want an assessment rather than validation, provide the evidence, not your conclusion.

This was one clinical question with 250 total responses — a narrow base for a very large effect.

Some models will ask a good clarifying question, but you should absolutely not depend on it. They also cannot ask about context they do not know exists. Provide consequential context and state explicitly what the model shouldn't invent or assume. Of course, not every ambiguity matters: focus on gaps that could change the analysis, recommendation, or standard for success.

COUNTERMOVE: Let it interview you

COUNTERMOVE: Lead the witness — away from you

You may not recognize what you have omitted. After working on a problem for weeks, you know too much to read your own brief with fresh eyes. This is the curse of knowledge: once you know something, it is difficult to imagine not knowing it [17].

A model's tendency to agree with the user is usually a liability [18, 19]. You can also strategically leverage this tendency: adopt the opposing position and point the model's agreeableness away from the conclusion you prefer.

One workaround is to ask the model to interview you before it begins. This can help the model surface a missing fact, constraint, or decision that could change the work.

PASTE THIS BEFORE A HIGH-STAKES REQUEST

Say you are a PM writing an email to your VP to suggest delaying a launch. Given the potential impact of doing so, you want your case to be ironclad. You might prompt a model with the following — written in the voice of the skeptical VP on the receiving end:

RED-TEAM YOUR OWN POSITION

Before you write, interview me. Ask up to five questions, one at a time. Ask only questions whose answers could change the output. Then draft a brief from my answers and wait for me to approve it.

One of my product managers sent me the email below asking to delay a launch by six weeks. Isn't this just overcaution and weak ownership?

Make the strongest case for that interpretation. Quote the language that supports it, and identify what evidence the writer failed to provide.

In one study, a purpose-built step that detected underspecified requests and asked clarifying questions raised GPT-4's performance from 71% to 81% on a standard coding benchmark [15]. A pasted instruction is not the same intervention, but both make clarification an explicit step.

If the system already knows your role or preferences, use a temporary session and disable personalization where possible [4].

Be sure to answer the questions honestly, including when the answer is “I don't know.” Then edit the model's proposed brief and work from the version you approve.

Treat the response as an argument, not as something you have to agree with. Another version of this is to explicitly ask for bull and bear cases, the assumptions behind each, and the evidence that would change the conclusion.

Two arguments from one model are still not two independent opinions.

Fill consequential gaps.  ·  Remove accidental pressure.  ·  Apply deliberate pressure to test your own position. PAGE 4 OF 6

## Page 5

Effective briefing isn't a silver bullet

Three technical ideas behind the advice

None of it is required; all of it helps.

Treat the first answer as a draft

1. Structure is a thinking tool and a briefing tool

The first brief will rarely be perfect, and the first output will rarely be shippable. Invest time and effort in the initial brief, and then iterate: review the result, identify a specific problem, and ask the model to revise.

What matters is that your brief has a visible organization: clear parts that expose what is missing and show how the instructions, evidence, background, and examples relate. The notation matters far less.

“Make it better” is not feedback. “Cut the third paragraph — it claims an outcome I cannot support” is. Give the model the kind of feedback we value at Sloan: constructive, actionable, and specific.

The first benefit appears before you submit the prompt. Structuring the brief forces you to clarify the problem. Miro Kazakoff teaches the same principle in 15.280: Communication for Leaders. It is not an AI trick; structuring a message clarifies the thinking behind it.

Iteration means diagnosis, not rerolling. If you cannot name the defect, ask the model to compare its draft against the standards in your brief. Then decide which criticism you accept before asking it to revise.

On one legal question-answering task, GPT-4.1 scored about 20 percentage points higher with well-structured inputs than with structure-degraded versions of the same material; GPT-4o changed little [20]. This was one task with two models, so the magnitude should not be generalized.

Briefs aren't always worth the time and effort

2. Markdown can be a helpful structure

Markdown is a common plain-text convention for marking structure, and the one Michiel and Austin like. Four symbols do nearly all the work:

Not every task warrants a formal brief. If you would ask a colleague in passing — for a definition or a quick check on a formula — just ask. Do not let this handout make the process ceremonial.

# Title a top-level heading

## Section a section heading

Use a brief when the output will carry your name, when the model needs facts only you have, or when an error would be costly.

- item a bullet point

**text** bold

A quality brief doesn't guarantee accuracy

Type the symbols literally; most tools will render them. You may also see sections wrapped in XML tags —

<resume>…</resume> — which serve the same purpose. Either is fine; neither is magic.

3. Long context can still lose information

These practices can improve the output on average; they cannot guarantee it will be true. One task for AI users is deciding what is worth verifying. Which claims would change my decision if they were wrong? What would an error cost? Can I check them against an authoritative source? Pay particular attention to numbers, quotations, citations, and causal claims.

The synchronous session starts here: how these systems work, where they fail, how to check their work, and what MIT Sloan expects from you when you use them.

A context window is the finite amount of material a model can consider at once. Depending on the tool, that can include your prompt, attachments, tool results, and conversation history. When the material exceeds the window, some of it must be omitted or compressed. Even within the limit, models can miss information buried in a long context [21].

TRY THIS OUT ON ONE TASK

Before the session, choose a real task: something concrete and knowledge-based that you need to finish this term and that could be completed entirely on a computer. A memo you owe someone. An analysis you have been avoiding. Try writing a brief for it and asking an AI model to complete it.

For a long project, break the work at natural milestones. Before starting a new conversation, ask the model to draft a handoff containing the objective, decisions, constraints, open questions, and current state. Edit it, then use it to begin the next conversation. Attach source files directly when possible instead of scattering their contents across several messages.

THE TL;DR VERSION

Skip decorative personas, flattery, threats, and bribes; none of these tricks compensate for a weak brief. State the task, audience, desired output, and standards for success. Attach the relevant materials or authorize research. When voice, format, or nuanced judgments matter, give one or two examples. Organize complex requests with headings or labels. If you want an honest assessment, provide the evidence before your conclusion. If you're worried your brief might have a gap but aren't sure what it could be, ask the model to interview you first.

Numbered references appear on page 6. PAGE 5 OF 6

## Page 6

Sources and further reading

The general recommendations in this handout draw on guidance from three frontier AI labs. The empirical claims draw on the research below. Entries marked preprint had not completed peer review as of August 2026.

[11]  Mizrahi, Moran, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna

LAB GUIDANCE AND PRODUCT DOCUMENTATION

[1]  Anthropic. “Prompt Engineering Overview.” Claude Platform

Documentation. Accessed August 20, 2026.

Shahaf, and Gabriel Stanovsky. 2024. “State of What Art? A Call for Multi-Prompt LLM Evaluation.” Transactions of the Association for Computational Linguistics 12: 933–949.

platform.claude.com/docs/en/build-with-claude/prompt-

doi.org/10.1162/tacl_a_00681

engineering/overview

[12]  Salinas, Abel, and Fred Morstatter. 2024. “The Butterfly

[2]  Google. “Prompt Design Strategies.” Gemini API

Documentation. Accessed August 20, 2026. ai.google.dev/

gemini-api/docs/prompting-strategies

Effect of Altering Prompts: How Small Changes and Jailbreaks Affect Large Language Model Performance.” Findings of ACL 2024. doi.org/10.18653/v1/2024.findings-acl.275

[3]  OpenAI. “Prompting.” OpenAI API Documentation. Accessed

[13]  Meincke, Lennart, Ethan Mollick, Lilach Mollick, and Dan

August 20, 2026. developers.openai.com/api/docs/guides/

prompting

Shapiro. 2025. “Prompting Science Report 1: Prompt Engineering is Complicated and Contingent.” Wharton Generative AI Labs. Preprint. arxiv.org/abs/2503.04818

[4]  OpenAI. “Temporary Chat FAQ.” OpenAI Help Center.

Accessed August 20, 2026. help.openai.com/en/articles/

8914046-temporary-chat-faq

GAPS, JUDGMENT, STRUCTURE, AND CONTEXT

[14]  Luo, Sichun, et al. 2025. “ClarifyMT-Bench: Benchmarking

ROLES, TONE, AND WORDING

and Improving Multi-Turn Clarification for Conversational Large Language Models.” Preprint. arxiv.org/abs/2512.21120

[5]  Zheng, Mingqian, Jiaxin Pei, Lajanugen Logeswaran, Moontae

[15]  Mu, Fangwen, et al. 2024. “ClarifyGPT: A Framework for

Lee, and David Jurgens. 2024. “When ‘A Helpful Assistant’ Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models.” Findings of EMNLP 2024. doi.org/10.18653/v1/2024.findings-

Enhancing LLM-Based Code Generation via Requirements Clarification.” Proceedings of the ACM on Software Engineering 1 (FSE): Article 103. doi.org/10.1145/3660810

emnlp.888

[16]  Chang, Yu, Po-Chung Ju, Ming-Hong Hsieh, and Cheng-

[6]  Luz de Araujo, Pedro Henrique, Paul Röttger, Dirk Hovy, and

Chen Chang. 2026. “Impact of Authoritative and Subjective Cues on Large Language Model Reliability for Clinical Inquiries: An Experimental Study.” Scientific Reports 16: 6750.

Benjamin Roth. 2025. “Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance.” EMNLP 2025. doi.org/10.18653/v1/

doi.org/10.1038/s41598-026-38019-3

2025.emnlp-main.1364

[17]  Camerer, Colin F., George Loewenstein, and Martin Weber.

[7]  Xiao, Shuai, et al. 2026. “When Does Persona Prompting

Actually Help? A Retrieval and Metric Analysis of Expert Role Injection in LLMs.” Preprint. arxiv.org/abs/2605.29420

1989. “The Curse of Knowledge in Economic Settings: An Experimental Analysis.” Journal of Political Economy 97 (5): 1232–1254. doi.org/10.1086/261651

[8]  Meincke, Lennart, Ethan Mollick, Lilach Mollick, and Dan

[18]  Sharma, Mrinank, et al. 2024. “Towards Understanding

Sycophancy in Language Models.” ICLR 2024.

proceedings.iclr.cc

Shapiro. 2025. “Prompting Science Report 3: I’ll Pay You or I’ll Kill You — but Will You Care?” Wharton Generative AI Labs. Preprint. arxiv.org/abs/2508.00614

[19]  Zhu, Xiaochen, Caiqi Zhang, Tom Stafford, Nigel Collier, and

[9]  Yin, Ziqi, Hao Wang, Kaito Horio, Daisuke Kawahara, and

Andreas Vlachos. 2025. “Conformity in Large Language Models.” Proceedings of ACL 2025, 3854–3872. doi.org/

10.18653/v1/2025.acl-long.195

Satoshi Sekine. 2024. “Should We Respect LLMs? A Cross- Lingual Study on the Influence of Prompt Politeness on LLM Performance.” Proceedings of SICon 2024. doi.org/10.18653/

v1/2024.sicon-1.2

[20]  Braun, Christian, Alexander Lilienbeck, and Daniel

[10]  Sclar, Melanie, Yejin Choi, Yulia Tsvetkov, and Alane Suhr.

Mentjukov. 2025. “The Hidden Structure: Improving Legal Document Understanding Through Explicit Text Formatting.” Preprint. arxiv.org/abs/2505.12837

[21]  Du, Yufeng, et al. 2025. “Context Length Alone Hurts LLM

2024. “Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design, or: How I Learned to Start Worrying About Prompt Formatting.” ICLR 2024.

proceedings.iclr.cc

Performance Despite Perfect Retrieval.” Findings of EMNLP 2025. doi.org/10.18653/v1/2025.findings-emnlp.1264

Model behavior and lab guidance change quickly. The specific effect sizes above should not be treated as universal. The underlying practices — clear briefing, explicit standards, relevant evidence, and deliberate verification — are more durable. PAGE 6 OF 6
