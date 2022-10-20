import random
from instance.solution import Solutions
import numpy as np
import ipdb
from numba import njit


class Selection:
    def __init__(
        self,
        selection_method: str,
        tournaments_number: int,
        population_size: int,
        tournament_size: int,
    ) -> None:
        self.selection_method = selection_method
        self.tournaments_number = tournaments_number
        self.tournament_size = tournament_size
        self.population_size = population_size

    def select(
        self, solutions_array: np.ndarray, rating_array: list[float]
    ) -> np.ndarray:
        selected_solutions = np.zeros(solutions_array.shape)
        if self.selection_method == "tournament":
            for turn in range(self.tournaments_number):
                # ipdb.set_trace()
                selected_solution = self._tournament(solutions_array, rating_array)
                selected_solutions[turn] = selected_solution
            return selected_solutions.astype(int)
        elif self.selection_method == "roulette":
            raise NotImplementedError
            for turn in range():
                selected_solution = self._roulette()
                selected_solutions.append(selected_solution)

    def _tournament(self, solutions_array: np.ndarray, distance_array: np.ndarray):
        selected_indexes = random.sample(
            range(self.population_size), self.tournament_size
        )
        # ipdb.set_trace()
        current_minimal = distance_array[selected_indexes].min()
        best_index = np.where(distance_array == current_minimal)[0][0]
        return solutions_array[best_index]

    # to be implemented later
    def _roulette():
        return None
