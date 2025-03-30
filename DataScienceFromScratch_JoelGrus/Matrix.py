from typing import Callable
from typing import Tuple

Vector = List[float]
Matrix = List[Vector]


"""Returns (# of rows of A, # of columns of A"""
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


"""Returns the ith row of A (as a Vector)"""
def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


"""Returns the jth column of A (as a Vector)"""
def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


"""Returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i,j)"""
def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


"""Returns the n x n identity matrix"""
def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i,j: 1 if i==j else 0)
    

assert shape([[1,2,3], [4,5,6]]) == (2,3)


assert identity_matrix(5) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]