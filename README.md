Tone Architect: An AI Linguistics Discord Bot

## Overview
Tone Architect is a localized Discord bot that acts as a conversational co-pilot. By using the OpenAI API and applying core linguistic principles (Grice’s Maxims and Politeness Theory), the bot analyzes user messages to determine their underlying "vibe" and generates three possible contextual rewrites: softened, professional, and direct.

## Tech Stack & Unit Economics
Language: Python (discord.py)

LLM Engine: OpenAI gpt-4o-mini

Unit Economics: Used gpt-4o-mini to keep operational inference costs under $0.001 per user interaction, proving highly scalable product margins.

Data Tracking: Built-in Python CSV logger for local latency and performance metric tracking.

## Beta Testing & User Insights (MVP Launch)
To validate the product's core hypothesis, I deployed the MVP to a closed beta test with university students and software engineers, gathering both quantitative backend metrics and qualitative user survey data.

Quantitative Metrics (Backend CSV Logging):

Total Interactions: 23 distinct API calls.

Average Latency: 3.36 seconds (Ranged from 1.95s to 5.88s due to OpenAI API fluctuation).

Vibe Score Spectrum: Analyzed inputs ranging from 0/100 ("Aggressive/Threatening") to 85/100 ("Warm/Inviting"), with an average score of 38/100, proving successful handling of blunt/passive-aggressive edge cases.

Qualitative Feedback (User Survey):

Tone Accuracy: 100% of surveyed users reported that the AI perfectly understood and correctly categorized the tone of their original message.

Perceived Latency: Despite a 3.36s actual latency, 100% of surveyed users rated the bot's response time as "instant," indicating high user tolerance for generation wait-times within a Discord chat environment.

The "Co-Pilot" Behavior: 66.7% of users stated they would edit the AI's generated text before sending it, rather than copying it verbatim. This validates that the tool's product-market fit is as a drafting assistant, not an absolute replacement for human communication.

## Iterative Roadmap (V1.1 Planned Fixes)
User feedback highlighted three critical areas for the next iteration:

Prompt Tuning: Users noted the "Direct" rewrite occasionally produced unnatural, robotic phrasing. The System Prompt will be updated to enforce stricter conversational boundaries.

Scoring Logic Bug: A user discovered that re-feeding the bot its own suggested replies sometimes yielded a lower Vibe Score than the original blunt message. V1.1 will implement comparative anchor logic to stabilize the algorithm.

Friction Reduction: Survey completion dropped off by 37.5% due to the friction of clicking an external Google Form link. Future versions will integrate Discord Reaction Emojis for frictionless, in-app data collection.
