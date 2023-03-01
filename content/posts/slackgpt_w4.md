---
title: "#13 SlackGPT Week 4: Landing page and user management"
date: 2023-03-01T13:41:35+01:00
draft: false
---
Hi and welcome to this week’s update! It’s been a month since I’m working on SquidGPT - a Slack bot that answers business questions according to pre-defined frameworks. I was hoping to have a working, installable version of the bot by the end of February. It looks like I’ll be extending that deadline until next week (for now 😅) -  turns out user management is more difficult than I thought. 

Also, the bot has a new name - SquidGPT. Because squids are super smart & social. And I’m building an AI chatbot, so it fits. The bot will stay a squid, but the name may change, as domain names like [squidgpt.com](http://squidgpt.com) and a few others are already taken. 

# **🛴Road to a working prototype**

RIP old deadline of 28.02.23. New deadline 08.03.2022. Four main deliverables:

- ✅Improve answer quality - [see previous post](http://www.scortescu.com/posts/slackgpt_w3/#improved-answer-quality)
- ✅Build a homepage for the bot in Slack - [see previous post](http://www.scortescu.com/posts/slackgpt_w3/#build-a-homepage-for-the-bot-in-slack)
- ⚠️Build a landing page including an install button
- ⛔Handle user management

## ⚠️Landing page

Good news: I’ve finished a first draft of [SquidGPT’s landing page](https://squidgpt.carrd.co/) (screenshot below for future generations)

Not so good news: the install button doesn’t work - courtesy of still inexistent user management

![landing](/slackgpt_w4/landing.png#center)

I’ve built the page with [carrd](https://www.notion.so/13-SlackGPT-Week-4-Landing-page-and-user-management-aef4cc2e877d402eb6098f45d826e480), which makes it incredibly easy to produce. The landing page has six main elements:

- **Logo** - I built the logo with [dall-e](https://openai.com/product/dall-e-2), which is an AI for image generation. the prompt I used:`logo without text for a slack bot that answers questions. cartoonish squid minimalistic aesthetic. vector art illustration, made with illustrator, trending on artstation hq, deviantart, vibrant colors, digital art, concept art, logotype design, 8 khd post - processing, smooth, sharp focus`
- **Install button** - click on this to install the bot
- **Headers** - I’m still working on the right taglines for this bot, but they will only really get better after I talk to customers
- **How it works** - small tutorial showing how easy it is to get something useful out of 🦑
- **Features** - currently, that’s the four frameworks that SquidGPT can answer questions in
- **Pricing** - 🤑🤑🤑

Kind people have already shared some initial feedback which I will get to after finishing user management:

- Improve visuals
    - Replace How-it-works gif with step by step images that match the step-by step text.
    - Improve feature graphics quality (currently too simpl and large). Perhaps add actual results for each framework
    - Smaller fonts
- Make headline more specific - what kind of decisions will be made faster, for whom?
- Make smaller fonts, especially on mobile
- Figure out pricing - Is 1 week trial enough? Is 9$/month too high/low?

## ⛔Handle user management

I’ve underestimated how technically difficult user management would be. “User management” in the context of SlackGPT means being able to let users from any Slack workplace install the bot, and then have the bot respond to them on request. This requires implementing two pieces of software: an authentication flow and a place to store credentials. The authentication flow would take you to a page like the one below.

![auth](/slackgpt_w4/auth.png#center)

When a user clicks “Allow”, Slack generates a token (like a password of sorts) specific to that user and workspace. I need to store that token somewhere secure. When a user interacts with the bot, the bot can only answer back if it uses the right token.

The good news is that Slack’s software development kit helps handle the authentication flow + the storing and retrieving of credentials. The bad news is that: 1. This only works with certain types of databases (e.g. PostgreSQL and SQLite3); and 2. I’m having a hard time getting these databases (currently using a managed PostgreSQL database from AWS) to talk to my app.

I have a three possible solutions in mind, so there’s hope:

- Switch to a different *database* provider (e.g. Supabase) - their PostgreSQL implementation seems much friendlier than AWS’
- Switch to a different *app host* & *database* provider (e.g. Heroku) - there are some tutorials for Heroku serverless functions + databases for Slack bots. Not my favorite option, as I’ve got my app setup working with AWS Lambda
- *Handle authentication by myself*, instead of using Slack’s library - worst option as it involves rewriting large chunks of the bot + a bunch of code for the authentication flow and database stuff

## ****🗿Personal update: How’s it going, Stefan?****

Marathon training: taking an 8-day break from running, to be in full force on March 5th for the Paris semi-marathon 

Excited to have an old friend from university visiting me this weekend. Spring promises to be interesting, with at least 3 other visits planned by May.  

Also feeling kind of anxious & frustrated about missing my end-of-February deadline.

# ➡️Next steps

For now, I’m heads down trying to hack my way into an installable bot by setting up user management. Once that’s done, I’ll start working on and executing a customer development plan, which should be the focus for March
