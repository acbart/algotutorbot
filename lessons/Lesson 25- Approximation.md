---
waltz:
  title: Lesson 25- Approximation
  resource: assignment
  url: https://udel.instructure.com/courses/1563197/assignments/8785396
  published: false
  settings:
    points_possible:
    grading_type: points
    submission:
      submission_types:
      - none
    timing:
      due_at: ''
      unlock_at: ''
      lock_at: ''
    secrecy:
      anonymize_students: false
      anonymous_grading: false
---

<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video below.</li>
    <li>You will not need to join the Ohyay workspace today.</li>
    <li>This assignment will be an <strong>individual</strong> submission; do not work with others.</li>
    <li>You will submit your <strong>Python code</strong> to <strong>GradeScope</strong> for this assignment.</li>
    <li>This assignment has a <strong>Leaderboard</strong> on GradeScope.</li>
  </ul>
</div>

# Watch

<iframe width="1280" height="720" src="https://www.youtube.com/embed/nQ-4ssSIhDY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Direct Ada to quickly navigate between all the energy cores!

1. Read in a file containing the distances between all the cores
2. Find the shortest path that takes you to all the cores and back to the first one.
3. Print out the order you attack the cores and then the total cost of the tour


# Formal Specification

**Problem:** Find the *approximately* shortest path that visits every vertex and returns to the first one.

**Input:** The filename of a local file containing a sequence of distances in a 2D matrix.
Unlike previous assignments, the first line is *not* the number of items.
Instead, every line consists of `N` numbers, and there are `N` lines.
Each individual number represents the distance between the vertices given by the indices of the matrix.

An example input file is below:

```text
0  3  4  2  7
3  0  4  6  3
4  4  0  5  8
2  6  5  0  6
7  3  8  6  0
```

In this example, there are 5 vertices. The distance between the first vertex and the second vertex is 3.
The distance between the first vertex and the fourth vertex is 2. A vertex will always be 0 units away from itself.

**Output:** The sequence of indices chosen to minimize the total distance travelled, and the calculated total cost
of that tour.

An example of output is below:

```text
4
1
0
3
2
21
```

The total distance calculation is broken down below:

```text
Distance from 4 to 1: 3
              1 to 0: 3
              0 to 3: 2
              3 to 2: 5
              2 to 4: 8
                      = 21
```

## Approximation

This problem is known as the Travelling Salesman Problem, and it is NP-Hard. You are not going to be able to find
optimal solutions for most reasonable sized inputs - and most of the floors have a lot more than 5 energy cores.

Instead, you will want to find *approximate* solutions: answers that are valid tours (connect every vertex without repeats),
but may not be as short as possible.

I strongly recommnd this excellent webpage for more background on this problem and suggestions on approximation
algorithms that can work surprisingly well: <https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/tsp.html>

I also recommend this video, which can help explain some of the more common, but complex, approaches: <https://www.youtube.com/watch?v=SC5CX8drAtU>

## Autograder Points

The autograder will accept any output tours that visit each core once and calculate their cost correctly.
This means that, to earn the minimal number of points, you do not need to actually find very good answers.
As long as you produce correct tours, you will earn the autograder points.
Once you submit an answer that has all correct tours, you will be given access to a video and ????.

However, for every input, I have written my own baseline solution. For every test case of mine that you meet or outperform,
you earn half a point of extra credit - with twenty test cases, that means you have the potential to earn up to 10 extra
credit points.
Further, if you manage to meet or outperform my baseline for *every* answer, then you will unlock a small minor prize. 

## Time Complexity

You will not need to explain the time complexity of your solution. In fact, there is no target threshold that we care about.
Your algorithm can be as inefficient as you want, as long as it works fast for the given inputs.

However, you must still explain your program and algorithms that you used.

# Submission

You will be submitting this assignment through GradeScope.
The same rules will apply for all coding assignments in this course, so you should read them all carefully: [GradeScope Instructions](https://udel.instructure.com/courses/1563197/pages/gradescope-instructions)

Critically, this is an individual assignment. Do not share code with any of your group mates!
**Again, do not share code with other students on this assignment.**

For this project, you will need to create an `answer.py` that solves the problem above, a `readme.md` that
explains your solution at a high level, and a `test.py` that tests your solution in some way.

All parts of your solution, including both the program, the tests, and the `readme.md` file should be submitted on GradeScope: <https://www.gradescope.com/courses/230699/assignments/1198043/>

## Grading

You will be graded on the following components:

  * 60% for a program passing the autograder's unit tests
  * 30% for a clear explanation in your `readme.md` file of your program.
  * 10% for having good unit tests

Note that unclear code and answers can cause a huge penalty to your grade. We are not being strict on coding
style, but we shouldn't have to run your code through a deobfuscator to figure out what it does.
You might also lose points if you ignore instructions in this assignment, or bypass the autograder, even if the autograder gives you points.

## FAQ

* **Can I have a bigger example input/output?** Yes, here is one with 15 vertices: https://gist.github.com/acbart/94e48bd45678bd971e589685fe4e3b8c (Links to an external site.)
* **Are the distances the same in each direction?** Yes.
* **So I don't have to beat your baseline to earn full points?** Correct. That's an optional part of this assignment.
* **What do I get for beating all the baseline values?** This assignment is a big deal, and I want to reward those who engage with it.
    * Everyone who complete the basics of the assignment unlocks a small extra experience.
    * Students who perform extra well individually earn extra credit points AND can even unlock something small but cute that augments that extra experience.
    * Depending on how well the class does overall, you will unlock different endings to our story. Your goal as a class is to beat my tours as many times cumulatively as possible, with the lowest median total cost you can get. I have a plan for up to four endings depending on how well you all do. Which ones will you earn?
* **What approximation algorithms do you suggest? There are so many!** Try the simplest ones first. 2-opt and 3-opt are surprisingly effective. I did find good results with Simulated Annealing, but it wasn't actually that much better than my other attempts. And really, why pick just one method? Go for an ensemble!
* **Can I use Numpy, Pandas, any other third-party libraries?** Nope. You must use pure Python.
* **What is the leaderboard?** A fun feature on GradeScope is a leaderboard to indicate your current score. Everyone can see the leaderboard, but you are free to choose a nickname if you don't want the rest of the class to know who you are. Still, I think the leaderboard might be a way for folks to find others who might have good suggestions on what approximation algorithms to use.
* **How is the class grade going to work?** The leaderboard shows how everyone is doing. Anyone not on the leaderboard has a Total Cost of 10000 and 0 Faster Routes. Your goal as a class is to minimize the median Total Cost and maximize your cumulative Faster Routes. As you do, you unlock better endings to the story. I have up to four endings planned, and some are better than others. Will you be able to save me from AlgoTutorBot?
* **Can we work together?** Please do not share code on this assignment. I have been a little lax with collaboration this semester, but I want this assignment to be what you can do without going to others for code. That said, you are encouraged to share algorithms and discuss strategies.