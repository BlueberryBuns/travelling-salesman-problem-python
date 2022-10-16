from functools import cached_property
import logging
import numpy as np


class Solutions:
    def __init__(self, cities: int, instances: int, init_method: str):
        self.number_of_instances = instances
        self.number_of_cities = cities
        self.best_solution = np.zeros((cities), dtype=np.uint16)
        self.best_distance = np.Inf
        self.solution_array = self._initialize_solution_array(init_method)
        self.distance_array = np.zeros((instances, cities), dtype=float)

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
        solution_array = np.random.default_rng().permuted(solution_array, axis=1)
        return solution_array.astype(np.uint16)

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

    @cached_property
    def total_length(self) -> np.ndarray:
        return self.distance_array.sum(axis=1, dtype=np.uint64)

    @cached_property
    def min_value(self):
        return self.total_length.min()

    @cached_property
    def min_arg(self):
        return self.total_length.argmin()

    @cached_property
    def avg_value(self):
        return self.total_length.mean()

    @cached_property
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
