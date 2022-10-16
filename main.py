from pathlib import Path
<<<<<<< HEAD
=======
import time

import numpy as np
>>>>>>> b76bfb5 (testing)
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
            init_method="random",
        )
        # algorithm_1 = GreedyAlgorithm(matrix_representation, greedy_solutions)
        algorithm = RandomAlgorithm(matrix_representation, random_solutions)
        algorithm.execute()
        random_solutions.update_best_solution()
        print(f"{random_solutions.best_solution=}")
        print(f"{random_solutions.best_distance=}")


def main():
    input_file = Path("example_instances/berlin11_modified.tsp")
    loader = InstanceLoader()
    config = ConfigLoader("config.yaml")
<<<<<<< HEAD
=======

    def create_solution() -> Solutions:
        sol = Solutions(cities=5, instances=5)
        sol.solution_array = np.array(
            (
                (0, 1, 2, 3, 4),
                (1, 4, 3, 2, 0),
                (0, 1, 3, 2, 4),
                (1, 0, 3, 2, 4),
                (1, 4, 0, 2, 3),
            )
        )
        sol.distance_array = np.array(
            (
                (12, 99, 510, 322, 146),
                (10, 11, 50, 32, 16),
                (19, 19, 3000, 322, 256),
                (109, 101, 500, 302, 106),
                (120, 909, 510, 322, 146),
            )
        )
        return sol

    solutionss = create_solution()

    mutated_solutions = Mutate(solutionss).mutate()
    import ipdb; ipdb.set_trace()
    # print(config._config)
    # import ipdb; ipdb.set_trace()
>>>>>>> b76bfb5 (testing)

    # print(config._config["genetic_algorithm"])
    # print(config._genetic_algorithm)
    # print(config.genetic_crosover_method)

    # representation = loader.load(input_file)
    # print(representation.verticies_list)

<<<<<<< HEAD
    matrixRep = MatrixRepresentation(representation)

    result = RandomAlgorithm(representation, matrixRep).execute()
    print(result)
=======
    # matrixRep = MatrixRepresentation(representation)
    # print(matrixRep.adjacency_matix)
    # import ipdb; ipdb.set_trace()
    # logging_setup()
    # logging.info("Test message")
    # result = RandomAlgorithm(representation, matrixRep).execute()
    # print(result)
>>>>>>> b76bfb5 (testing)


if __name__ == "__main__":
    main()
    # alt_main()
