import numpy as np 

def swap_row(A, i, j):
    A[[i, j]] = A[[j, i]]
    return A

def make_row_echelon_form(A):
    N = len(A)
    for i in range(0, N):
        # Search for index of the maximum value in column i
        max_row = np.argmax(A[:,i])
        
        # Swap maximum row with row i
        if i != (N-1):
            swap_row(A, max_row, i)
        
        # Make all rows below row i 0 
        for k in range(i+1, N):
            c = -A[k][i] / A[i][i]
            for j in range(i, N+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
    
    return A

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
    A = np.array([
        [-3, 2, -1, -1], 
        [6, -6, 7, -7], 
        [3, -4, 4, -6]
    ])
    print('A: ', A[:, :len(A)])
    print('b: ', A[:, len(A):len(A)+1])
    x = gauss_elimination(A)
    print('x: ', x)
