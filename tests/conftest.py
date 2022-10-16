import numpy as np
from instance.representation import Node, Representation, MatrixRepresentation

import pytest

from instance.solution import Solutions


class FixtureCreator:
    X = [565, 25, 345, 945, 845, 880, 25, 525, 580, 650, 1605]
    Y = [575, 185, 750, 685, 655, 660, 230, 1000, 1175, 1130, 620]

    @classmethod
    def create_node_list(cls):
        return [Node(a, b, c) for a, b, c in zip(cls.X, cls.Y, range(11))]

    @classmethod
    def create_solution(cls) -> Solutions:
        sol = Solutions(cities=5, instances=2)
        sol.solution_array = np.array(
            (
                (0, 1, 2, 3, 4),
                (1, 4, 3, 2, 0),
                (0, 1, 3, 2, 4),
                (1, 0, 3, 2, 4),
                (1, 4, 0, 2, 3),
            )
        )
        sol.distance_array = np.array(
            (
                (12, 99, 510, 322, 146),
                (10, 11, 50, 32, 16),
                (19, 19, 3000, 322, 256),
                (109, 101, 500, 302, 106),
                (120, 909, 510, 322, 146),
            )
        )
        return sol


@pytest.fixture
def representation():
    return Representation(FixtureCreator.create_node_list())


@pytest.fixture
def matrix_representation():
    return MatrixRepresentation(Representation(FixtureCreator.create_node_list()))


@pytest.fixture
def solutions():
    return FixtureCreator.create_solution()
