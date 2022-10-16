import numpy as np
from instance.representation import Node, Representation, MatrixRepresentation

import pytest


class FixtureCreator:
    X = [565, 25, 345, 945, 845, 880, 25, 525, 580, 650, 1605]
    Y = [575, 185, 750, 685, 655, 660, 230, 1000, 1175, 1130, 620]

    @classmethod
    def create_node_list(cls):
        return [Node(a, b, c) for a, b, c in zip(cls.X, cls.Y, range(11))]


@pytest.fixture
def representation():
    return Representation(FixtureCreator.create_node_list())


@pytest.fixture
def matrix_representation():
    return MatrixRepresentation(Representation(FixtureCreator.create_node_list()))
