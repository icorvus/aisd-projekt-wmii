import numpy as np


def create_random_matrix_for_flow(n: int) -> np.ndarray:
    matrix = np.random.randint(1, 11, size=(n, n))
    np.fill_diagonal(matrix, 0)
    return matrix
