from functools import cached_property
import numpy as np


class Solutions:
    def __init__(self, cities, instances):
        self.best_solution = np.zeros((cities), dtype=np.uint16)
        self.best_distance = np.iinfo(np.uint64).max
        self.solution_array = np.zeros((instances, cities), dtype=np.uint16)
        self.distance_array = np.zeros((instances, cities), dtype=np.uint64)

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
        if self.best_distance > self.min_value():
            self.best_distance = self.min_value()
            self.best_solution = self.solution_array[self.min_arg()]
