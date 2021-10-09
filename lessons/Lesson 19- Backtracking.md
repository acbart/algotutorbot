---
waltz:
  title: Lesson 19- Backtracking
  resource: assignment
  url: https://udel.instructure.com/courses/1563197/assignments/8785398
  published: true
  settings:
    points_possible:
    grading_type: points
    submission:
      submission_types:
      - none
    timing:
      due_at: ''
      unlock_at: 'April 16 2021, 0400 AM'
      lock_at: ''
    secrecy:
      anonymize_students: false
      anonymous_grading: false
---

<div class="alert alert-info -waltz-literal">
  <ul>
    <li>Watch the video and refer to the other videos as needed.</li>
    <li>If you need help, join the Ohyay workspace at <strong>9:05am</strong>.</li>
    <li>This assignment has you work <strong>individually</strong></li>
    <li>You will submit your working code and the password on <strong>Canvas</strong>.</li>
  </ul>
</div>

# Watch

<iframe width="1180" height="664" src="https://www.youtube.com/embed/3OZhUluPmeo"
  title="YouTube video player" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Do

Ada and Babbage have been taken! I need your help rescuing them.

The password that you need can be discovered using the `mysterious_drive.zip` that I gave you before.

Reuse the `search_zip` function you wrote in the previous lesson. This time, search for a `.py` file instead of a `.json`.
The file should be named `password_hash.py`; this module contains a function named `simple_hash` that AlgoTutorBot used to 
hash the password of the Interrogation Chamber. Dr. Bart has already determined that the hash code is `81445731`;
now you need to figure out what the original password is by brute-forcing it from a dictionary.

Adjacent to the `.py` file that you find will be a file named `dictionary.txt`. This file contains a list of words
that AlgoTutorBot prefers to use in its passwords. You will need to read in this file and write a Backtracking algorithm
that recursively tests every possible combination of words until it finds the first one that matches the previously
identified hash.

Extract the `.txt` and `.py` file and place them in a new directory side-by-side.
You can extract the `.zip` file, but you will not be able to open it until you have cracked AlgoTutorBot's password.
That zip file will have a link to a video that you should watch after you have cracked the password.

## Submission

When you are done, you will need to submit a Python file that contains all the code you ended up writing to find
the files and to crack the hash. I expect to see a complete backtracking algorithm!

**Include the cracked password as a comment at the top of your submitted file.**

Submit the file here on Canvas for full points.
You do not need to document the file, but make sure the code is readable.

## Supplemental Videos

If you are having trouble with writing a Backtracking algorithm, here are some videos that were created last
year. They go into a good amount of depth about Backtracking.

<iframe width="1180" height="664" src="https://www.youtube.com/embed/Gz-LICeHYwg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>