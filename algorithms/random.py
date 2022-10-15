from instance import Node
import numpy as np
from loader import InstanceLoader

# functions to be moved to base.py? or what's the base.py purpose?
# instance or representation?
class RandomSolver():

    def __init__(self):
        self._loader = InstanceLoader()

    def solve(self):
        representation = self._loader.load(".//source//berlin11_modified.tsp")
        min_distance = np.Inf
        min_route: list[Node]

        for i in range(1000):
            route = self._generate_route(representation)
            distance = self._calculate_distance(route)

            if distance < min_distance:
                min_distance = distance
                min_route = route

        return min_distance, min_route

    def _generate_route(self):
        return 0

    def _calculate_distance(self):
        return 0
    
    
