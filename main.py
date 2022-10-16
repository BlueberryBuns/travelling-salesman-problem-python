from pathlib import Path
from algorithms.greedy import GreedyAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solutions
from loader import InstanceLoader
from loader.config import ConfigLoader
from instance import MatrixRepresentation
from algorithms import RandomAlgorithm


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

    # print(config._config["genetic_algorithm"])
    # print(config._genetic_algorithm)
    # print(config.genetic_crosover_method)

    representation = loader.load(input_file)
    print(representation.verticies_list)

    matrixRep = MatrixRepresentation(representation)

    result = RandomAlgorithm(representation, matrixRep).execute()
    print(result)


if __name__ == "__main__":
    # main()
    alt_main()
