import math
from typing import List

Vector = List[float]
sameSizeError = "vectors must be the same length"

class Vector:

    def add(v: Vector, w: Vector) -> Vector:
        assert len(v) == len(w), sameSizeError
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    def subtract(v: Vector, w: Vector) -> Vector:
        assert len(v) == len(w), sameSizeError
        return [v_i - w_i for v_i, w_i in zip(v, w)]


    """Sums all corresponding elements"""
    def vector_sum(vectors: List[Vector]) -> Vector:
        assert vectors, "cannot sum empty set of vectors"

        num_elements = len(vectors[0])
        assert all(len(v) == num_elements for v in vectors), sameSizeError

        return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


    """Multiplies every element by c"""
    def scalar_multiply(c: float, v: Vector) -> Vector:
        return [c * v_i for v_i in v]


    """Computes the element-wise average"""
    def vector_mean(vectors: List[Vector]) -> Vector:
        n = len(vectors)
        return scalar_multiply(1/n, vector_sum(vectors))


    """Computes v_1 * w_1 + ... + v_n * w_n"""
    def dot(v: Vector, w: Vector) -> float:
        assert len(v) == len(w), sameSizeError
        return sum(v_i * w_i for v_i, w_i in zip(v, w))


    """Returns v_1 * v_1 + ... + v_n * v_n"""
    def sum_of_squares(v: Vector) -> float:
        return dot(v,v)


    """Returns the magnitude (or length) of v"""
    def magnitude(v: Vector) -> float:
        return math.sqrt(sum_of_squares(v))


    """Computes (v_1 - w_1)**2 + ... + (v_n - w_n)**2 """
    def squared_distance(v: Vector, w: Vector) -> float:
        return sum_of_squares(subtract(v,w))


    """Computes the distance between v and w"""
    def distance(v: Vector, w: Vector) -> float:
        return magnitude(subtract(v,w))


    #[1+3+5+7, 2+4+6+8]
    assert vector_sum([1,2], [3,4], [5,6], [7,8]) == [16,20]

    #[2*1, 2*2, 2*3]
    assert scalar_multiply(2, [1,2,3]) == [2,4,6]

    #[(1+3+5)/3, (2+4+6)/3]
    assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]

    #1*4 + 2*5 + 3*6
    assert dot([1,2,3], [4,5,6]) == 32

    #sqrt(3*3 + 4*4)
    assert magnitude([3,4]) == 5
