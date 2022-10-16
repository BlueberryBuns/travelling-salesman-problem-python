from dataclasses import dataclass
import logging
from numba import njit
import numpy as np
from tqdm import tqdm


# @dataclass(frozen=True)
# class Node:
#     x: int
#     y: int
#     index: int


# @dataclass(frozen=True)
# class Representation:
#     verticies_list: list[Node]


@dataclass(frozen=True)
class Repres:
    nodes_array: np.ndarray


@njit
def calculate_distance(a: np.ndarray, b: np.ndarray) -> float:
    if a[0] == b[0]:
        return np.Inf
    distance = np.sqrt(np.square(a[1] - b[1]) + np.square(a[2] - b[2]))
    return distance


class MatrixRepresentation:
    def __init__(self, representation: Repres) -> None:
        self.adjacency_matix = self._populate_matrix(representation.nodes_array)

    def _create_empty_matrix(self, nodes_array: np.ndarray) -> np.ndarray:
        size = nodes_array.shape[0]
        return np.empty((size, size))

    @staticmethod
    def _convert_to_array_int(array: np.ndarray):
        # return np.rint(array).astype(np.int64)
        return np.rint(array).astype(np.uint64)

    @staticmethod
    @njit
    def _generate_neighbour_distance(
        current_city: np.ndarray, nodes_array: np.ndarray, distance_matrix: np.ndarray
    ) -> np.ndarray:
        current_city_index = int(current_city[0])
        for neighbour in nodes_array:
            neighbour_index = int(neighbour[0])
            distance_matrix[current_city_index][neighbour_index] = calculate_distance(
                current_city, neighbour
            )
        return distance_matrix

    def _populate_matrix(self, nodes_array: np.ndarray) -> np.ndarray:
        distance_matrix = self._create_empty_matrix(nodes_array)
        logging.warning("Creating Matrix representation of TSP")
        for city in tqdm(nodes_array):
            # for neighbour in representation.verticies_list:
            #     distance_matix[city.index][neighbour.index] = self._calculate_distance(
            #         city, neighbour
            #     )
            distance_matrix = self._generate_neighbour_distance(
                city, nodes_array, distance_matrix
            )
        logging.warning("Matrix creation finished successfully!")
        return distance_matrix.astype(np.float64)
