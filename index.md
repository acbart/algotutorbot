---
---

# Introduction to Algorithms with AlgoTutorBot

In Spring 2021, I taught a really weird Algorithms course, with the help of a megalomaniac Intelligent Tutoring System. I was chased, punched, and duct taped to a chair. But I think my students learned a little bit about Big Oh notation, so it's kind of a mixed bag. Want to hear more? Keep reading, or meet me at [SIGCSE'22](https://sigcse2022.us2.pathable.com/meetings/virtual/wT27nvQLMxSNj6Jke)!

1. [About](#about)
2. [Particularly Interesting Items](#particularly-interesting-items)
3. [Documentary](#documentary)
4. [Lessons](#lessons)
5. [Full Video Playlist](#full-video-playlist)
6. [Contact Me](#contact-me)

<!-- ![Screenshot from Lesson 16, where AlgoTutorBot has tied up Dr. Bart and is lecturing about Graph Structures](resources/algotutorbot.png) -->

<iframe width="590" height="332" src="https://www.youtube.com/embed/sGudGnwU7yc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## About

During the Spring of the 2021 semester, stuck in quarantine due to the ongoing global
pandemic, I decided I needed to do something completely different with my undergraduate-level
Algorithms course. Tired of teaching via Zoom to little boxes, I decided to recreate the entire
course, inspired by my love of Escape Rooms and Alternate Reality Games. Connecting
together Canvas, Ohyay, and GradeScope with my own custom technology, I weaved an
asynchronous, video-based narrative whereby students would inevitably have to save me from
my own Frankenstein’s monster: an evil Intelligent Tutoring System named "AlgoTutorBot" who
threatens not only the course, but the entire world!

The final course incorporates a range of interesting assignments that are available to external
adopters. This includes not only programming problems and conventional algorithmic logic
problems, but also a novel web application for experimenting with runtime analysis, an
interactive point-and-click adventure for practicing graph algorithms, and a pedagogical
methodology for concretizing students' problem solving process into tangible artifacts. There are
also a number of smaller assignments that would be easily adopted into a regular Algorithms
course. All resources and a walkthrough video of the experience are available at
https://acbart.github.io/algotutorbot/

This website shows off the final version of the course, and also describes some of the lessons I
learned along the way. The curriculum was a tremendous amount of effort, and would not be
easily reproduced. However, the experience was very rewarding and earned me my highest
course evaluations ever - virtually perfect scores.

## Particularly Interesting Items

* [Runtime Case Builder](https://acbart.github.io/runtime-case-builder/?preload=RCB_find_with_break_dynamic.json): An interactive web application that let's students make graphs of algorithms' runtime. Students can control not only the algorithm, but also the cases and instances of input they use. Multiple cases of inputs can be visually compared against each other, e.g., to highlight different worst/best case behavior of algorithms. Check out this assignment for some [example questions](https://docs.google.com/document/d/1bxph3XW2O2fmrgDw7DmTnJzYo58CzZvorQG0eWJ8hks/edit?usp=sharing) you could use the Runtime Case Builder with. 

![Runtime Case Builder Screenshot](resources/runtime_case_builder.png)

* Algorithmic Problem Solving Flowchart: I hypothesize that Algorithms courses that give feedback only on students' answers, rather than their problem-solving process, are emphasizing the wrong thing and are likely to encourage cheating. I have been experimenting with a scaffolded series of assignments where students develop a "flowchart for solving problems". This is *not* about making flowcharts that show an algorithm that solves a problem - this is about helping students to formalize their problem-solving strategies. The idea is first introduced in [Lesson 08](lessons/Lesson 08- Algorithm Flowchart), built further in Lessons [12](lessons/Lesson 12- Algorithmic Strategies), [17](lessons/Lesson 17- Flowchart Updates), and [22](lessons/Lesson 22- Pit Digging), and finally somewhat summatively assessed in [26](lessons/Lesson 26- Final Algorithmic Puzzles). An example of what a "flowchart" might end up looking like is available [here as an image](resources/Algorithmic Flowchart Example-v2.pdf) (to prevent trivial copy/pasting). Note that the end result may not actually be a flowchart, but instead something more like a textual algorithm; the important part is that they concretize their thoughts, not that they produce a certain style of diagram!

![Point-and-click Graph Algorithm Adventure Screenshot](resources/point_and_click_adventure.png)


* Point-and-click Graph Algorithm Adventure: In Lesson 16, students were directed to a special section of the Ohyay space that was modeled after my house. With spooky music playing and little context, they had to join together and explore the house to find me. Along the way, they find a video where I reveal that I have hidden some notes around the house that explain how they can determine the password to unlock the door to the basement. Basically, they have to execute a number of graph algorithms (e.g., Prim's, Djikstra's) using the house's rooms as a graph of vertices and edges. A walkthrough of the adventure can be found [here](lessons/Lesson 16- Graph Concepts).

## Documentary

The following video is a sort-of "Documentary" about what I did in the course, and shows some highlights from the semester.

<iframe width="640" height="360" src="https://www.youtube.com/embed/RPXTiiGKdCo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Lessons

* [Lesson 00- Introduction](lessons/Lesson 00- Introduction)
* [Lesson 01- Algorithm Basics](lessons/Lesson 01- Algorithm Basics)           
* [Lesson 02- Practicing Problems](lessons/Lesson 02- Practicing Problems)        
* [Lesson 03- Using GradeScope](lessons/Lesson 03- Using GradeScope)           
* [Lesson 04- Runtime Analysis](lessons/Lesson 04- Runtime Analysis)           
* [Lesson 05- Bounds and Big Oh](lessons/Lesson 05- Bounds and Big Oh)          
* [Lesson 06- ADTs and Data Structures](lessons/Lesson 06- ADTs and Data Structures)   
* [Lesson 07- Algorithm Misconceptions](lessons/Lesson 07- Algorithm Misconceptions)   
* [Lesson 08- Algorithm Flowchart](lessons/Lesson 08- Algorithm Flowchart)        
* [Lesson 09- Implement an Algorithm](lessons/Lesson 09- Implement an Algorithm)     
* [Lesson 10- Trees](lessons/Lesson 10- Trees)                      
* [Lesson 11- Sorting](lessons/Lesson 11- Sorting)                    
* [Lesson 12- Algorithmic Strategies](lessons/Lesson 12- Algorithmic Strategies)     
* [Lesson 13- Big Oh in the Wild](lessons/Lesson 13- Big Oh in the Wild)
* [Intermezzo](lessons/Intermezzo)       
* [Lesson 14- Graph Structure](lessons/Lesson 14- Graph Structure)           
* [Lesson 15- Graph Traversal](lessons/Lesson 15- Graph Traversal)
* [Lesson 16- Graph Concepts](lessons/Lesson 16- Graph Concepts)            
* [Lesson 17- Flowchart Updates](lessons/Lesson 17- Flowchart Updates)          
* [Lesson 18- Recursion](lessons/Lesson 18- Recursion)                  
* [Lesson 19- Backtracking](lessons/Lesson 19- Backtracking)               
* [Lesson 20- Dynamic Programming](lessons/Lesson 20- Dynamic Programming)        
* [Lesson 21- Bookbag Filling](lessons/Lesson 21- Bookbag Filling)            
* [Lesson 22- Pit Digging](lessons/Lesson 22- Pit Digging)
* [Lesson 23- Nondeterministic Polynomial Time.pdf](quizzes/Quiz_ Lesson 23- Nondeterministic Polynomial Time.pdf)
* [Lesson 24- Reductions.pdf](quizzes/Quiz_ Lesson 24- Reductions.pdf)
* [Lesson 25- Approximation](lessons/Lesson 25- Approximation)              
    * When Lesson 25 is completed, [this page](https://acbart.github.io/endless-algo-runner/) becomes available.
* [Lesson 26- Final Algorithmic Puzzles](lessons/Lesson 26- Final Algorithmic Puzzles)  
* [Lesson 27- The End](lessons/Lesson 27- The End)                    

## Full Video Playlist

The following contains *all* the videos used in the course, including several that are meant to be secret. If you don't want spoilers, then you shouldn't watch. But if you want to see how it all turns out, watch below! It's 3 hours, 25 minutes total.

<iframe width="590" height="332" src="https://www.youtube.com/embed/jFDxhB0gtZQ?list=PL4lj9_lkgXTMlEKffSifwms8iYJKjTITH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Contact Me

Thanks for checking out all my materials! I have chosen not to upload some of them, to prevent them from being abused by students searching for answers. This mostly includes instructor unit tests and grading scripts, answer keys, and reference answers. If you are an instructor interested in these materials, please feel free to fill out this google form: [https://forms.gle/dU6U17Uy4QZ3KR577](https://forms.gle/dU6U17Uy4QZ3KR577)

If you would like to contact Dr. Bart directly, you can email him at <a href="mailto:acbart+atb@udel.edu">acbart+atb@udel.edu</a>
