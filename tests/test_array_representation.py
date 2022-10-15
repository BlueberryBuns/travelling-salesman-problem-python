import numpy as np
from instance.representation import Node, Representation, ArrayRepresentation

import pytest


@pytest.fixture
def representation():
    X = [565, 25, 345, 945, 845, 880, 25, 525, 580, 650, 1605]
    Y = [575, 185, 750, 685, 655, 660, 230, 1000, 1175, 1130, 620]
    node_list = [Node(a, b, c) for a, b, c in zip(X, Y, range(11))]
    return Representation(node_list)


def test_standard_reprwsentation(representation: Representation):
    print(representation.verticies_array)


def test_matrix_represetation(representation: Representation):
    ar = ArrayRepresentation(representation)
    print(ar.distance_matix)
    print(ar.distance_matix.dtype)
