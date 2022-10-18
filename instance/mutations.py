from instance.solution import Solutions
import numpy as np


class Mutate:
    def __init__(self, solutions: Solutions, mutation_method: str, mutation_rate: float) -> None:
        self.solutions = solutions
        self.mutation_method = mutation_method
        self.mutation_rate = mutation_rate

    def mutate(self) -> Solutions:
        instances = self._get_instances_for_mutation()
        if self.mutation_method == "swap":
            import ipdb; ipdb.set_trace()
            return self._swap(instances)
        elif self.mutation_method == "inverse":
            import ipdb; ipdb.set_trace()
            return self._inverse(instances)

    def _swap(self, instances: np.ndarray) -> np.ndarray:
        for instance in instances:
            indexes = np.random.randint(len(instance), size=2) # 2 indexes to be swaped
            import ipdb; ipdb.set_trace()
            instance[indexes[0]], instance[indexes[1]] = instance[indexes[1]], instance[indexes[0]]
            ipdb.set_trace()
        return instances

    def _inverse(self, instances: np.ndarray) -> np.ndarray:
        for instance in instances:
            indexes = np.random.randint(len(instance), size=2) # 2 indexes where inversion starts and ends
            instance[indexes[0], indexes[1]] = instance[indexes[0], indexes[1]][::-1] # inversing part of the list
            
        return instances

    # It has not been tested yet!
    def _get_instances_for_mutation(self):
        random_ints = np.random.rand(len(self.solutions.solution_array))
        to_be_mutated = np.where(random_ints<self.mutation_rate)[0]
        instances_for_mutation = self.solutions.solution_array[to_be_mutated, :] # to chyba niepotrzebne, potrzeba tylko indexów?

        return instances_for_mutation