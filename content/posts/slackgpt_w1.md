---
title: "#10 SlackGPT Week 1 progress update"
date: 2023-02-08T23:34:39+01:00
draft: false
---
Hi and thanks for coming to my blog!

In my last post I wrote about committing to build a Slack app that gives access to the GPT AI language model. This week I’ve thought more about what exactly this app should be doing and also had great progress in building a prototype. In this post, I will be covering:

- 🔭 **Vision**: When my bot grows up, what will it become?
- 🛴**Minimum Viable** **Product**: Current state and what’s still missing
- 🗿**Personal update:** How’s it going, Stefan?
- ➡️**Next steps:** Step nexts

# 🔭Vision: When my bot grows up, what will it become?

The vision for the bot is to serve as a business analyst working for decision makers and the teams that support them. It is targeted at CEOs, consultants (internal and external), and (real 😀) business analysts across strategy and operations functions. These people often need to think about ambiguous business problems in structured, analytical ways. 

However, they might miss some pieces of the puzzle due to their own or their organization’s blind spots. Sometimes, they hire consultants to help them reason through & communicate about problems, and hopefully bypass blind spots. These consultants can be expensive, hard to hire, and perhaps not needed on a full-time basis. 

SlackGPT (working title, better ideas are welcome) could help with the early problem-solving work, like ideation, and structuring an analysis. It could also help them consume large amounts of information and understand its implications. Finally, it could help them imagine the future and plan accordingly, as well as write up arguments to persuade stakeholders to act on their recommendations. 

Of course, you could just use ChatGPT to answer your business questions. So why SlackGPT? Two reasons: 

1. ChatGPT is a blank slate. This means that you need to give it more than a simple question, to get a good answer out of it. You need to explain to it what you expect from the answer. SlackGPT gives the user a choice of frameworks through which it can analyze a business question. Behind the scenes it does the explaining for you. 
2. ChatGPT lives on it’s own [webpage](https://chat.openai.com/chat), while most people spend their working time in their usual business tools: email, slides, spreadsheets, chat (Slack anyone?), etc. SlackGPT lives in… Slack. 

In a nutshell, you will be able to give SlackGPT a question or instruction, choose a framework, and get back a structured answer. Some examples:

- Answer [this question] for me using [scenario analysis]
- Synthesize [this article] for me using [the Pyramid Principle]
- Rewrite [this message] for me to [make it more persuasive]

![vision](/slackgpt_w1/vision.png#center)

This is a work in progress. If you’re reading this and have some ideas, please share them with me. One thing I know I need to refine is the target audience I wrote about in the beginning. That would also help make the frameworks and use cases more specific. 

# 🛴**Minimum Viable** **Product**: Current state and what’s still missing

I’m currently working on building a prototype or Minimum Viable Product of SlackGPT. 

## Current state

The goal for this week was to get the bot to answer questions through four different frameworks: Cost/Benefit, Pro/Con, Strengths/Weaknesses/Opportunities/Threats and Scenario Analysis. 

To do this, I started by doing some [prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api), to make sure that when the user asks a question in a given framework, the answer that comes back is meaningful, and is properly structured. I then worked on processing the answers from OpenAI, so that they can consistently be sent to a Slack channel. Finally, I updated the image generating [bot I built in December](http://www.scortescu.com/posts/chatbot/#what-i-learned-by-building-an-ai-powered-chat-bot) with the shiny new question-answering capabilities.  

Here’s an example of how the bot answers to a scenario analysis for “I decide to write a blog about building my startup”. 

![prompt](/slackgpt_w1/prompt.png#center)

![prompt_answer](/slackgpt_w1/prompt_answer.png#center)

I’m expecting three different scenarios: 👍Positive, 👉Neutral and 👎Negative, including possible further developments.

![scenario_1](/slackgpt_w1/scenario_1.png#center)

![scenario_2](/slackgpt_w1/scenario_2.png#center)

![scenario_3](/slackgpt_w1/scenario_3.png#center)


It works! It doesn’t always work (some questions throw it off), and the quality of the answers can be improved, but it works! For example, in the answer above, the three scenarios should actually be different from each other. There should be a positive, negative and neutral scenario, and each scenario should have a different title. The bot does give positive, negative and neutral scenarios, but the titles are all the same. Also, there could be more variation in the answers. 

## What’s still missing

There are a ton of things that need to happen before I’ll be able to call this a working prototype:

- Content capabilities:
    - More frameworks, such as:
        - “Work backwards - what Y needs to happen for X to be true”
        - “What are the assumptions behind X”
        - “Write a persuasive argument for X”
        - “Rewrite X to be more polite/non-violent/customer friendly”
    - Better answer quality
    - Add perspectives/profiles - answer all the framework questions from the point of view of a designer/Elon Musk/a dog/[build your own profile]
- User interface improvements:
    - Build a homepage in Slack for the bot, to help users get started and change settings
    - Add modals - a way for users to interact with the bot that gives more guidance than the /slash commands in the pictures above, like how Slack does it for its built in reminder feature, see below
    
    ![modal](/slackgpt_w1/modal.png#center)
    
- A webpage where users can learn about and install the bot
- Getting the bot ready to be installed on other organization’s workspaces. This includes:
    - User management
    - Extra security
    - A way to charge money
    - A bunch of other things

# 🗿**Personal update:** How’s it going, Stefan?

I’m feeling super positive after a week of building. The more I build the more ideas and inspiration I get. 

Fully recovered from my cold and on track for my half-marathon training.

I started two new books that I’m finding very interesting so far: [The House in the Cerulean Sea](https://www.goodreads.com/book/show/45047384-the-house-in-the-cerulean-sea) and [Don Quixote](https://www.goodreads.com/book/show/3836.Don_Quixote) 

Finally, I’m excited to be going to Strasbourg for a long birthday weekend!

# ➡️**Next steps:** Step nexts

- Keep working on the MVP. The goal for this week is to tune the answers to the frameworks I already built and build out at least 1 and maybe 2 more frameworks
- Come up with a better name than SlackGPT