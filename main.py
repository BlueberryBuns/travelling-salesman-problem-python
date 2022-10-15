<<<<<<< HEAD
from loader import InstanceLoader

loader = InstanceLoader()

representation = loader.load(".\\source\\berlin11_modified.tsp")

print(representation.nodes_array)
=======
import logging
from logging_setup import logging_setup

if __name__ == "__main__":
    logging_setup()
    logging.info("Test message")
>>>>>>> ba815bf (Add array representation of graph)
