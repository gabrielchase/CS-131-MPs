import numpy as np 

A = np.array([
    [-3, 2, -1, -1], 
    [6, -6, 7, -7], 
    [3, -4, 4, -6]
])

def swap_row(A, i, j):
    A_copy = A
    A_copy[[i, j]] = A_copy[[j, i]]
    return A_copy

def make_row_echelon_form(A):
    A_copy = A
    N = len(A)
    for i in range(0, N):
        # Search for index of the maximum value in column i
        max_row = np.argmax(A[:,i])
        
        # Swap maximum row with current row (column by column)
        if i != (N-1):
            swap_row(A, max_row, i)
        
        # Make all rows below this one 0 in current column
        for k in range(i+1, N):
            c = -A[k][i]/A[i][i]
            for j in range(i, N+1):
                if i == j:
                    A_copy[k][j] = 0
                else:
                    A_copy[k][j] += c * A[i][j]
    
    return A_copy

def backward_substitution(A):
    N = len(A)
    x = [0 for i in range(N)]
    
    for i in range(N-1, -1, -1):
        x[i] = A[i][N] / A[i][i]
        for k in range(i-1, -1, -1):
            A[k][N] -= A[k][i] * x[i]
    return x

def gauss_elimination(A):
    N = len(A)
    A = make_row_echelon_form(A)
    x = backward_substitution(A)
    return x

if __name__ == "__main__":
    print('A: ', A[:, :len(A)])
    print('b: ', A[:, len(A):len(A)+1])
    x = gauss_elimination(A)
    print('x: ', x)
