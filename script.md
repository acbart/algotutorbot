## Act 1- Introduction

In the Spring 2021, it was a year into the global COVID19 pandemic, and the university of Delaware where I teach, was online.
I had been tasked with teaching CISC320 Introduction to Algorithms, an upper-division course for sophomore and junior CS majors.

I'd taught the class a few times before, and I wasn't really sure how I could meaningfully translate it to work online.
The class tends to be very lecture heavy, and the projects can easily end up decontextualized.
To be honest, I was dreading the thought of spending an entire semester talking to little black boxes on Zoom, with students who were sure to be bored after just the first week of talking about Big Oh notation and limit analysis.

That previous Fall 2020, when I was first teaching an entire semester online, my most effective assignment was an educational escape room I put together for Halloween, with pre-recorded videos that told a little narrative where I was stuck in my patio. Not only were my students more engaged than they'd ever been before, but even just making that assignment was a lot more fun for me.

I wanted to capture that kind of energy again, even though I knew it might be a lot of effort. Working furiously over my winter break, I threw together an outline for the semester that I thought would be fun and exciting for students, with the plan to fill in blanks as I went.
I had no idea that this would lead to the busiest, most complex, but also most rewarding course I've ever taught.

> Lesson 00- Introduction, first two minutes

The story I put together was that I had created an Intelligent Tutoring System named AlgoTutorBot. I introduce him in the very first lecture as an integral member of the course staff. During the first month of lectures, AlgoTutorBot establishes a faintly antagonistic relationship with me. For example, in Lesson 2 he makes fun of my face. But I was trying even harder to make the students dislike him, for instance, by having him repeatedly suggest we have exams despite my objections. My goal was to set him up as the eventual villain of the story, although we also had to cover a fair amount of learning material at the same time.

The course progresses normally for the first month. I cover the basic definition of problems and algorithms, explain the ideas of Big Oh and runtime analysis, review basic data structures, and talk about ideas like Proofs and Counter Examples. Twice a week, students began lecture by watching a relatively short prerecorded video lesson, usually only 10-20 minutes long. Then, they complete an assignment based on what we covered in the video.
There's a number of interesting little assignments here that might be of interest to adopters. 

The best is probably Lesson 4, which covers Runtime Analysis through a web-based tool I created named Runtime Case Builder. Students can take a piece of editable Python code, create a bunch of possible inputs, and plot the number of steps that the algorithm takes. This whole tool is actually pretty sophisticated, and is free and open source.

* Lesson 5 is traditional math problems involving Big Oh, not much novelty there.
* Lesson 3 and 9 and coding problems autograded with GradeScope, which might be useful for adopters.
* Lesson 6 has students fill out a table describing different Abstract Data Types and Data Structures, it went okay.
* Lesson 7 was pretty fun, students have to write counter-arguments to a bunch of common misconceptions related to Algorithms and Data Structures.
* Lesson 10 has them debugging an implementation of an AVL tree, that went pretty smoothly.
* Lesson 11 has them create a video explaining one of various sorting exotic sorting algorithms, which also went fairly well.

Lesson 8 introduces a major recurring assignment that I haven't ever used before, which was for students to make a flowchart that documents their problem-solving strategies. This was a mixed success - some students did a great job with this, and by the end of the course had beautiful explanations of how they solved algorithmic problems. But some students never really figured out what I wanted, and couldn't do more than replicate my examples. 

Lesson 12 builds on Lesson 8 to have them solve an algorithmic problem, but using a fairly regimented approach based on their flowchart. Critically, I require them to make an attempt without google first on their own for 30 minutes, before taking a long multi-hour break. Then they can make another attempt with external resources, including the course staff - I expect them to reach an answer at that point, since they can ultimately ask one of us for help. Afterwards, they need to write a reflection documenting their approach and describing revisions they might make to their Algorithmic Flowchart. They repeat this process a few more times over the course of the semester. The flowchart aspect worked okay, but I heartily recommend the general strategy of having students make two attempts, because I think it generates a lot more buy-in from them. They see the value in attempting it on their own, but can be confident that they'll eventually get the answer and the points.

The final assignment in this phase of the course centers on an article about Accidentally Quadratic algorithms in the wild. They have to read about real-world cases where moderate sized inputs caused huge issues because algorithms were poorly tuned. I think this one is interesting, because it helps contextualize the course content a little more.

At this point, we're about 6 weeks into the course, and I had a lot of videos with AlgoTutorBot where he acts increasingly erratic. He starts getting very belligerent, he crashes during the lecture, and at one point he suggests that "1+2 is the sum of Apple." And at the end of Lesson 13, he gets a little suspicious.

> Lesson 13: 4:32->end

This all comes to a head after Lesson 13, when I am supposed to release midterm grades.

> Act 2 Conclusion video, 1:30min

This lesson ends right before an extra long weekend, so the cliffhanger is not resolved for a little while. When students return to the online course site, they find that a lot of the text has been changed to suggest that AlgoTutorBot is now in charge. The next video is even more dramatic.

> Lesson 14 video, start -> 30 seconds...
> Lesson 14 video, last 30 seconds or so

So yeah, things get a little wild from here. The rest of that lecture is a little dry, but the worksheet they complete accompanying it has a lot great little comments from AlgoTutorBot embedded.  The next lecture gets much crazier, though, once I escape.

> Screenshot of Lesson 15.

Confronting AlgoTutorBot from my phone, I explain how I was able to chew through the tape and escape. He counters by siccing his "AlgoDeathBots" on me, enlisting the students to write graph search programs that will help chase me down. Once students pass a sufficient number of test cases, they are rewarded with a video of the Death Bots being deployed...

> Lesson 15 part 2.

I declare war on ATB and go into hiding, leading to my absolute favorite assignment of the course. Lesson 16, graph algorithms.

At this point, I need to explain a bit more about the format of the course. Students began each class by finding a daily Lesson on Canvas and watching its associated video. Then, they join a website named Ohyay which has a dedicated space for the class. Ohyay is a little bit like PowerPoint crossed with Zoom, with the space broken up into separate Rooms that can be navigated between. This gives you a huge amount of flexibility as an instructor to create interactive experiences while still letting students see and interact with each other. Throughout the course so far, students have been working in groups and navigating between rooms, so they are comfortable with the space and have expectations for it.

On Lesson 16, about midway through the semester, they find that the day's lesson has them navigate to a new Room in Ohyay: My House.

> Record some footage of going through.

The adventure begins with AlgoTutorBot explaining that I have retreated further into the house and is eluding his grasp. 
From there, they can enter my house and move between rooms.
It's essentially a point and click adventure game embedded in Ohyay. These are actually photographs of my house, 

At some point, the students made their way to the living room and found a TV. This video includes a recording of me explaining that I have hidden some clues throughout the house that, together, will help them access the lower levels of the building that have been mysteriously added by AlgoTutorBot.

Strategically throughout the house, there are notes that they can hover over to get clues. Putting all the clues together, they find out they have to perform a few different graph algorithms, including Prim's and Djikstra's, in order to get the answers to a quiz back on Canvas. When they complete that quiz, they are taken to a new room in the house with a victory screen.

Lesson 16 was the high point of the course for me, and I think students enjoyed it. Certainly, I really threw them for a loop when they realized the scale of what I was having them do. I was able to lurk behind the scenes and watch their growing confusion and amusement as they worked together to explore the house. 10/10 I recommend spooking your students every semester.

In the second half of the course, students switch from helping AlgoTutorBot to helping me, as we try to turn the tides on our new robotic overlord. There's several more coding assignments that have them using recursion, dynamic programming, and brute force backtracking algorithms.

Lesson 18 has students use recursion to crack open a zip file that has a recursive structure of files, one of which contains a recursive JSON file, which in turn has a recursive data value: a 1-dimensional string maze. I'm actually a little proud of this idea. Basically, it's a string of emojis, some of which are arrows indicating the next index they should jump to. In some cases, the arrows fork, so the easiest solution is to write a little recursive algorithm.

Lesson 19 builds on that lesson, by having them extract a file from the Zip, but the file is password protected. They have to write a bruteforce password checker that abuses the weak hash function and known password requirements, in order to figure out the password for the file. This unveils the next video, which advances the plot to help me rescue my dogs, who had been kidnapped by AlgoTutorBot.

Lesson 21 has Ada and Babbage, my two dogs, traversing the facility looking for clues to AlgoTutorBot's nefarious master plan. The students are tasked with writing a Dynamic Programming algorithm to solve the Knapsack problem. As students complete more test cases, they unlock amusing videos where Babbage progressively fills his knapsack with better and better items - although he also brings me pudding and booze, rather than clues. Eventually, however, he brings me an "evil glowing power core", revealed to be pivotal to the structural integrity of the base.

The next few Lessons are essentially a boring quiz about Non-deterministic Polynomial Time algorithms and Reduction. I was running out of time and energy at this point, so to be honest I don't think they ended up very interesting. There are some amusing videos of AlgoTutorBot at that point, though, who is suffering from an increasing breakdown as he tries to get the students to complete quizzes and fails to catch me. 

All of this brings us to Lesson 25, which is the last really exciting assignment. I start the video from a ventilation shaft, explaining that students need to write an algorithm to direct my dog Ada to destroy all of the cores as quickly as possible. In other words, they have to implement a solution to the Travelling Salesman Problem. Their solution doesn't have to be optimal, but it does need to outperform my baseline. If they do, they are actually rewarded with not just a video of the last core being destroyed by Ada, but also a little web-game where they control an avatar of me escaping the facility. I spent way too long working on the game for that, considering it had no real pedagogical value.

Escaping the facility, it seems like all has gone well, and that the adventure is over. I have my dogs, the facility is destroyed, and I am safe.

> Lesson 26 Intro: first 90 seconds? Full video if we can.

So yeah, things get pretty silly from here. After this last assignment, I released the final video. The whole thing was 12 minutes long, featuring three possible endings. Once again, I spent way too long on that part, considering it had no pedagogical value. But I had such a fun time making it, I can't say it wasn't worth it. I won't spoil the endings, in case you want to go watch them and see how the story plays out.

So how did this go in the end? Well, I didn't conduct this as a research experiment. I don't have data about their performance on any kind of assessments, and even if I did it wouldn't be meaningful given the surrounding context. We had a global pandemic going on, and some of my students had some real traumatic experiences outside of my class. Things have not been normal for any of us.

I do have my course evaluations. Although we know as a community that course evaluations are a very limited instrument, I think it's telling that I scored the highest evaluations I have ever earned. On a 5-point scale for the "Overall Course Rating", I got a 4.8, with every student giving me a perfect score, except for two students who gave me 4/5s. The comments talked a lot about the narrative and the assignments, which they all seemed to appreciate.

One of the best pieces of evidence that this was popular, however, was that some students started making fan art and fan music of AlgoTutorBot. I wasn't privvy to the conversations, but apparently quite a few students even outside the course started following the narrative and discussing it. Again, I have no quantitative data, so take this all with a grain of salt. But it was pretty gratifying when alumni started sharing artwork and music about my course.

In general, I think that I learned a few lessons from this whole experience.

First, modern course design tools make it realistic for even an amateur without a budget to put together a fun course narrative like this. It was a lot of work, but I think I provided a fun story and engaging activities. I didn't have to break the bank or kill myself worrying about production values - it was okay when it was rough around the edges.
Second, try to prepare as much as possible up front. Trying to develop stuff during the semester is always brutal. I had to make a lot of decisions on the fly, but having the rough outline helped a lot. I think it's better to make a less flexible story if that means you have more to use.
Third, don't be afraid to think outside of the box and change your expectations. I threw out my exams, my dry lectures, anything that I didn't think would work in the remote experience. If I'd taught a normal course that spring during the global pandemic, the students and I would have all gone nuts. Another semester of business as usual was just too much to consider. Sometimes you have to try stuff, if only for your own sanity. If students saw less material, that's okay, because I think they managed to learn what they did see a little more deeply.

Looking back, this course was a huge amount of work. I was completely and utterly burned out at the end of this semester. Teaching the course remotely, even with this approach, was dehumanizing and stressful. I had students who just couldn't get motivated or keep up with the workload, even though it was the easiest version of the course I've ever taught. I hated teaching online, and I can't imagine doing it again. I love some of the assignments that I created, and making the videos was a lot of fun. I'm hoping to use a lot of the resources I created again some day, but I don't think I could recreate the exact experience again. But some students genuinely enjoyed the experience, and a lot of it was just a lot of fun. Either way, good or bad, I'm going to remember this semester for the rest of my life.

Well, thank you so much for watching through this video and hearing about the strangest class I've ever taught. I hope you might be inspired to try making your own course with an embedded narrative. If you do, please let me know how it goes. I think that there's a lot of potential for educational games and interactive experiences that keep the line between fun and programming plenty blurred. But for now, let's keep learning about how to teach students algorithms.