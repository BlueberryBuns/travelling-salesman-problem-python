import logging
from pathlib import Path
from loader import InstanceLoader
from loader.config import ConfigLoader
from logging_setup import logging_setup
from instance import MatrixRepresentation
from algorithms import RandomAlgorithm


def main():
    input_file = Path("example_instances/berlin11_modified.tsp")
    loader = InstanceLoader()
    config = ConfigLoader("config.yaml")
    # print(config._config)
    # import ipdb; ipdb.set_trace()

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
    main()
