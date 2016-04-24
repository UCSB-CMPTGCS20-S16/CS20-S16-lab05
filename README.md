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

Step 0: Create a folder/directory for lab05
--------------------------------------------------------------

Make a directory or folder for lab05.  We suggest `~/cs20/lab05`,
which as you may recall, means:

* a `cs20` folder inside your home folder
* then, a `lab05` folder inside that.

We are now going to get two files from the web.

Step 1: Copy some code into `lab05Funcs.py`
-----------------------------------------

We are going to copy some code from `lab05Funcs.py`
into a file with the same name under your `~/cs20/lab05` folder

In IDLE, select "File=&gt;New Window" to open a new "untitled" window for Python code.

When it comes up, click and drag the window by its title bar over to the right of your Python Shell window.

Now, open one of these links and copy-paste into your new untitled file. (You may want to "right click", or on Mac, "control-click", to open it in a new window or tab.)

* As a plain file: [lab05Funcs.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab05/master/lab05Funcs.py)
* On github: [lab05Funcs.py on github](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab05/blob/master/lab05Funcs.py)

Use the "Save As" option to save that file in the`~/cs20/lab05` folder with the name `lab05Funcs.py`

Alternatively, from the front page of the repository, [UCSB-CMPTGCS20-S16/CS20-S16-lab05](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab05), right click `lab05Funcs.py` and use the "Save Link As" option to save that file in the `~/cs20/lab05` folder with the name `lab05Funcs.py`

Step 2: Copy some more code from `lab05Tests.py`
-----------------------------------------------

Now we are going to do the same thing again, with a second file of Python code.

We are going to copy some code from `lab05Tests.py`
into a file with the same name under your `~/cs20/lab05` folder

In IDLE, select "File=&gt;New Window" *again* to open *yet another* new "untitled" window for Python code, and open one of these links to copy the code into this new file.

* As a plain file: [lab05Tests.py](https://raw.githubusercontent.com/UCSB-CMPTGCS20-S16/CS20-S16-lab05/master/lab05Tests.py)
* On github: [lab05Tests.py on github](https://github.com/UCSB-CMPTGCS20-S16/CS20-S16-lab05/blob/master/lab05Tests.py)

Use the "Save As" option to save that file in the`~/cs20/lab05` folder with the name `lab05Tests.py`

Or, use the same alternate method from Step 1.

Remember that upper vs. lower case matter. Save it again if you didn't get it exactly right the first time, and use the `rm` command to remove (delete) any files that are in the wrong place.

Once you see that you have lab05Funcs.py and lab05Tests.py under your `~/cs20/lab05` directory, you are good to move on to the next step.

Step 3: Importing functions from our lab02 file
-----------------------------------------------

Take a look inside your lab05Funcs.py file, and you'll see this line near the top:

    from lab02Funcs import isList

What we are doing here is pulling in a function from our lab02 work.

We are going to NEED an isList function to do the work for lab05. But, we don't want to have to write those functions from scratch.

So we can REUSE the code. All we have to do is copy over the lab02Funcs.py file from our lab02 directory into our lab05 directory.

So, make a copy of your lab02Funcs.py from the earlier lab, and put it in the same folder/directory with your lab05Funcs.py and lab05Tests.py files.

When you've copied the lab02Funcs.py file over, and you see that you have all three files that we are going to need for this week's lab, you can get started on the programming part.

Step 4: Fixing function stubs, adding functions, adding tests
-------------------------------------------------------------

As we discussed in lecture, when writing functions along with test cases, we often start with "stub" versions.

These allow us to "test the test" to make sure that when the function is bogus, that the tests work correctly.

If you look through the `lab05Funcs.py` file, you will see several function definitions that are "stub" versions.

Run the `lab05Tests.py` file, and you'll see that many of the tests are failing, because the function in question returns the string "stub" instead of the answer that it should.

Go through the file, and replace the stubs with correct values.

In addition, you'll also find:

-   several places in `lab05Funcs.py` where there are comments with "@@@" signs that tell you to add new function definitions
-   several places in `lab05Tests.py` where there are comments with "@@@" signs that tell you to add new test cases

Follow all of the instructions.

-   As you follow the instructions with the @@@ in them, REMOVE THE COMMENTS THAT HAVE THE @@@ IN THEM.

You can always look back at the versions of the files on the web if you want to see what the instructions originally said.

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

<b>(Again, "grade", ha ha. If you are in the CCS version of this course, just go with it, even if the point values don't necessarily matter. The "grade" stuff is still a good indication of how programming work is evaluated and assessed in traditional-style courses, so it's probably good for you to know in case you choose to study CS further.)</b>

At the top of BOTH the `lab05Funcs.py` file, and the `lab05Tests.py` file, add the following lines of code. They should be at the VERY top, the VERY first lines.

But, change the name here to YOUR name, and the email to YOUR email (use your umail address, not a gmail, yahoo or hotmail address.)

Add the word SOLO or PAIR, and if working in a pair, put both names (one per line)

    # lab05Funcs.py  SOLO, Gina Gaucho, ggaucho@umail.ucsb.edu 

    # lab05Tests.py  SOLO, Gina Gaucho, ggaucho@umail.ucsb.edu 

OR:

    # lab05Funcs.py  PAIR, Gordon Gaucho, ggaucho@umail.ucsb.edu 
    # lab05Funcs.py  PAIR, Martin Perez, mperez07@umail.ucsb.edu 

    # lab05Tests.py  PAIR, Gordon Gaucho, ggaucho@umail.ucsb.edu 
    # lab05Tests.py  PAIR, Martin Perez, mperez07@umail.ucsb.edu 

### Step 5b: Check your lab against the grading rubric

Open these lab instructions in a second browser window. Scroll down to the bottom of the lab, to the grading section.

Find the list of grading criteria. Check your own work against each of those.

If there are any parts that don't make sense to you, be sure to ask about those.

If you see that you've done everything correctly, then you are ready to submit.

Step 6: Submit your assignment via submit.cs
-------------------------------------------------------

@@@@@@ UPDATE THIS LINK AND THE COMMAND
Here's the link: https://submit.cs.ucsb.edu/form/project/471/submission

If you happen to be working on CSIL, you can also submit by typing

```
~submit/submit -p 471 lab02Funcs.py lab04Funcs.py
```

Evaluation and Grading
======================

-   lab05 directory submitted (15 pts) and contains (with correctly spelled names)
    -   lab02Funcs.py (5 pts)
    -   lab05Funcs.py (5 pts)
    -   lab05Tests.py (5 pts)

-   In lab05Funcs.py:
    -   Correct implementation of smallestInt() (40 pts)
    -   Correct implementation of indexOfSmallestInt() (40 pts)
    -   Correct implementation of longestString() (40 pts)
    -   Correct implementation of indexOfShortestString() (40 pts)
    
-   In lab05Tests.py:
    -   Six tests (ten points each) for smallestInt (60 pts)

Note: if tests are modified to make them pass (instead of modifying the code to make it pass the tests) then additional points may be deducted. Don't modify the tests. Modify the code so that it passes the tests.

-   General (50 pts)
    -   all (@@@) comments removed in both files
    -   submitting work on time
    -   registering your pair or solo on Gauchospace
    -   adding names to top of files
    -   anything else specified in the instructions

<hr>
Copyright 2014,2015, Phillip T. Conrad, CS Dept, UC Santa Barbara. Permission to copy for non-commercial, non-profit, educational purposes granted, provided appropriate credit is given; all other rights reserved.
