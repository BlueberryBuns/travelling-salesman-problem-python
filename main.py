import logging
from pathlib import Path
from loader import InstanceLoader
from logging_setup import logging_setup


def main():
    input_file = Path("example_instances/berlin11_modified.tsp")
    loader = InstanceLoader()
    representation = loader.load(input_file)
    print(representation.verticies_list)

    logging_setup()
    logging.info("Test message")


if __name__ == "__main__":
    main()
