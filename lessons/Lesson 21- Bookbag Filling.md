---
---


<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video below.</li>
    <li>You will not need to join the Ohyay workspace today.</li>
    <li>This assignment will be an <strong>individual</strong> submission.</li>
    <li>You will submit your <strong>Python code</strong> to <strong>GradeScope</strong> for this assignment.</li>
    <li>There are <strong>five videos</strong> on GradeScope that unlock as you pass the instructor unit tests.</li>
  </ul>
</div>

# Watch

<iframe width="1280" height="720" src="https://www.youtube.com/embed/n22f-jsX23o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Babbage needs your help filling up his bookbag with valuable items!

1. Read in a file containing a maximum capacity and items' names, weights, and value
2. Find the subset of items that maximize the value while keeping the minimum equal to or below the threshold capacity
3. Print out the list of items and their total value


# Formal Specification

**Problem:** Identify the subset of items that will maximize their value while keeping their total weight equal to or below a threshold.

**Input:** The filename of a local file containing a sequence of items, each on their own line.
The first line contains the number of total items in the facility.
The second line specifies the maximum `capacity` of the bookbag.
All subsequent lines describe the sequence of items and contain three elements.

An item's information consists of the following information, separated by spaces:

1. The unique `name` of the item, without spaces and no more than 256 characters long.
2. An integer specifying the `weight` of the item
3. An integer specifying the `value` of the item

An example input file is below:

```text
5
15
Blueprints 4 50
HardDrive 10 2
DogFood 10 5
MysteriousCrystal 20 60
SuperComputer 100 100
```

**Output:** The name of each chosen item on its own line, with the last line having the total value of the items.

An example of output is below:

```text
Blueprints
DogFood
55
```

## Capacity

A critical aspect of this Problem is to understand that Babbage can only carry a certain amount of total weight.
We call this total weight the `capacity` of the bookbag. In the example above, the `capacity` is 15. This means
that we can take:

* `Blueprints`, which weigh 4
* `DogFood`, which weigh 10

The total weight of these objects is 14, and their total value is 55. Notice that we take the `DogFood` instead
of the `HardDrive`, because Babbage believes the `DogFood` is worth more (I mean, he is a dog).
The other two options cannot be considered because their weight is more than the capacity of the bag.

However, if the `capacity` was instead 20, then the output would be:

```text
MysteriousCrystal
60
```

The increased capacity means Babbage can now carry the `MysteriousCrystal`, which has a value of 60 and a weight of 20.
This is more than the combined value of the `BluePrints` and `DogFood`, so he leaves them behind.

## Time Complexity

Your solution must work in time complexity `O(nW)` where `n` is the number of items and `W` is the numerical size of the capacity.
Notice this `W` term - we are asking for [*pseudo-polynomial time* algorithm](https://en.wikipedia.org/wiki/Pseudo-polynomial_time).

# Submission

You will be submitting this assignment through GradeScope.
The same rules will apply for all coding assignments in this course, so you should read them all carefully: [GradeScope Instructions](https://udel.instructure.com/courses/1563197/pages/gradescope-instructions)

Critically, this is an individual assignment. Do not share code with any of your group mates!

For this project, you will need to create an `answer.py` that solves the problem above, a `readme.md` that
explains your solution at a high level, and a `test.py` that tests your solution in some way.
Inside your `readme.md` file, make sure you clearly explain the **algorithmic runtime** of your program in terms of Big O.
For full credit, you must be able to justify your program's complexity as worst case `O(nW)`.

All parts of your solution, including both the program and the `readme.md` file should be submitted on GradeScope: <https://www.gradescope.com/courses/230699/assignments/1189387/>

## Grading

You will be graded on the following components:

  * 60% for a program passing the autograder's unit tests
  * 30% for a clear explanation in your `readme.md` file of the algorithmic runtime of your program.
  * 10% for having good unit tests

Note that unclear code and answers can cause a huge penalty to your grade. We are not being strict on coding
style, but we shouldn't have to run your code through a deobfuscator to figure out what it does.
You might also lose points if you ignore instructions in this assignment, or bypass the autograder, even if the autograder gives you points.
