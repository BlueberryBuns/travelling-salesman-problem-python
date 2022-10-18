from instance.solution import Solutions
import numpy as np
from numba import njit


class Mutate:
    def __init__(self, mutation_method: str, mutation_rate: float) -> None:
        # self.solutions = solutions
        self.mutation_method = mutation_method
        self.mutation_rate = mutation_rate

    def mutate(self, solutions_array: np.ndarray) -> np.ndarray:
        instances, altered_indexes = self._get_instances_for_mutation(solutions_array)
        indexes = np.random.randint(len(instances[0]), size=(len(instances), 2))
        indexes.sort()
        if self.mutation_method == "swap":
            altered_solutions = self._swap(instances, indexes)
        elif self.mutation_method == "inverse":
            altered_solutions = self._inverse(instances, indexes)
        return self.assign_new_solutions(
            solutions_array, altered_indexes, altered_solutions
        )

    @staticmethod
    @njit
    def assign_new_solutions(
        solutions_array: np.ndarray,
        altered_indexes: np.ndarray,
        altered_solutions: np.ndarray,
    ):
        for index, altered_index in enumerate(altered_indexes):
            solutions_array[altered_index] = altered_solutions[index]
        return solutions_array

    @staticmethod
    @njit
    def _swap(instances: np.ndarray, indexes: np.ndarray) -> np.ndarray:
        for idx, instance in enumerate(instances):
            instance[indexes[idx][0]], instance[indexes[idx][1]] = (
                instance[indexes[idx][1]],
                instance[indexes[idx][0]],
            )
        return instances

    @staticmethod
    @njit
    def _inverse(instances: np.ndarray, indexes: np.ndarray) -> np.ndarray:
        for idx, instance in enumerate(instances):
            instance[indexes[idx][0] : indexes[idx][1]] = instance[
                indexes[idx][0] : indexes[idx][1]
            ][::-1]
        return instances

    def _get_instances_for_mutation(self, solution_array: np.ndarray):
        random_ints = np.random.rand(len(solution_array))
        indexes_to_be_mutated = np.where(random_ints < self.mutation_rate)[0]
        instances_for_mutation = solution_array[
            indexes_to_be_mutated, :
        ]  # to chyba niepotrzebne, potrzeba tylko indexów?

        return instances_for_mutation, indexes_to_be_mutated
