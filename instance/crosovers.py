from abc import ABC, abstractmethod
import random
import time

import numpy as np
from numba import njit

class BaseCrossover:

    @abstractmethod
    def crossover(solution_a: np.ndarray, solution_b: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def execute(self, population: np.ndarray) -> np.ndarray:
        indexes = np.arange(len(population))
        np.random.shuffle(indexes)
        for i in range(1, len(indexes), 2):
            population[i-1], population[i] = self.crossover(population[i-1], population[i])
            # Last one (unaltered) is not overwritten if the population size is odd
        return population



@njit
def get_final_value_from_mapping(
    mapped_values_0: np.ndarray, mapped_values_1: np.ndarray, value: int
) -> int:
    continue_discovery = True
    current_value = value
    while continue_discovery:
        if current_value in mapped_values_0:
            idx = np.where(mapped_values_0 == current_value)[0][0]
            current_value = mapped_values_1[idx]
        else:
            continue_discovery = False
    return current_value


class PMX(BaseCrossover):
    def __init__(self):
        ...

    def crossover(
        self, solution_a: np.ndarray, solution_b: np.ndarray
    ) -> list[np.ndarray]:
        total_length = solution_a.shape[0]
        cut_a = random.randint(0, total_length - 3)
        cut_b = random.randint(cut_a + 1, total_length)
        solution_1, solution_2 = self._alter_solutions(
            solution_a, solution_b, cut_a, cut_b
        )
        return [solution_1.astype(int), solution_2.astype(int)]

    @staticmethod
    @njit
    def _alter_solutions(
        solution_a: np.ndarray, solution_b: np.ndarray, cut_a: int, cut_b: int
    ) -> np.ndarray:
        total_length = solution_a.shape[0]
        new_solution_a = np.zeros(total_length)
        new_solution_b = np.zeros(total_length)
        solution_array = np.zeros((2, total_length))
        mapping_a = solution_a[cut_a : cut_b + 1]
        mapping_b = solution_b[cut_a : cut_b + 1]
        new_solution_a[cut_a : cut_b + 1] = solution_b[cut_a : cut_b + 1]
        new_solution_b[cut_a : cut_b + 1] = solution_a[cut_a : cut_b + 1]
        for jj in range(total_length):
            if jj >= cut_a and jj <= cut_b:
                continue
            if solution_a[jj] in mapping_b:
                new_solution_a[jj] = get_final_value_from_mapping(
                    mapping_b, mapping_a, solution_a[jj]
                )
            else:
                new_solution_a[jj] = solution_a[jj]

            if solution_b[jj] in mapping_a:
                new_solution_b[jj] = get_final_value_from_mapping(
                    mapping_a, mapping_b, solution_b[jj]
                )
            else:
                new_solution_b[jj] = solution_b[jj]
        solution_array[0] = new_solution_a
        solution_array[1] = new_solution_b
        return solution_array


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
                mapping_length = cut_b - cut_a
                custom_iterator += mapping_length
            if city in new_solution[cut_a:cut_b]:
                continue
            else:
                new_solution[custom_iterator] = city
                custom_iterator += 1
        return new_solution


# x = np.arange(100, dtype=int)
# y = np.arange(100, dtype=int)[::-1]
# pmx = PMX()
# # ox = OX()

# # x,y = pmx.crossover(x,y)
# for _ in range(10):
#     start = time.time_ns()
#     solution_a, solution_b = pmx.crossover(x, y)
#     stop = time.time_ns()
#     # print(solution_a, "\n", solution_b, "\n\n")
#     print((stop - start) / 1000, "us")
# print("*" * 50)
# for _ in range(10):
#     start = time.time_ns()
#     solution_a, solution_b = ox.crossover(x, y)
#     stop = time.time_ns()
#     # print(solution_a, "\n", solution_b, "\n\n")
#     print((stop - start) / 1000, "us")
