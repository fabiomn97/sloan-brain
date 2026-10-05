---
title: "15060 software setup"
course: "15.060"
course_name: "Data, Models, and Decisions: E"
term: "Fall Term (AY 2026-2027)"
type: "reading"
date: "2026-08-31"
source: "canvas"
url: "https://canvas.mit.edu/courses/38514/files/6741365"
original: "raw/fall-term-ay-2026-2027/15.060/files/software/15060-software-setup.pdf"
locator_kind: "page"
---

## Page 1

15.060 Data, Models, and Decisions

Setting up Google Colab, @Risk, and MS Excel Solver

Please complete prior to Recitation 1

This document will guide you in setting up your computer with all the software required for DMD. In particular, you will 1) check if you can access Google Colab, 2) install the Horizon client to access an Excel simulation add-in called @Risk via the Sloan Remote Lab), and 3) activate Excel’s built-in Solver optimization add-in.

Tasks #2 and #3 have a corresponding short online question designed to test if your installation task was completed successfully. The questions are available on Canvas under the software module. You are required to submit your answers on Canvas once you have successfully completed the corresponding tasks.

You will need an active internet connection. We recommend that you close all open programs on your computer before working through the following tasks.

Task 1. Google Colab

1) Create a Google account (if you use Gmail, you already have one) and install the Chrome browser (if you aren’t already a Chrome user)

2) Type ‘colab.new’ in the Chrome URL bar. You should see something like this:

3) Click on Connect (see screenshot)

## Page 2

4) After a second or two, you should see something like this:

5) Type 2 + 2 in the text box and click the black arrow to the left. You should see the answer 4 appear below (see screenshot)

6) You are all set! If at any point, you ran into difficulties, please email your TA.

2/4

## Page 3

Task 2. Setting up and using @Risk

In this task you will set up access to the Excel simulation add-in @Risk via the Sloan Remote Lab.

One-time installation and first-time access

Go here* and follow the instructions to download the Horizon client, install it on your machine, and login to the Sloan Remote Lab for the first time. Please carefully follow the instructions step by step.

- Note that the instructions for Windows and Mac are different.
- The instructions may say “VMWare Horizon” while what you see may be “Omnissa Horizon”. They are the same.

* If you receive a “Bad Request”, make sure to clear your browsing history and try again.

Every time you want to use @Risk

1. Log into the Sloan Remote Lab 2. Wait for the remote desktop to load. This may take a few minutes. 3. Using the search bar on your desktop, search for @Risk and click to open it. Excel will open automatically but may take a while. 4. When you see a "Welcome to @Risk" box, you're good to go. You can ‘x’ out of this box.

(If at any point you run into difficulties, please email your TA).

Task 2 Question

5. Download the spreadsheet simple_simulation_model.xlsx from Canvas (in Files > Software) to your computer. 6. Log into the Sloan Remote Lab and open @Risk (i.e., follow the four steps described above in Every time you want to use @Risk) 7. Open simple_simulation_model.xlsx from within the Excel that you fired up in the previous step (i.e., not the Excel on your laptop). Your remote desktop can access files from your laptop through the Network Drive (Z). See the last paragraph of the installation how-to page above for more details.

8. Click the button on the menu bar. 9. After the simulation is completed, you should see an output window like the one below. What is the mean value of Revenue reported in the output window? (Hint: Read off the value in the pink oval below.🙂)

3/4

## Page 4

Important: If you get timed out or locked out of the remote desktop when you are using @Risk at any point during the course, this is how you get back in:

1. Click on the icon inside the pink oval. If you can't see it, it's probably because you're in full screen mode - press Esc and it should appear. You will be asked for a password.

2. Type your MIT Kerberos password (unfortunately, you can't copy-paste your Kerberos password into this text box. You will need to manually type it in).

(If at any point you run into difficulties, please email your TA).

Task 3. Setting up Solver

In this task you will ensure that Excel’s built-in optimization add-in, Solver, is ready for use. Solver comes standard with Microsoft Excel, but sometimes the add-in needs to be `activated’.

Note: You should set up Solver on Excel directly on your personal laptops (instructions to download and activate Excel here).

Microsoft Windows:

- Launch Microsoft Excel
- Go to File > Options
- Click Add-Ins
- Scroll down to the Manage box, select Excel Add-ins and click Go
- Check the Solve Add-in box if it is not already checked
- Verify that a Solver menu item now appears under the Data ribbon

MacOS:

- Launch Microsoft Excel
- Select Excel Add-ins from the Tools menu
- Check the Solve Add-in box if it is not already checked
- Verify that a Solver menu item now appears under the Data ribbon

Task 3 Question

Launch Microsoft Excel and open the spreadsheet simple_optimization_model.xlsx provided on Canvas. Select Data > Solver and click Solve to run the defined optimization model. When the results come back, click OK. What is the optimal price reported in cell C11?

4/4
