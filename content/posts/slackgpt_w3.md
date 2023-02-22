---
title: "#12 SlackGPT Week 3: Better answer quality and homepage"
date: 2023-02-22T23:26:03+01:00
draft: false
---
Hi and welcome to my weekly update! I’ve spent the past 3 weeks working on a Slack bot that answers business questions according to pre-defined frameworks - SlackGPT. A minimum-viable version of  SlackGPT is in progress. That includes a *working* bot that users can install onto their own Slack workspace and interact with from multiple touchpoints + a landing page. My self-imposed deadline (*see random thought below*) for this version is 28.02.23. 

> _Random thought: Have you ever wondered what happens when you miss a deadline? Nothing  happens, really. It’s not like you need to figure out the orbit transfer equation on time, or you’ll miss the connection to Mars. But they help make stuff happen. Deadlines cast shame on the deadline-missers, and people avoid shame at all costs. This is very… stick. We should have more deadline carrots. Good things should happen when you don’t miss a deadline._
> 

# **🛴Road to a working prototype**

So what needs to happen before 28.02.23. There are four main deliverables:

- ✅Improve answer quality
- ✅Build a homepage for the bot in Slack
- ➡️Build a landing page including an install button
- ➡️Handle user management

## ✅Improved answer quality

I was getting inconsistent insightfulness and formatting across questions. So I took a systematic approach to fix that. 

1. I defined 15 questions (personal, business & practical) to test with each framework
2. For each framework, I iteratively :
    a. Adjusted the prompts 
    b. Tuned the parameters (see [previous post](http://www.scortescu.com/posts/slackgpt_w2/#improving-results-from-gpt))
3. Fixed the final post-processing code

Interestingly, each prompt works better with different parameters, which makes it non-trivial to get reach an optimal point.  

Now, all prompts work all of the time, and answers tend to be insightful and well written. Here’s an example of a *negative scenario* for me deciding to learn software engineering while building my first software product

![bad](/slackgpt_w3/bad.png#center)

## ✅Build a homepage for the bot in Slack

A *homepage* is one of the multiple “surfaces” a bot can have within Slack. Along with *slash commands* and *shortcuts* it’s an entry point into the bot. While *slash commands* and *shortcuts* can be accessed anywhere from the text box, the bot homepage is like a user profile, but for a bot. It can also host text and media, which can help guide users the first few times they use the bot. 

![homepage](/slackgpt_w3/homepage.png#center)

Clicking on one of the buttons in the screenshot above opens the following modal:

![home_modal](/slackgpt_w3/home_modal.png#center)

Some ideas for future improvements include:

1. Add a tutorial for how to use the bot
2. Add the possibility to create profiles and context (e.g. write an answer relevant for the Customer Support department of a medium-sized French company)

## ➡️Build a landing page including an install button

A landing page, or website, provides a way to communicate about SlackGPT with potential users, and (for now) the only way to install the app. If you’re selling anything on the internet, and you don’t have a website, who even are you. 

### Landing page

Bad news: [slackgpt.com](http://slackgpt.com) and [slackgpt.app](http://slackgpt.app) have already been bought up in December.

![ohno](/slackgpt_w3/ohno.png#center)

Good news: I have a bit of progress into building the homepage: 

- Selected a tool: I’ll build the site with [carrd](https://carrd.co/) - it’s super simple to set up and cheap.
- Found a few examples to guide design: from my past research into slack apps, 2 have stood out with simple, appealing design and copy - [Kona](https://www.heykona.com/) and [HeyTaco](https://heytaco.com/)
- Defined the page structure:
    - Headline + subheadline + call-to-action
    - How it works + screenshots
    - Available frameworks
    - “coming soon ” features (e.g. message writing, summarization, etc.)

The challenge here will be to write super-clear attractive copy, make some visually pleasing designs without putting weeks of iteration.

### Install button

Really the most important action a user can take on the landing page is to install SlackGPT. There are two ways that an app can be installed into a Slack workplace:

1. Through the official Slack app [marketplace](https://slack.com/apps)
2. Through an unofficial link provided by Slack. This link goes on the landing page.

The approval process for 1 can take up to a a few months, and honestly SlackGPT is not there yet. But anyone can generate their unofficial install link. For SlackGPT, there’s still one thing to build before that: a way to handle user management.  

## ➡️Handle user management

Once people start installing the app, the bot will need to know who those people are and how (much) they use it. This will come handy in the future, if our bot aspires to remember things like users’ preferences, whether their free trial is over and whether they’ve subscribed already 🤑.  

Haven’t explored this part so far, but aren’t you super excited to read about it the next post?

# ****🗿Personal update: How’s it going, Stefan?****

Marathon training going great. Set a few personal records this week, with longest distance (19.5km), fastest 1km (4.8 min/km), fastest 5km (5.4 min/km)

More and more excited every day about the AI + Slack space. Partly because of the dopamine hits I get from learning things and solving problems + instant feedback. Partly because of some rabbit holes I’ve gone down on all kinds of new tools that will help make SlackGPT awesome.
