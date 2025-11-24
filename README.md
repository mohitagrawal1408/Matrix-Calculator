# Simplified Matrix Calculator

## Overview of the Project
The Simplified Matrix Calculator is a command-line tool built with Python. It automates the tedious math involved in Linear Algebra. By using this tool, users can enter raw data for matrices and instantly get results for operations that would take minutes to solve by hand. It is designed to be lightweight, fast, and impossible to crash with bad inputs.

## Features
* Determinant & Inverse Calculator: Instantly finds these properties for any square matrix.
* Matrix Arithmetic: Supports Addition (A + B), Subtraction (A - B), and Multiplication (A * B).
* Transpose Function: Swaps the rows and columns of a matrix instantly.
* Identity Checker: Compares two matrices to see if they are identical.
* Safe Mode: Prevents mathematical errors (like trying to invert a singular matrix) by warning the user first.

## Technologies/Tools Used
* Language: Python 3
* Core Library: NumPy (for efficient mathematical computing)
* Interface: Console / Command Line Interface (CLI)

## Steps to Install & Run the Project
1. Install Python: Ensure Python is installed on your computer.
2. Install NumPy: This project requires the NumPy library. Open your terminal or command prompt and type:
   pip install numpy
3. Download the Code: Save the project file as matrix_calculator.py.
4. Run the Application:
   * Open your terminal in the folder where you saved the file.
   * Run the following command:
   python matrix_calculator.py

## Instructions for Testing
To verify the project is working correctly, follow these test steps:

1. Test Addition:
   * Run the program.
   * Create Matrix A with 2 rows and 2 columns (Values: 1 2 3 4).
   * Choose to add a second matrix.
   * Create Matrix B with 2 rows and 2 columns (Values: 1 1 1 1).
   * Select "Calculate A + B".
   * Expected Result: The output should show a matrix with values 2 3 4 5.

2. Test Error Handling:
   * Restart the program.
   * When asked for the number of rows, type "hello" instead of a number.
   * Expected Result: The system should say "Invalid input" and ask you to enter the number again.
