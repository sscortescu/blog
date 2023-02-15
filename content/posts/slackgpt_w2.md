---
title: "#11 SlackGPT Week 2: Answer quality sorrows"
date: 2023-02-15T18:59:21+01:00
draft: false
---
Hi and welcome to my weekly update, where I write about the day-to-day of my attempt at entrepreneurship. [Last week](http://www.scortescu.com/posts/slackgpt_w1/) I wrote about my vision for the Slack app that I’m building, and what needs to get done on the way to a working prototype. In this post I share some updates on said prototype.  

# 🛴Road to a working prototype

This week, I’ve been focused on two things: **improving results from GPT** and **building a running slack app** with slash commands and shortcuts. In terms of the day-to-day, this involved hitting new technical walls, bugs and things I’ve never done before followed by reading lots of documentation and Stackoverflow  posts, and most of all trying stuff. 

## Improving results from GPT

SlackGPT can currently answer questions through four different frameworks: Cost/Benefit, Pro/Con, Strengths/Weaknesses/Opportunities/Threats and Scenario Analysis. Currently, this works *sometimes*. *Sometimes* it doesn’t finish writing the answer completely. *Sometimes* it writes out something trivial like “expanding to new markets is great because it leads to expanding the company”. And *sometimes* it can… become confused 😖 

![bla.png](/slackgpt_w2/bla.png#center)

I’m using a few tools to tune the outputs from GPT:

- **Prompt engineering**: Writing better questions to ask the AI has helped me get more consistent results. This includes asking the model to follow a sequence of steps when generating its analyses and asking it to think critically.
- **Model parameters:**
    - **Temperature**: This is a parameter that makes the bot choose more or less improbable answers. Higher temperature means more randomness and potentially more creativity.
    - **Repetition penalties:** Sometimes the model tends to repeat itself. There are some parameters to help prevent this. However, setting these too high leads to inconsistent formatting. That prevents proper postprocessing of results.

Currently, after trying many different combinations, the improvement in answer quality doesn’t feel stellar. However, it looks like I’ll just have to keep trying if I want a consistently good experience. Otherwise the product won’t work. 

## **Building a running slack app**

Last week, I already had a running slack app with slash commands. Slash commands are a way to call a slack bot from the text input field.

![slash.png](/slackgpt_w2/slash.png#center)

However, one of the things that SlackGPT wants to do well, is to make it as easy as possible to get good answers out of AI. Writing out a slash command means one needs to remember a command for each framework, or specify the framework within the prompt. Neither of those is very user-friendly. 

So I’ve been working on implementing modals in the app. A user can now click on the “Shortcuts” button and chose to Create an analysis.

![shortcut.png](/slackgpt_w2/shortcut.png#center)

They can then select a framework (work in progress), choose where to get the answer and write out their questions, all in a dedicated modal.

![modal.png](/slackgpt_w2/modal.png#center)

## What’s still missing

After working on SlackGPT for 2 weeks now, it feels like I should soon have something that others can try. Therefore, I’m setting myself a deadline to publish the bot by the end of February. In my previous post I’ve mentioned that [what](http://www.scortescu.com/posts/slackgpt_w1/#whats-still-missing) needs to happen for me to call it a working prototype. 

To make it for the 28.02 deadline, I will deprioritize adding more frameworks, adding context, implementing billing and security. That means that the next 2 weeks, I’ll:

- Improve answer quality
- Build a homepage for the bot in Slack
- Build a landing page including an install button
- Handle user management

It’s an optimistic timeline, but I feel like the need for better execution momentum! 

Once published, I’ll start working on marketing and sales, including: writing more publicly (Twitter and LinkedIn), reaching out to potential customers. 

# 🗿**Personal update: How’s it going, Stefan?**

The long weekend in Strasbourg was awesome! It was great to be surrounded by caring people. Also got to make some chicken BBQ which ended up tasting fantastic.  

Marathon training going well. Now trying to improve the pace to better than 5:30 min/km

Finally, despite light frustration with code bugs and slow progress on answer quality, I feel great about this project! It’s only been two weeks, but I feel like I’ve learned so much! In particular, I can see a close future where I’ve built a reusable Slack app skeleton. That would make building any future apps faster and easier.
