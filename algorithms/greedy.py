from functools import cached_property

import numpy as np
from algorithms.base import BaseTSPAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solution


class GreedyAlgorithm(BaseTSPAlgorithm):
    def __init__(self, matrix_representation: MatrixRepresentation):
        self.matrix_representation = matrix_representation

    @cached_property
    def cities_count(self) -> int:
        return len(self.adjacency_matrix)

    @cached_property
    def adjacency_matrix(self) -> np.ndarray:
        return self.matrix_representation.adjacency_matix

    def execute(self) -> list[int, Solution]:
        # best_city =
        """
        matrix = adjacency_array
        for
            matrix[city_idx].min(), zwracał index
            matrix = matrix[:indexu:,:index:]


        """
        best_distance = np.iinfo(np.int64).max
        avg_time = 0
        distance = 0
        for starting_city in range(self.cities_count):
            matrix = np.copy(self.adjacency_matrix)
            current_city = starting_city
            for idx in range(self.cities_count):
                # solution.add(tmp.argmin())
                if idx == self.cities_count - 1:
                    continue
                dst = matrix[current_city, :].min()
                next_city = matrix[current_city, :].argmin()
                distance += dst
                import time

                start = time.time_ns()
                matrix[current_city, :] = np.iinfo(np.int64).max
                matrix[:, current_city] = np.iinfo(np.int64).max
                stop = time.time_ns()
                current_city = next_city
                avg_time += stop
                avg_time -= start

            distance += self.adjacency_matrix[current_city, starting_city]
            if best_distance > distance:
                best_distance = distance

            xxx = time.time_ns()
            aaa = 7 in ["a", "b", "c", "d", 7]
            ddd = time.time_ns()
            res = xxx - ddd
        import ipdb

        ipdb.set_trace()

    def alt_execute(self):
        best_distance = np.iinfo(np.int64).max
        cities = [city_idx for city_idx in range(self.cities_count)]
        for starting_city in range(self.cities_count):
            visited_cities = []
            visited_cities.append(starting_city)
            for city in (cty for cty in cities if cty not in visited_cities):
                import ipdb

                ipdb.set_trace()
