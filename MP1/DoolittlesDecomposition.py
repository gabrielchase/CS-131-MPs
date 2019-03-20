import numpy as np

def initialize_l(N):
    L = np.zeros((N, N))
    for i in range(N):
        L[i][i] = 1
    
    return L

def swap_row(A, i, j):
    A[[i, j]] = A[[j, i]]
    return A

def compute_y(L, B, N):
    y = np.zeros(N)

    # Backward substitution to compute y
    for i in range(N):
        y[i] = B[i] / L[i][i]
        for j in range(i):
            y[i] -= y[j] * L[i][j]

    return y

def compute_x(U, Y, N):
    Y_copy = np.copy(Y)
    x = np.zeros(N)

    for i in range(N-1, -1, -1):
        x[i] = Y_copy[i] / U[i][i]
        for j in range (i-1,-1,-1):
            Y_copy[j] -= x[i] * U[j][i]

    return x

def lu_decomposition(A):
    N = len(A)
    L = initialize_l(N)
    U = A[:,:N]
    B = A[:,N]

    print('INITIALIZE L: \n', L)
    print('INITIALIZE U: \n', U)
    print('B: ', B)

    for i in range(0, N):
        # Search for index of the maximum value in column i
        # max_row = np.argmax(U[:,i])

        # Swap maximum row with row i
        # print('before swap: ', U)
        # if i != (N-1):
        #     swap_row(U, max_row, i)
        # print('after swap: ', U)

        # Compute for L and U
        for j in range(i+1, N):
            factor = -(U[j][i] / U[i][i])
            L[j][i] = -factor
            
            # Compute U
            for k in range(i, N):
                U[j][k] += factor * U[i][k]

        # Make all values below diagonal in U a value of 0
        for j in range(N):
            if j < i:
                U[i][j] = 0

        Y = compute_y(L, B, N)

    X = compute_x(U, Y, N)

    return L, U, Y, X

    

if __name__ == "__main__":
    A = np.array([
        [1, 4, 1, 7],
        [1, 6, -1, 13],
        [2, -1, 2, 5]
    ])

    [1, 4, 1]
    [0, 2, -2]
    [0, 0, -9] 
    print('A: \n', A)

    L, U, Y, X = lu_decomposition(A)

    print('---- AFTER LU DECOMPOSITION ----')
    print('L: \n', L)
    print('U: \n', U)
    print('Y: \n', Y)
    print('X: \n', X)
