# Khansole Academy

## Overview
Khansole Academy is a beginner-friendly Python program that helps students practice addition. It generates random addition questions, checks the user's answers, and tracks consecutive correct answers.

The goal is to answer **three questions correctly in a row** to master addition.

## Features
- Generates two random numbers for each addition question.
- Accepts the user's answer.
- Checks whether the answer is correct.
- Displays feedback for correct and incorrect answers.
- Tracks consecutive correct answers.
- Resets the counter after an incorrect answer.
- Ends the game after three consecutive correct answers.

## How It Works
1. Displays the title `Khansole Academy`.
2. Initializes `correct_in_a_row` to zero.
3. Generates two random numbers using `randint(10, 99)`.
4. Displays an addition question and asks the user for an answer.
5. Increases the counter if the answer is correct.
6. Resets the counter to zero if the answer is incorrect.
7. Repeats until the user answers three questions correctly in a row.
8. Displays a congratulatory message when the goal is achieved.

## Python Concepts Used
- **Functions:** Organize code using `main()`.
- **Loops:** Repeat questions using a `while` loop.
- **Conditional statements:** Check answers using `if` and `else`.
- **Variables:** Store numbers, answers, and the consecutive-correct counter.
- **Random numbers:** Generate questions using `randint()`.
- **User input:** Receive answers using `input()`.
- **Type conversion:** Convert input to an integer using `int()`.
- **F-strings:** Display variables inside messages.

## Week 2: Khansole Academy Twists

The following twists are listed in the Code in Place Week 2 Khansole Academy assignments. Each twist introduces a possible extension to the original program.

1. **Three's a Crowd** — Explore a variation involving three participants or elements.
2. **Mind Your Type** — Explore handling input types and ensuring answers are processed correctly.
3. **Multiplication Tables** — Extend arithmetic practice to multiplication.
4. **Story Time** — Add a story-based element to the math practice.
5. **Set the Goal** — Allow the target for consecutive correct answers to be adjusted.
6. **Too Generous** — Explore a variation in how the program handles answers or scoring.
7. **Report Card** — Extend the program to provide a summary of the user's performance.
8. **Fair Share** — Explore a variation involving sharing or distributing results fairly.
9. **Stuck at One** — Explore a special case involving the consecutive-correct counter.
10. **Level Up** — Introduce progression through different levels of difficulty.
11. **Plus or Minus** — Extend the game to include addition and subtraction.

Note: These descriptions are brief interpretations of the twist titles, not verified summaries of the assignment instructions.

## Requirements
- Python 3
- No external libraries required; `random` is included with Python.

## How to Run
1. Save the program as `khansole_academy.py`.
2. Open a terminal in the same folder.
3. Run:

   ```bash
   python khansole_academy.py
   ```

## Learning Objectives
This project helps beginners practice Python fundamentals, including loops, conditional statements, variables, user input, random number generation, and basic arithmetic. The twists provide opportunities to modify the original program and explore additional programming concepts.
