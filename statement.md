# Project Statement: Simplified Matrix Calculator

## 1. Problem Statement
In engineering and mathematics courses, students often have to solve complex matrix problems by hand. Calculating things like the "Inverse" or "Determinant" of a matrix manually is very slow and it is easy to make small calculation mistakes. Students currently lack a simple, text-based tool that allows them to quickly verify their manual answers or perform heavy calculations instantly without needing complex software like MATLAB.

## 2. Scope of the Project
The Simplified Matrix Calculator is a Python-based application designed to solve linear algebra problems. The scope of this project includes:
* Matrix Creation: Allowing users to build matrices of any size (rows and columns).
* Mathematical Logic: Automating complex operations like Inverses, Determinants, and Transposes using the NumPy library.
* Arithmetic Operations: Enabling users to Add, Subtract, and Multiply two different matrices.
* Validation: The system automatically checks if an operation is mathematically possible (e.g., ensuring matrices are the same size before adding) to prevent errors.

## 3. Target Users
* Engineering Students: To verify their homework answers for Linear Algebra.
* Math Teachers: To quickly generate problem sets or solutions.
* Programming Beginners: To understand how data arrays work in Python.

## 4. High-Level Features
* Dynamic Inputs: Users can input data for matrices of any size, not just standard 2x2 or 3x3 grids.
* Smart Error Handling: The system acts like a guide; if a user enters a letter instead of a number, it asks them to try again politely instead of crashing.
* Step-by-Step Menu: The program runs in a loop, allowing users to perform multiple calculations (like finding the Inverse of A, then multiplying A by B) in one session.
* Instant Feedback: Results are displayed immediately in a clean, readable format.
