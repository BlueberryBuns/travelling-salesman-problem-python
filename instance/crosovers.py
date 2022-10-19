from abc import ABC, abstractmethod
import random
import time

import numpy as np
from numba import njit


class BaseCrossover(ABC):
    @staticmethod
    @abstractmethod
    def crossover(solution_a: np.ndarray, solution_b: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class PMX(BaseCrossover):
    def __init__(self):
        ...

    @njit
    def crossover(solution_a: np.ndarray, solution_b: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class OX(BaseCrossover):
    def __init__(self):
        ...

    def crossover(
        self, solution_a: np.ndarray, solution_b: np.ndarray
    ) -> list[np.ndarray]:
        total_length = solution_a.shape[0]
        cut_a = random.randint(0, total_length - 3)
        cut_b = random.randint(cut_a + 1, total_length - 1)
        new_solution_a = self._alter_solutions(solution_a, solution_b, cut_a, cut_b)
        new_solution_b = self._alter_solutions(solution_b, solution_a, cut_a, cut_b)
        return [new_solution_a.astype(int), new_solution_b.astype(int)]

    @staticmethod
    @njit
    def _alter_solutions(
        solution_a: np.ndarray, solution_b: np.ndarray, cut_a: int, cut_b: int
    ) -> np.ndarray:
        new_solution = np.zeros(shape=solution_a.shape)
        new_solution[cut_a:cut_b] = solution_a[cut_a:cut_b]
        custom_iterator = 0
        for city in solution_b:
            if custom_iterator == cut_a:
                diff = cut_b - cut_a
                custom_iterator += diff

            if city in new_solution[cut_a:cut_b]:
                continue
            else:
                new_solution[custom_iterator] = city
                custom_iterator += 1
        return new_solution

# x = np.arange(416, dtype=int)
# y = np.arange(416, dtype=int)[::-1]
# ox = OX()

# for _ in range(100):
#     start = time.time_ns()
#     x, y = ox.crossover(x, y)
#     stop = time.time_ns()
#     print((stop - start) / 1000, "us")
# a,b = ox.crossover(a,b)

# print(a)
# print(b)
