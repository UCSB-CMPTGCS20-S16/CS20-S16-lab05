# CS20-S16-lab05

NOTE: THIS LAB IS NOT YET COMPLETE.    PLEASE COME BACK LATER
=============================================================

Introduction
============

More practice with writing functions and tests
----------------------------------------------

In this lab, we continue practicing writing functions and tests, in
the same style as some of our previous labs.

The difference is that the functions we are writing will be a bit more
challenging.

You may work individually, OR in a pair, as you see fit.

Step by Step
============

Step 0: Register as either working alone, or working in a pair
--------------------------------------------------------------

Make a directory or folder for lab04.  We suggest `~/cs20/lab04`,
which as you may recall, means:

* a `cs20` folder inside your home folder
* then, a `lab04` folder inside that.

We are now going to get two files from the web.

Step 1: Copy some code into `lab04Funcs.py`
-----------------------------------------

We are going to copy some code from `lab04Funcs.py`
into a file with the same name under your `~/cs20/lab04` folder

* As a plain file: [lab04Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab04/master/lab04Funcs.py)
* On github: [lab04Funcs.py on github](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab04/blob/master/lab04Funcs.py)

In IDLE, select "File=&gt;New Window" to open a new "untitled" window for Python code.

When it comes up, click and drag the window by its title bar over to the right of your Python Shell window.

Now, open this link. (You may want to "right click", or on Mac, "control-click", to open it in a new window or tab.)

Use the "Save As" option to save that file in the `~/cs20/lab04` folder with the name `lab04Funcs.py`

Step 2: Copy some more code from `lab04Tests.py`
-----------------------------------------------

Now we are going to do the same thing again, with a second file of Python code.

We are going to copy some code from `lab04Tests.py`
into a file with the same name under your `~/cs20/lab04` folder

* As a plain file: [lab04Tests.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab04/master/lab04Tests.py)
* On github: [lab04Tests.py on github](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab04/blob/master/lab04Tests.py)

* You may want to "right click", or on Mac, "control-click", to open it in a new window or tab.
* We want to copy code from that version of `lab04Tests.py` into a file with the same name under your `~/cs20/lab04` folder.

In IDLE, select "File=&gt;New Window" *again* to open *yet another* new "untitled" window for Python code.

When it comes up, click and drag the window some place so that you can get to it, your `lab04Funcs.py` window, the web browser window with `lab04Tests.py` and to your Python Shell window easily by clicking.

Use the "Save As" option to save that file in the`~/cs20/lab04` folder with the name `lab04Tests.py`

Remember that upper vs. lower case matter. Save it again if you didn't get it exactly right the first time, and use the `rm` command to remove (delete) any files that are in the wrong place.

Once you see that you have lab04Funcs.py and lab04Tests.py under your `~/cs20/lab04` directory, you are good to move on to the next step.

Step 3: Importing functions from our lab02 file
-----------------------------------------------

Take a look inside your lab04Funcs.py file, and you'll see these two lines near the top:

    from lab02Funcs import isList
    from lab02Funcs import isSimpleNumeric

What we are doing here is pulling in two functions from our lab02 work.

We are going to NEED an isList function and an isSimpleNumeric function to do the work for lab04. But, we don't want to have to write those functions from scratch.

So we can REUSE the code. All we have to do is copy over the lab02Funcs.py file from our lab02 directory into our lab04 directory.

So, make a copy of your lab02Funcs.py from the earlier lab, and put it in the same folder/directory with your lab04Funcs.py and lab04Tests.py files.

When you've copied the lab02Funcs.py file over, and you see that you have all three files that we are going to need for this week's lab, you can get started on the programming part.

Step 4: Fixing function stubs, adding functions, adding tests
-------------------------------------------------------------

As we discussed in lecture, when writing functions along with test cases, we often start with "stub" versions.

These allow us to "test the test" to make sure that when the function is bogus, that the tests work correctly.

If you look through the `lab04Funcs.py` file, you will see several function definitions that are "stub" versions.

Run the lab04Tests.py file, and you'll see that many of the tests are failing, because the function in question returns the string "stub" instead of the answer that it should.

Go through the file, and replace the stubs with correct values.

In addition, you'll also find:

-   several places in `lab04Funcs.py` where there are comments with "@@@" signs that tell you to add new function definitions.
-   several places in lab04Tests.py where there are comments with "@@@" signs that tell you to add new test cases

Follow all of the instructions.

-   As you follow the instructions with the @@@ in them, REMOVE THE COMMENTS THAT HAVE THE @@@ IN THEM.

You can always look back at the versions of the files on the web if you want to see what the instructions originally said.

If you leave any of the @@@ comments in the file, points may be deducted.

When you have:

-   fixed all the stubs, and the tests cases pass
-   added all the functions you are supposed to add
-   added all the test cases you are supposed to add

Then you are ready to submit!

### A few helpful hints

At the bottom of the file, you'll see that you can select either to run ALL tests, or ONLY the test for a certain function.

Follow the instructions there if you want to focus on just one function at a time.

Step 5: Getting ready to submit
-------------------------------

We are just about ready to submit your work for grading.

But first, some important preparation steps:

### Step 5a: Add your name(s) and email to the top of the file

This step is worth 10 points (10% of your grade) so don't forget it.

<b>(Yeah, "grade", ha ha. If you are in the CCS version of this course, just go with me on this.    It was easier to leave this all in that edit it out.   The "grade" stuff is still a good indication of how programming work is evaluated and assessed in traditional-style courses, so probably good for you to know in case you choose to study CS further.)</b>

At the top of BOTH the `lab04Funcs.py` file, and the `lab04Tests.py` file, add the following lines of code. They should be at the VERY top, the VERY first lines.

But, change the name here to YOUR name, the lab section to YOUR lab section, and the email to YOUR email (use your umail address, not a gmail, yahoo or hotmail address.)

Add the word SOLO or PAIR, and if working in a pair, put both names (one per line)

    # lab04Funcs.py  SOLO, Gina Gaucho, ggaucho@umail.ucsb.edu 

    # lab04Tests.py  SOLO, Gina Gaucho, ggaucho@umail.ucsb.edu 

OR:

    # lab04Funcs.py  PAIR, Gordon Gaucho, ggaucho@umail.ucsb.edu 
    # lab04Funcs.py  PAIR, Martin Perez, mperez07@umail.ucsb.edu 

    # lab04Tests.py  PAIR, Gordon Gaucho, ggaucho@umail.ucsb.edu 
    # lab04Tests.py  PAIR, Martin Perez, mperez07@umail.ucsb.edu 

### Step 5b: Check your lab against the grading rubric

To maximize your grade, it is good to check your OWN lab against the SAME criteria the TA and instructor will use to grade it—BEFORE you submit it!

Open these lab instructions in a second browser window. Scroll down to the bottom of the lab, to the grading section.

Find the list of grading criteria. Check your own work against each of those.

If there are any parts that don't make sense to you, be sure to ask the TA/Instructor about those.

If you see that you've done everything correctly, then you are ready to submit.

Step 6: Submit your assignment via submit.cs
-------------------------------------------------------

Here's the link: https://submit.cs.ucsb.edu/form/project/471/submission

If you happen to be working on CSIL, you can also submit by typing

```
~submit/submit -p 471 lab02Funcs.py lab04Funcs.py
```

Evaluation and Grading
======================

-   lab04 directory submitted (15 pts) and contains:
    -   lab03Funcs.py (5 pts)
    -   lab04Funcs.py (5 pts)
    -   lab04Tests.py (5 pts)

<!-- -->

-   In lab04Funcs.py:
    -   name(s) at top (10 pts)
    -   (15 pts) corrected problems with `notStringContainingE(word)` so that it passes tests
    -   (15 pts) corrected problems with `hasNoX(word)` so that it passes tests
    -   (30 pts) correct version of `isListOfIntegers(theList)`
    -   (30 pts) correct version of `isListOfEvenIntegers(theList)`
    -   (30 pts) correct version of `totalLength(listOfStrings)`
    -   (30 pts) correct version of `lengthOfEach(listOfStrings)`
    -   (30 pts) correct version of `countEvens(listOfInts)`
    -   (30 pts) correct version of `onlyEvens(listOfInts)`
    -   all @@@ comments removed (10 pts)



-   In `lab04Tests.py`:
    -   (10 pts) Nothing changed except adding comment to first lines with name
    -   Note: if tests are modified to make them pass (instead of modifying the code to make it pass the tests) then additional points may be deducted. Don't modify the tests. Modify the code so that it passes the tests.



-   General (30 pts)
    -   following instructions
    -   submitting work on time
    -   anything else specified in the instructions

<b>If you finish both lab03 and lab04 during this week's lab</b>

-   Then you are amazing! Turn in your homework, and have a nice day!

<hr>
Copyright 2014,2015, Phillip T. Conrad, CS Dept, UC Santa Barbara. Permission to copy for non-commercial, non-profit, educational purposes granted, provided appropriate credit is given; all other rights reserved.
