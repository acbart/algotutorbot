---
waltz:
  title: Lesson 10- Trees
  resource: assignment
  url: https://udel.instructure.com/courses/1563197/assignments/8785356
  published: false
  settings:
    points_possible: 10
    grading_type: points
    submission:
      submission_types:
      - none
    timing:
      due_at: March 16 2021, 1100 PM
      unlock_at: March 15 2021, 0700 PM
      lock_at: ''
    secrecy:
      anonymize_students: false
      anonymous_grading: false
---

<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video below.</li>
    <li>Join your Ohyay group room by <strong>9:25am</strong>.</li>
    <li>This assignment will be a <strong>group</strong> submission</li>
    <li>You will submit your <strong>correct Python code</strong> to <strong>GradeScope</strong> for this assignment.</li>
  </ul>
</div>

# Watch

<iframe width="1280" height="720" src="https://www.youtube.com/embed/Vx2SGrRcWAY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Since apparently AlgoTutorBot <del>CAN'T DO THE SIMPLE JOB HE WAS PROGRAMMED FOR</del> is having some trouble, we had to
change today's lesson a little. Originally, we were going to have you use an AVL Tree to make something really cool.
But now, we're going to have to fix the broken AVL code instead. Sigh.

* Download the AVL tree file here: <https://gist.github.com/acbart/0dab040d91c3c282f5aaed91ad54f9ac>

The AVL Tree implementation is quite simple, only letting you insert new elements and traverse them in order.
<del>So it's suprising that AlgoTutorBot couldn't even achieve this, but I guess you get what you paid for.</del>
When the algorithm works correctly, you should be able to use the algorithm to create a sorted list of values.
This is demonstrated by the unit tests provided alongside the AVL Tree.
Fortunately, the unit tests do not have any bugs <del>(that I know about, anyway)</del>.

As far as I can tell, the program is broken in seven places.
Each bug is small and shouldn't require fixing more than a couple lines.
You need to track the bugs down, fix them, and then put a comment at each bug location.
That comment should explain what you changed and give the name(s) of who found that specific bug.

Work with your group mates to find, fix, and label all the bugs in the program.
Then, at the top of your program, write a comment describing how your teammates went about debugging the
implementation.
Also clearly identify your group members name and emails.

### Submission

Submit the final version of your program on GradeScope here: <https://www.gradescope.com/courses/230699/assignments/1058536/>

You do not need to submit your unit tests.

Be sure to clearly identify all of your groupmates in the GradeScope submission.

<del>Sometimes I think AlgoTutorBot was a terrible investment.</del>