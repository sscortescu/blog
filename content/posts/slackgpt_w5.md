---
title: "#14 SlackGPT Week 5: User management and OpenAI’s own Slack bot"
date: 2023-03-08T19:13:40+01:00
draft: false
---
Hi and welcome to this week’s update! This week I was heads down coding the bot installation and user management. I finished that in good time and spent some time iterating implementing first feedback in SquidGPT’s website + some minor formatting improvements in the actual app. Finally, today I found out OpenAI is working on their own Slack app (⚠️) - no surprise there, but still .

# **🛴Road to a working prototype**

RIP old deadline of 28.02.23. New deadline 08.03.2022. Four main deliverables:

- ✅Improve answer quality - [see previous post](http://www.scortescu.com/posts/slackgpt_w3/#improved-answer-quality)
- ✅Build a homepage for the bot in Slack - [see previous post](http://www.scortescu.com/posts/slackgpt_w3/#build-a-homepage-for-the-bot-in-slack)
- ✅Build a landing page including an install button
- ✅Handle user management 🎉

## ✅Landing page

With installation flows and user management in place, the “Add to Slack” button now works!! Go SquidGPT 🦑!

I’ve decided to invest some more effort into the landing page beside the install button. My next step is to start talking to potential customers. And I’ve already received some feedback on the landing page. So I went ahead and implemented that. Here are the changes:

- Made the headlines more precise, and hopefully clearer
- Simplified the “How it works section”
- Added “business-y” examples for each of the frameworks, and removed the cost benefit framework as it’s very similar to the pro/con one
- Worked on the visual quality and consistency
- Lowered prices to 2$/user/month
- Added a section on data privacy and security

Here’s the new page in its full glory (or go to [this link](https://squidgpt.carrd.co/) for the real thing):

![landing_v2](/slackgpt_w5/landing_v2.png#center)

## ✅Handle user management

When I finished writing this last week, I was a bit pessimistic about managing to figure this one out. Fortunately, my first idea (*Switch to a different database provider (e.g. Supabase) - their PostgreSQL implementation seems much friendlier than AWS’*) helped a lot. 

In Supabase, I could see if my database was actually doing anything. With a working database, I found out that the example code provided by Slack had a bug (it didn’t properly build the require tables, if they didn’t exist). 

Fixing that bug led me to another one inside Slack’s Software Development Kit (SDK). Slack’s own code for handling queries to the database (adding new users, retrieving existing users) didn’t handle the response correctly. Bad Slack 😵‍💫

Everything works now. Hopefully, from here on it should be easier to keep adding features to the bot, and start the process for getting it on the actual [Slack marketplace](https://slack.com/apps)

# ⚠️OpenAI’s own Slack bot

[Slack and OpenAI are working together to bring ChatGPT to Slack](https://www.salesforce.com/news/stories/chatgpt-app-for-slack/) soon. It’s not unexpected. Microsoft has already integrated ChatGPT in Teams. Hell, everyone and their grandma is doing it. My initial hypothesis that people want to keep chatting where they were chatting and not have to go somewhere new isn’t the insight of the century. Just try to get someone to install a new messaging up for that one contact (you know who you are).

However, that shouldn’t change my plans for SquidGPT too much (tell me why it should, *seriously*). I still think (to be confirmed by customers) that getting insightful answers structured according to predefined frameworks is both: 1. useful for people that frequently write up their analyses, and 2. not trivial with ChatGPT’s current capabilities. 

There’s one thing that changes. Some people previously asked “Why don’t you also add regular ChatGPT, not just the framework stuff?”. I think that I won’t be prioritizing that for now. At least until OpenAI reveals more about their plans. 

## ****🗿Personal update: How’s it going, Stefan?****

🏃I’ve finished the half marathon successfully. It was much harder than I first thought - stupid hills. But I still made a good time: 2 hours 1 minute 20 seconds. That’s 5:45 min/km. With some more prep, I should be able to make the marathon in under 4 hours.

Had a friend visiting over the weekend. It was great to connect and we also went to the Musee d’Orsay - always impressed by Monet (naturally, as he’s an impressionist). 

# ➡️Next steps

March is the month of customer development. Here’s what I plan to do:

- Define the customer profile more precisely
- Write up a sequence of messages for reaching out and following up
- Find and write to >100 people
- Run interviews with everyone that responds
- Synthesize the feedback and review the strategy

