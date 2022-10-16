import random
from instance import Node
import numpy as np
import yaml
from functools import cached_property

from instance.representation import MatrixRepresentation, Representation

class RandomAlgorithm:
    def __init__(self, representation: Representation, adjacency_array: MatrixRepresentation):
        self.representation = representation
        self.adjacecny_array = adjacency_array

    def execute(self):
        min_distance = np.iinfo(np.int64).max
        min_route: list[Node]

        for i in range(10000): # to be read from config
            route = self._generate_route(self.representation)
            distance = self._calculate_route_distance(route, self.adjacecny_array)

            if distance < min_distance:
                min_distance = distance
                min_route = route

        return min_distance, min_route


    def _generate_route(self, representation: Representation) -> list[Node]:

        random_route = representation.verticies_list.copy()
        random.shuffle(random_route)

        return random_route


    def _calculate_route_distance(self, route: list[Node], adjacency_array: MatrixRepresentation) -> int:

        distance = 0
        matrix = adjacency_array.adjacency_matix
        for i in range(len(route)-1):
            distance += matrix[route[i-1].index][route[i].index]

        return distance


    
    
