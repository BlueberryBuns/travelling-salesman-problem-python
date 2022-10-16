from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    index: int


@dataclass(frozen=True)
class Representation:
    verticies_list: list[Node]


class MatrixRepresentation:
    def __init__(self, representation: Representation) -> None:
        self.adjacency_matix = self._populate_matrix(representation)

    @staticmethod
    def _calculate_distance(a: Node, b: Node) -> float:
        if a.index == b.index:
            return np.iinfo(np.int64).max
        distance = np.sqrt(np.square(a.x - b.x) + np.square(a.y - b.y))
        return distance

    def _create_cities_matrix(self, representation: Representation) -> np.ndarray:
        size = len(representation.verticies_list)
        return np.empty((size, size))

    @staticmethod
    def _convert_to_array_int(array: np.ndarray):
        return np.rint(array).astype(int)

    def _populate_matrix(self, representation: Representation) -> np.ndarray:
        distance_matix = self._create_cities_matrix(representation)
        for city in representation.verticies_list:
            for neighbour in representation.verticies_list:
                distance_matix[city.index][neighbour.index] = self._calculate_distance(
                    city, neighbour
                )
        return self._convert_to_array_int(distance_matix)
