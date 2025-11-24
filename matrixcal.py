import numpy as np
print("\n============================================")
print("Welcome to the Simplified Matrix Calculator!")
print("============================================\n")
print("--- 1. Set Up Matrix A ---")
while True:
    try:
        rows_A=int(input("Enter the number of rows for Matrix A: "))
        cols_A=int(input("Enter the number of columns for Matrix A: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number for rows/columns.")
while True:
    try:
        expected_count=rows_A*cols_A
        print(f"Enter the {expected_count} entries for Matrix A in a single line, separated by spaces:")
        entries_A=list(map(float, input().split()))
        
        if(len(entries_A)!=expected_count):
            print(f"Error! Expected {expected_count} entries but you entered {len(entries_A)}. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please ensure all entries are numbers separated by spaces.")
matrix_A=np.array(entries_A).reshape(rows_A, cols_A)
print("\nMatrix A has been created:")
print(matrix_A)
is_A_square=(rows_A==cols_A)
determinant_A=np.linalg.det(matrix_A) if is_A_square else None
print("\n--- 2. Operations on Matrix A ---")
try:
    do_inverse_A=int(input("Calculate Inverse of A? (1 for Yes / 0 for No): "))
    do_determinant_A=int(input("Calculate Determinant of A? (1 for Yes / 0 for No): "))
    do_transpose_A=int(input("Calculate Transpose of A? (1 for Yes / 0 for No): "))
except ValueError:
    print("Invalid choice input. Skipping remaining operations for Matrix A.")
    do_inverse_A=do_determinant_A=do_transpose_A=0 

if(do_inverse_A==1):
    if(is_A_square and abs(determinant_A) > 1e-9):
        matrix_inv_A=np.linalg.inv(matrix_A)
        print(" The Inverse of Matrix A is:")
        print(matrix_inv_A)
    else:
        print("Matrix A is not invertible.")
if(do_determinant_A==1):
    if(is_A_square):
        print(f" The Determinant of Matrix A is: {determinant_A:.4f}")
    else:
        print("Cannot calculate determinant. Matrix A is not square.")
if(do_transpose_A==1):
    A_transpose=matrix_A.transpose()
    print("The Transpose of Matrix A is:")
    print(A_transpose)
print("\n--- 3. Combined Operations ---")
try:
    do_combined=int(input("Do you want to enter a second Matrix (B) for combined operations? (1 for Yes / 0 for No): "))
except ValueError:
    print("Invalid choice input for combined operations. Exiting combined section.")
    do_combined = 0
if(do_combined==1):
    print("\n--- Set Up Matrix B ---")
    while True:
        try:
            rows_B=int(input("Enter the number of rows for Matrix B: "))
            cols_B=int(input("Enter the number of columns for Matrix B: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for rows/columns.")
    while True:
        try:
            expected_count = rows_B * cols_B
            print(f"Enter the {expected_count} entries for Matrix B in a single line, separated by spaces:")
            entries_B = list(map(float, input().split()))
            if (len(entries_B)!=expected_count):
                print(f"Error! Expected {expected_count} entries but you entered {len(entries_B)}. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please ensure all entries are numbers separated by spaces.")
    matrix_B=np.array(entries_B).reshape(rows_B, cols_B)
    print("\nMatrix B has been created:")
    print(matrix_B)
    is_B_square=(rows_B==cols_B)
    determinant_B=np.linalg.det(matrix_B) if is_B_square else None
    print("\n--- Combined & Matrix B Operations ---")
    try:
        do_inverse_B=int(input("Calculate Inverse of B? (1/0): "))
        do_determinant_B=int(input("Calculate Determinant of B? (1/0): "))
        do_add=int(input("Calculate A + B? (1/0): "))
        do_subtract=int(input("Calculate A - B? (1/0): "))
        do_multiply=int(input("Calculate A * B? (1/0): "))
        do_transpose_B=int(input("Calculate Transpose of B? (1/0): "))
        do_identical=int(input("Check if A and B are identical? (1/0): "))
    except ValueError:
        print("Invalid choice input. Skipping remaining combined operations.")
        do_inverse_B=do_determinant_B=do_add=do_subtract=do_multiply=do_transpose_B=do_identical=0
    if (do_inverse_B==1):
        if(is_B_square ,abs(determinant_B) > 1e-9):
            matrix_inv_B=np.linalg.inv(matrix_B)
            print("The Inverse of Matrix B is:")
            print(matrix_inv_B)
        else:
            print("Matrix B is not invertible.")
    if(do_determinant_B==1):
        if (is_B_square):
            print(f"The Determinant of Matrix B is: {determinant_B:.4f}")
        else:
            print("Cannot calculate determinant. Matrix B is not square.")
    if (do_add==1):
        if (matrix_A.shape==matrix_B.shape):
            result_add=matrix_A+matrix_B
            print("\nThe sum of Matrix A and B is:")
            print(result_add)
        else:
            print("\nAddition failed. Matrices must have the same dimensions for addition.")
    if (do_subtract==1):
        if (matrix_A.shape==matrix_B.shape):
            result_sub=matrix_A-matrix_B
            print("\nThe difference (A - B) is:")
            print(result_sub)
        else:
            print("\nSubtraction failed. Matrices must have the same dimensions for subtraction.")
    if (do_multiply==1):
        if(cols_A==rows_B):
            result_mult=np.dot(matrix_A, matrix_B)
            print("\n The product (A * B) is:")
            print(result_mult)
        else:
            print("\n Multiplication failed. Columns of A must equal Rows of B.")
    if (do_transpose_B==1):
        B_transpose=matrix_B.transpose()
        print("\nThe Transpose of Matrix B is:")
        print(B_transpose)
    if (do_identical==1):
        if(np.array_equal(matrix_A, matrix_B)):
            print("\nMatrix A and Matrix B are *Identical*.")
        else:
            print("\nMatrix A and Matrix B are *Not Identical*.")
print("\n============================================")
print("-------- Thank You for using the Calculator! ----------")
print("============================================")
