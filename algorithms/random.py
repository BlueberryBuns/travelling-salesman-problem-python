import random
import time

from tqdm import tqdm

# from instance import Node
import numpy as np
from numba import njit

from instance.representation import MatrixRepresentation  # , Representation
from instance.solution import Solutions


class RandomAlgorithm:
    def __init__(
        self, matrix_representation: MatrixRepresentation, solutions: Solutions
    ):
        self.solutions = solutions
        self.matrix_representation = matrix_representation

    def execute(self):
        for index, solution in enumerate(tqdm(self.solutions.solution_array)):
            self.solutions.distance_array[index] = self.calculate_distance_array(
                solution, self.matrix_representation.adjacency_matix
            )

    @staticmethod
    @njit
    def calculate_distance_array(solution: np.ndarray, adjacency_array: np.ndarray):
        result = np.zeros(len(solution))
        for index, current_city in enumerate(solution):
            next_city_index = (index + 1) % len(solution)
            result[index] = adjacency_array[current_city][solution[next_city_index]]
        return result

    # def alt_execute(self):
    #     min_distance = np.iinfo(np.int64).max
    #     min_route: list[Node]

    #     for i in range(self.number_of_instances):  # to be read from config
    #         route = self._generate_route()
    #         distance = self._calculate_route_distance(route, self.matrix_representation)

    #         if distance < min_distance:
    #             min_distance = distance
    #             min_route = route

    #     return min_distance, min_route

    # def _generate_route(self, representation: Representation) -> list[Node]:

    #     random_route = representation.verticies_list.copy()
    #     random.shuffle(random_route)

    #     return random_route

    # def _calculate_route_distance(
    #     self, route: list[Node], adjacency_array: MatrixRepresentation
    # ) -> int:

    #     distance = 0
    #     matrix = adjacency_array.adjacency_matix
    #     for i in range(len(route) - 1):
    #         distance += matrix[route[i - 1].index][route[i].index]

    #     return distance
