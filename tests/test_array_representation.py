from instance.representation import Node, Representation, MatrixRepresentation

import pytest

from instance.solution import Solutions


# def test_standard_reprwsentation(representation: Representation):
#     print(representation.verticies_list)


# def test_matrix_represetation(matrix_representation: MatrixRepresentation):
#     print(matrix_representation)
#     print("*" * 30)
#     print(matrix_representation.adjacency_matix)

#     print(matrix_representation.adjacency_matix.dtype)


def test_solution_representation(solutions: Solutions):
    print(solutions.avg_value)
    import ipdb

    ipdb.set_trace()
