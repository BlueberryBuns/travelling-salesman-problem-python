import logging
from pathlib import Path
from algorithms.greedy import GreedyAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solutions
from loader import InstanceLoader
from loader.config import ConfigLoader
from logging_setup import logging_setup
from instance import MatrixRepresentation
from algorithms import RandomAlgorithm


def alt_main():
    loader = InstanceLoader()
    config = ConfigLoader("config.yaml")

    for selected_instance in config.selected_instances:
        
        matrix_representation = MatrixRepresentation(loader.load(selected_instance))
        greedy_solution = Solutions(matrix_representation.adjacency_matix.shape[0], instances=100)
        import ipdb; ipdb.set_trace()
    # algorithm = GreedyAlgorithm(matrix_representation, )


def main():
    input_file = Path("example_instances/berlin11_modified.tsp")
    loader = InstanceLoader()
    config = ConfigLoader("config.yaml")
<<<<<<< HEAD
    # print(config._config)
    # import ipdb; ipdb.set_trace()
=======
    print(config._config)
    import ipdb

    ipdb.set_trace()
>>>>>>> 45c9268 (Add modified solution handling, update greedy algorithm)

    # print(config._config["genetic_algorithm"])
    # print(config._genetic_algorithm)
    # print(config.genetic_crosover_method)

    representation = loader.load(input_file)
    print(representation.verticies_list)

    matrixRep = MatrixRepresentation(representation)
    print(matrixRep.adjacency_matix)
    # import ipdb; ipdb.set_trace()
    # logging_setup()
    # logging.info("Test message")
    result = RandomAlgorithm(representation, matrixRep).execute()
    print(result)


if __name__ == "__main__":
    # main()
    alt_main()
