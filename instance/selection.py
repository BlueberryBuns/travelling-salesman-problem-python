import random
from instance.solution import Solutions
import numpy as np


class Selection:
    def __init__(self, selection_method: str, tournaments_number: int, population_size: int) -> None:
        self.selection_method = selection_method
        self.tournaments_number = tournaments_number
        self.population_size = population_size

    def select(self, solutions_array: np.ndarray, distance_array: list[float]) -> np.ndarray:
        selected_solutions = []
        if self.selection_method == "tournament":
            for turn in range(self.tournaments_number):
                selected_solution = self._tournament(solutions_array, distance_array)
                selected_solutions.append(selected_solution)
        elif self.selection_method == "roulette":
            # for turn in range():
            #     selected_solution = self._roulette()
            #     selected_solutions.append(selected_solution)
            print("Roulette")

    def _tournament(self, solutions_array: np.ndarray, distance_array: list[float]):
        best = -np.Inf
        best_index = None
        selected_indexes = random.sample(range(self.population_size), self.tournaments_number)

        for specimen_index in selected_indexes:
            if best < distance_array[best_index]:
                best_index = specimen_index
                best = distance_array[best_index]

        return solutions_array[best_index]

    # to be implemented later
    def _roulette():
        return None