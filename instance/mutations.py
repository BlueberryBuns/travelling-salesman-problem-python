from instance import Solutions
import numpy as np


class Mutate:
    def __init__(self, solutions: Solutions) -> None:
        self.solutions = solutions

    def mutate(self) -> Solutions:
        config_value = "swap"

        if config_value == "swap":
            mutation_rate = 0.5
            instances = self._get_instances_for_mutation(mutation_rate)
            return self._swap(instances)
        elif config_value == "inverse":
            mutation_rate = 0.1
            instances = self._get_instances_for_mutation(mutation_rate)
            return self._inverse(instances)

    def _swap(self, instances: np.ndarray) -> np.ndarray:
        return 0

    def _inverse(self, instances: np.ndarray) -> np.ndarray:
        return 0

    # It has not been tested yet!
    def _get_instances_for_mutation(self, rate: float):

        random_ints = np.random.randint(100, len(self.solutions.solution_array))
        to_be_mutated = np.where(random_ints<rate*100)
        instances_for_mutation = self.solutions.solution_array[to_be_mutated, :]

        return instances_for_mutation