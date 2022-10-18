from pathlib import Path
import time

import numpy as np
from algorithms.greedy import GreedyAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solutions
from loader import InstanceLoader
from loader.config import ConfigLoader
from instance import MatrixRepresentation
from algorithms import RandomAlgorithm
from instance.mutations import Mutate


def alt_main():
    config = ConfigLoader("config.yaml")
    for selected_instance in config.selected_instances:
        loader = InstanceLoader(selected_instance)
        matrix_representation = MatrixRepresentation(loader.load())
        # greedy_solutions = Solutions(
        #     cities=loader.dimension, instances=loader.dimension, init_method="greedy"
        # )
        random_solutions = Solutions(
            cities=loader.dimension,
            instances=config.random_number_of_instances,
            init_method=config.genetic_init_method,
        )
        # algorithm_1 = GreedyAlgorithm(matrix_representation, greedy_solutions)
        algorithm = RandomAlgorithm(matrix_representation, random_solutions)
        algorithm.execute()
        random_solutions.update_best_solution()
        print(f"{random_solutions.best_solution=}")
        print(f"{random_solutions.best_distance=}")


def main():
    
    config = ConfigLoader("config.yaml")

    for selected_instance in config.selected_instances:
        loader = InstanceLoader(selected_instance)
        matrix_representation = MatrixRepresentation(loader.load())
        random_solutions = Solutions(
            cities=loader.dimension,
            instances=config.random_number_of_instances,
            init_method=config.genetic_init_method,
        )
        mutation = Mutate(config.genetic_mutation_method, config.genetic_mutation_rate)
        tmp = mutation.mutate(random_solutions.solution_array)
    import ipdb

    ipdb.set_trace()


if __name__ == "__main__":
    main()
    # alt_main()
