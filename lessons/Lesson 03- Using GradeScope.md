---
---



# Watch

<iframe width="644" height="362" src="https://www.youtube.com/embed/cNi4DUsBgiA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

We have a series of data files, each one representing a student's grades on various assignments in a course.
We need you to write a program that consumes the filename (from STDIN) and spits out
the sum of all the integer values in the associated local file. However, there are two catches. First, they want you to
ignore any negative numbers (indicating data errors). Second, if you encounter the number `-127`, you should stop
processing any further numbers (indicating an end of record).

## Formal Specification

**Problem:** Summate a sequence of numbers while skipping certain ones.

**Input:** The filename of a local file containing a sequence of integers, each on their own line. The first line will
be the number of integers to read, and is not included in the number of values. You can assume that each line will only
contain one integer For example:

```python

6  
5
10  
-3
15  
-127  
13
```

**Output:** An integer representing the sum, or the text `EMPTY` if no suitable values were given. In the example above,
the output would be `30`. Remember:

  * The first number is the quantity of values
  * Negative numbers are ignored.
  * You stop when you encounter `-127`

## Submission

You will be submitting this assignment through the course's autograder. The primary goal of this assignment is to get 
you used to using the autograder, since many subsequent assignments will also use this tool. To get started with
GradeScope, refer to [GradeScope Instructions](https://udel.instructure.com/courses/1563197/pages/gradescope-instructions "GradeScope Instructions")

For this project, you will need to:

* Write an `answer.py` that solves the problem above, and
* Create a `readme.md` that **explains** your solution at a high level and with its  **algorithmic runtime**.

All parts of your solution, including both the `answer.py` and the `readme.md` file should be submitted through the
autograder. You can access the autograder through the following link: <https://www.gradescope.com/courses/230699/assignments/976580/>

## Grading

You will be graded on the following components:

  * 50% for a program passing the autograder's unit tests
  * 30% for a clear explanation in your `readme.txt` file of how your program works.
  * 20% for a clear explanation in your `readme.txt` file of the algorithmic runtime of your program.

Remember, bypassing the autograder to avoid writing an appropriate algorithm (e.g., by explicilty handling each 
instructor unit test instead of solving the general problem) can lead to your submission being rejected or penalized.
Your goal is to demonstrate an understanding of how to solve algorithmic problems, not to pass unit tests.
