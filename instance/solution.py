from functools import cached_property
import logging
import numpy as np
from numba import njit
from tqdm import tqdm

from instance.representation import MatrixRepresentation


class Solutions:
    def __init__(
        self,
        cities: int,
        instances: int,
        init_method: str,
        matrix_representation: MatrixRepresentation,
    ):
        self.number_of_instances = instances
        self.number_of_cities = cities
        self.best_solution = np.zeros((cities), dtype=np.uint16)
        self.best_distance = np.Inf
        self.solution_array = self._initialize_solution_array(init_method)
        self.distance_array = np.zeros((instances, cities), dtype=np.float32)
        self.matrix_representation = matrix_representation

    def _initialize_solution_array(self, method: str):
        try:
            method_mapping = {"random": self.random_init, "greedy": self.greedy_init}
            return method_mapping[method](
                self.number_of_instances, self.number_of_cities
            )
        except KeyError:
            raise Exception("Unsuported init method while setting up solution array")

    def random_init(self, n_instances, n_cities):
        solution_array = np.arange(n_cities * n_instances).reshape(
            (n_instances, n_cities)
        )
        solution_array %= n_cities
        solution_array = solution_array.astype(np.uint16)
        solution_array = np.random.default_rng().permuted(solution_array, axis=1)
        return solution_array

    def greedy_init(self, n_instances, n_cities):
        if n_cities == n_instances:
            logging.info(
                "Number of instances == number of cities, performing greedy search"
            )
            return np.zeros(
                (self.number_of_instances, self.number_of_cities), dtype=np.uint16
            )
        elif n_instances > n_cities:
            logging.info(
                "Number of instances > number of cities, performing greedy search, filling remaining data with random search"
            )
            raise NotImplementedError
        else:
            raise AttributeError(
                "Number of cities cannot be lower than number of instances!"
            )

    @property
    def total_length(self) -> np.ndarray:
        return self.distance_array.sum(axis=1, dtype=np.float32)

    @property
    def min_value(self):
        return self.total_length.min()

    @property
    def min_arg(self):
        return self.total_length.argmin()

    @property
    def avg_value(self):
        return self.total_length.mean()

    @property
    def max_value(self):
        return self.total_length.max()

    def sort_values(self) -> None:
        soreted_vals = self.total_length.argsort()
        self.solution_array = self.solution_array[soreted_vals]
        self.distance_array = self.distance_array[soreted_vals]

    def update_best_solution(self):
        if self.best_distance > self.min_value:
            self.best_distance = self.min_value
            self.best_solution = self.solution_array[self.min_arg]

    @staticmethod
    @njit
    def calculate_distance_array(solution: np.ndarray, adjacency_array: np.ndarray):
        result = np.zeros(len(solution))
        for index, current_city in enumerate(solution):
            next_city_index = (index + 1) % len(solution)
            result[index] = adjacency_array[current_city][solution[next_city_index]]
        return result

    def calculate_distance_of_all_solutions(self):
        for index, solution in enumerate(tqdm(self.solution_array)):
            self.distance_array[index] = self.calculate_distance_array(
                solution, self.matrix_representation.adjacency_matix
            )

    def validate(self):
        ...

    def log_to_csv(self):
        ...

    def evaluate(self):
        self.calculate_distance_of_all_solutions()
        self.validate()
        self.update_best_solution()
        self.log_to_csv()
