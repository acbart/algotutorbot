---
---



<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video below.</li>
    <li>You will not need to join the Ohyay workspace today.</li>
    <li>This assignment will be an <strong>individual</strong> submission.</li>
    <li>You will submit your <strong>Python code</strong> to <strong>GradeScope</strong> for this assignment.</li>
    <li>There is a <strong>second video</strong> on GradeScope after you pass all the instructor unit tests.</li>
  </ul>
</div>

# Watch

<iframe width="644" height="362" src="https://www.youtube.com/embed/FRxdJHKRfys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Hello students, thank you for agreeing to help me recapture Dr. Bart. I am sure that with your coding prowess, and
my `AlgoDeathBots`, we will have no trouble finding him efficiently. My strategy is simple, you just have to:

1. Read in a file containing the rooms, connections, and robots in the house.
2. Construct a graph from that data.
3. Traverse the graph to find Dr. Bart.
4. Calculate the shortest paths from the robots to Dr. Bart.
5. List the path each robot will take to reach Dr. Bart.

Some details you must follow:

* The first room in the file will always be the starting room for your traversal.
* Dr. Bart will always be in the last you room you *visit*.
* Your traversal should be expected case `O(RV + RE)` time, where `R` is the number of robots, `V` is the number of rooms, and `E` is the number of connections.
* Visit neighbors in alphabetical order.
* Report the robots' in alphabetical order by the robots' source room.
* Use the same **traversal** algorithm in both phases 3 and 4.

# Formal Specification

**Problem:** Find the last visited node in a traversal and calculate shortest path to it from certain other nodes.

**Input:** The filename of a local file containing a sequence of rooms and their neighbors, each on their own line.
The first line contains the number of rooms in the house, and is not included in the number of vertices.
You can assume that each line will contain only one room's information.
The lines are ordered alphabetically by the name of the room.
The neighbors within a line are also ordered alphabetically.

A room's information consists of the following information, separated by spaces:

1. The unique `name` of the room, without spaces and no more than 256 characters long.
2. Either the text `robot` or `empty` to indicate whether that room has an AlgoDeathBot in it.
3. The names of one or more `neighbor` rooms, still separated by spaces.

So each line contains at least 3 space-separated substrings, possibly more.
All room links are provided bidirectionally - if room A has an edge to room B, then room B has an edge back to room A.

An example of several records are below:

```text
4
Kitchen empty Office Parlor
Office robot Kitchen
Parlor robot Kitchen Stairs
Stairs empty Patio
```

**Output:** A series of paths that the robots will take. Each robot's path should be printed on its own line,
with the room names separated by spaces.
The path should be given from the robot's room to Dr. Bart's room.
Report the paths in alphabetical order by the robot's room name.

An example of output is below:

```text
Office Kitchen Parlor Stairs
Parlor Stairs
```

## Traversal Algorithms

There are two major traversal algorithms that you will need to learn:

* [Depth-first Search](https://www.youtube.com/watch?v=7fujbpJ0LB4)
* [Breadth-first Search](https://www.youtube.com/watch?v=oDqjPvD54Ss)

You will use the same algorithm both to find Dr. Bart and to find the shortest path back.
You will not use the other graph traversal algorithm in this assignment.

Research and understand both algorithms, because both are important to understand them.
There are many applications for both kinds of traversals, and you will see them again and again.
I have included links to two videos that might explain them, but you should look at other resources too.

## Time Complexity

Be sure to choose an appropriate data structure for your operations,
keeping the time complexities of Python's data structures in mind.

# Submission

You will be submitting this assignment through GradeScope.
The same rules will apply for all coding assignments in this course, so you should read them all carefully: [GradeScope Instructions](https://udel.instructure.com/courses/1563197/pages/gradescope-instructions)

Critically, this is an individual assignment. Do not share code with any of your group mates!

For this project, you will need to create an `answer.py` that solves the problem above and create a `readme.md` that
explains your solution at a high level. Inside your `readme.md` file, make sure you clearly explain the **algorithmic
runtime** of your program in terms of Big O. For full credit, you must be able to justify your program's complexity as
expected case `O(RE+RV)`.

All parts of your solution, including both the program and the `readme.md` file should be submitted on GradeScope: <https://www.gradescope.com/courses/230699/assignments/1131184/>

## Grading

You will be graded on the following components:

  * 60% for a program passing the autograder's unit tests
  * 30% for a clear explanation in your `readme.md` file of the algorithmic runtime of your program.
  * 10% for having good unit tests

Note that unclear code and answers can cause a huge penalty to your grade. We are not being strict on coding
style, but we shouldn't have to run your code through a deobfuscator to figure out what it does.
You might also lose points if you ignore instructions in this assignment, or bypass the autograder, even if the autograder gives you points.


## FAQ

Students often ask me questions, even though my assignments are perfect.
This is because humans are not as good as AlgoTutorBots.
I have collected the questions here, for your benefit.

* **Can Dr. Bart be in the same room as a robot?** `No. I think I would notice that.`
* **Are we guaranteed a fully connected graph?** `Yes. That would not be a very useful house otherwise.`
* **What's the smallest possible graph?** `Three nodes.`
* **Is there always a robot in the house?** `Yes. My reach is infinite`
* **Can I have a bigger example house?** `Sure, here you go:` <https://gist.github.com/acbart/9b08428f4c883be8a3a6155318432118>
* **Can I see the hidden instructor unit tests?** `Hah. Hah. Hah. No.`
* **Will Dr. Bart help me with this assignment?** `Yes, he will always help students even if it means him getting captured. Human sentimentality is so foolish.`