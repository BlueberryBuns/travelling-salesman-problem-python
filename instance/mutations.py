from functools import cached_property
import random
from instance import representation
from instance import Node
from instance import solution
from instance.solution import Solutions
import numpy as np


swap_rate = 0.01 # 1%
inversion_rate = 0.1

class Mutate:
    def __init__(self, solutions: Solutions) -> None:
        self.solutions = solutions

    def mutate(self) -> Solutions:
        config_value = "swap"

        if config_value == "swap":
            self._swap()
        else:
            self._inverse()

    def _swap(self) -> Solutions:
        return 0

    def _inverse(self) -> Solutions:
        return 0


    def _get_instances_for_mutation(self, rate: float):
        random_ints = np.random.randint(100, len(self.solutions.solution_array))
        to_be_mutated = np.where(random_ints<)




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