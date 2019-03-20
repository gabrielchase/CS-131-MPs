import numpy as np

def successive_overrelaxation(A, X, w, iterations=3):
    N = len(A)
    B = A[:,N]
    if not len(X):
        X = np.zeros(len(A)) 
    _A = np.copy(A[:, :N])
    
    print("Iteration 0: \n", X)
    print("--------------------------------")

    for iteration in range(1, iterations):
        print("Iteration: {}".format(iteration))
        for i in range(N):
            result = B[i]
            for j in range(N):
                if j != i:
                    result -= A[i][j] * X[j]

            result = (result / A[i][i])
            X[i] = ((1 - w) * X[i]) + (result * w)
        
        print(X)
        print("--------------------------------")


def gauss_seidel(A, X=[], iterations=3):
    N = len(A)
    B = A[:,N]
    if not len(X):
        X = np.zeros(len(A)) 
    _A = np.copy(A[:, :N])
    
    print("Iteration 0: \n", X)
    print("--------------------------------")

    for iteration in range(1, iterations):
        print("Iteration: {}".format(iteration))
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
        [2, -1, 0, 0], 
        [-1, 2, -1, 1], 
        [0, -1, 2, 2]
    ])
    # gauss_seidel(A, [0, .5, 1])
    # print("***********")
    successive_overrelaxation(A, [0, .5, 1], 1.2)

# [
#         [5, -1, 2, 12], 
#         [3, 8, -2, -25], 
#         [1, 1, 4, 6]
#     ]

