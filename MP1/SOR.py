import numpy as np

def gauss_seidel(A, iterations=3):
    N = len(A)
    B = A[:,N]
    X = np.zeros(len(A))
    _A = np.copy(A[:, :N])
    
    print("Iteration 0: \n", X)
    print("--------------------------------")

    for it in range(iterations):
        print("Iteration: {}".format(it+1))
        for i in range(N):
            # print("Solving X[{}]".format(i))
            X[i] = B[i] 
            # print("Initial X[{}]: {}".format(i, X[i]))
            for j in range(N):
                if j != i:
                    # print("A[{}][{}]: {} | X[{}]: {} | Prod: {}".format(i, j, A[i][j], j, X[j], A[i][j] * X[j]))
                    # print("Subtracting {}".format(A[i][j] * X[j]))
                    X[i] -= A[i][j] * X[j]
                    # print(X)
                    # print("New X[{}]: {}".format(i, X[i]))
            # print("Diving: {}".format(A[i][i]))
            X[i] /= A[i][i]
            # X[i] = X[i] / A[i]
        print(X)
        print("--------------------------------")

    # print(X)



if __name__ == "__main__":
    A = np.array([
        [5, -1, 2, 12], 
        [3, 8, -2, -25], 
        [1, 1, 4, 6]
    ])
    gauss_seidel(A)