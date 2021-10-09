---
---


<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video below.</li>
    <li>You will not need to join the Ohyay workspace today.</li>
    <li>This assignment will be an <strong>individual</strong> submission</li>
    <li>You will submit your <strong>Python code</strong> to <strong>GradeScope</strong> for this assignment.</li>
  </ul>
</div>

# Watch

<iframe width="644" height="362" src="https://www.youtube.com/embed/6OmeUKM1cfM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Previously, you were able to successfully handle summating student grades, which is a 
critical function for AlgoTutorBot. Now, we need you to process more sophisticated
log data, for even more students. We know from preliminary analyses this will have
to be a very efficient program.

The log data collected by AlgoTutorBot includes student submission scores, pages opened
by students, and temperature data collected by ATB using a variety of unobtrusive sensors.
Your program will use this data to report:

  * Student's highest page opened
  * Student's most recently opened page
  * Students' average submission score

To achieve full credit for performance, you must use built-in data structures to achieve O(1) expected case performance
for each row of input (a student log). Your overall solution should run in at least expected case `O(s*log(s)+l)`, where
`s` is the number of students and `l` is the number of rows of input (i.e., the number of student logs).

# Formal Specification

**Problem:** Calculate, sort, and report maximum, most recent, and average of a sequence of logs.

**Input:** The filename of a local file containing a sequence of student logs, each on their own line. The first line
will be the number of logs to read, and is not included in the number of logs. You can assume that each line will
only contain one log. The logs will come in ordered by the time they were collected.

A student log consists of three numbers and a letter, separated by spaces (in the form "Number, Letter, Number, Number").
All numbers will be 32-bit integers (i.e., no more than `2^31`).

  * The first element is the _Student ID_ , a unique number representing that student inside the dataset.
  * The second element is the _Action Code_ , and will be either the letter "P", "S", or "T"
  * If the letter is "P", for "Page Open", then the third element will be the _Page ID_ (a number) of the page opened by the student.
  * If the letter is "S", for "Submission Scored", then the third element will be the score of the _Submission_ made by the student (a number).
  * If the letter is "T", for "Temperature Tracked", then the third element will be the current _Temperature_ of the student (a number in Fahrenheit).
  * The fourth element is the _Timestamp_ , a number representing when the record was made.

An example of several records are below:

```text
507 P 1000 1
1 S 6 2
1 P 1400 3
1 S 8 8
1 T 101 10
507 S 4 12
1 P 1700 15
1 S 7 16
507 S 8 20
```

**Output:** A series of sorted student status reports. Each line of output will contain four numbers:

  * The student's ID
  * The student's highest Page ID
  * The student's latest Page ID
  * The student's average submission score (the sum of all the scores divided by the number of scores).

If a student doesn't have at least one submission and at least one page, then you should exclude it from the output. The
students should be sorted in ascending order based the status results: first by their highest page ID, than their latest
page ID, and finally by their average score. Truncate any decimals to become integers.

An example of output is below:

```text
507 1000 1000 6
1 1400 1700 7
```

# Submission

You will be submitting this assignment through the course's autograder.
The same rules will apply for all coding assignments in this course, so you should read them all carefully: [Autograder Instructions](https://udel.instructure.com/courses/1496336/pages/autograder-instructions)

Critically, this is an individual assignment. Do not share code with any of your group mates!

For this project, you will need to create an `answer.py` that solves the problem above and create a `readme.md` that
explains your solution at a high level. Inside your `readme.md` file, make sure you clearly explain the **algorithmic
runtime** of your program in terms of Big O. For full credit, you must be able to justify your program's complexity as
expected case `O(s*log(s)+l)`.

All parts of your solution, including both the program and the `readme.md` file should be submitted on GradeScope: <https://www.gradescope.com/courses/230699/assignments/1058794/>

## Grading

You will be graded on the following components:

  * 70% for a program passing the autograder's unit tests
  * 30% for a clear explanation in your `readme.md` file of the algorithmic runtime of your program.

Note that unclear code and answers can cause a huge penalty to your grade. We are not being strict on coding
style, but we shouldn't have to run your code through a deobfuscator to figure out what it does.