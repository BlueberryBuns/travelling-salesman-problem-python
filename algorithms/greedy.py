from functools import cached_property

import numpy as np
import numpy.ma as ma
from algorithms.base import BaseTSPAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solutions


class GreedyAlgorithm(BaseTSPAlgorithm):
    def __init__(
        self, matrix_representation: MatrixRepresentation, solutions: Solutions
    ):
        self.solutions = solutions
        self.matrix_representation = matrix_representation  

    @cached_property
    def cities_count(self) -> int:
        return len(self.adjacency_matrix)

    @cached_property
    def cities(self) -> np.ndarray:
        return np.arange(self.cities_count, dtype=np.uint16)

    @cached_property
    def adjacency_matrix(self) -> np.ndarray:
        return self.matrix_representation.adjacency_matix

    @staticmethod
    def remove_visited_cities(matrix: np.ndarray, current_city: int):
        matrix[current_city, :] = np.iinfo(np.int64).max
        matrix[:, current_city] = np.iinfo(np.int64).max
        return matrix

    def execute(self) -> list[int, Solutions]:
        for starting_city in range(self.cities_count):
            matrix = np.copy(self.adjacency_matrix)
            current_city = starting_city
            for idx in range(self.cities_count):
                if idx == self.cities_count - 1:
                    continue
                dst = matrix[current_city, :].min()
                next_city = matrix[current_city, :].argmin()
                self.solutions.distance_array[starting_city][idx] = dst
                self.solutions.solution_array[starting_city][idx] = next_city
                matrix = self.remove_visited_cities(matrix, current_city)
                # matrix[current_city, :] = np.iinfo(np.int64).max
                # matrix[:, current_city] = np.iinfo(np.int64).max
                current_city = next_city

            self.solutions.distance_array[starting_city][self.cities_count - 1] = self.adjacency_matrix[current_city, starting_city]
            self.solutions.solution_array[starting_city][self.cities_count - 1] = next_city

        self.solutions.update_best_solution()

        import ipdb

        ipdb.set_trace()

    def alt_execute(self):
        best_distance = np.iinfo(np.int64).max
        for starting_city in range(self.cities_count):
            visited_cities = []
            current_city = starting_city
            for city_idx in range(self.cities_count):
                visited_cities.append(current_city)
                remaining_cities = [c for c in self.cities if not c in visited_cities]
                for i in remaining_cities:

                    # XDDD = self.adjacency_matrix[current_city, remaining_cities]
                    import ipdb

                    ipdb.set_trace()
                x = self.adjacency_matrix[
                    current_city,
                ]
                mask = ma.masked_where(
                    self.adjacency_matrix[current_city, :] > 500,
                    self.adjacency_matrix[current_city, :],
                )

                import ipdb

                ipdb.set_trace()
