from instance import representation
from instance import Node
from instance.solution import Solutions
import numpy as np

class Mutate:
    def __init__(self, solutions: Solutions) -> None:
        self.solutions = solutions
        self.swap_rate = 0.01 # 1%
        self.inversion_rate = 0.1
        self.random = np.random.randint(100, len(solutions.solution_array))

    def Swap(self) -> Solutions:

        return 0

    def Inverse(self) -> Solutions:
        return 0

class FixtureFactory:
    @classmethod
    def create_solution(cls) -> Solutions:
        sol = Solutions(cities=5, instances=5)
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