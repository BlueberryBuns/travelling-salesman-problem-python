from pathlib import Path
import time

import numpy as np
from algorithms import greedy
from algorithms.genetic import GeneticAlgorithm
from algorithms.greedy import GreedyAlgorithm
from instance.representation import MatrixRepresentation
from instance.solution import Solutions
from loader import InstanceLoader
from loader.config import ConfigLoader
from instance import MatrixRepresentation
from algorithms import RandomAlgorithm
from instance.mutations import Mutatation

from instance.selection import Selection


def alt_main():
    config = ConfigLoader("config.yaml")
    for selected_instance in config.selected_instances:
        loader = InstanceLoader(selected_instance)
        matrix_representation = MatrixRepresentation(loader.load())
        greedy_solutions = Solutions(
            cities=loader.dimension,
            instances=loader.dimension,
            init_method="greedy",
            matrix_representation=matrix_representation,
        )
        random_solutions = Solutions(
            cities=loader.dimension,
            instances=config.random_number_of_instances,
            init_method=config.genetic_init_method,
            matrix_representation=matrix_representation,
        )
        algorithm = GreedyAlgorithm(matrix_representation, greedy_solutions)
        algorithm_random = RandomAlgorithm(matrix_representation, random_solutions)
        algorithm.execute()
        algorithm_random.execute()
        random_solutions.update_best_solution()
        print(f"{random_solutions.best_solution=}")
        print(f"{random_solutions.best_distance=}")
        greedy_solutions.update_best_solution()
        print(f"{greedy_solutions.best_solution=}")
        print(f"{greedy_solutions.best_distance=}")
        algorithm.print_matrix()


def main():

    config = ConfigLoader("config.yaml")

    for selected_instance in config.selected_instances:
        loader = InstanceLoader(selected_instance)
        matrix_representation = MatrixRepresentation(loader.load())

        solutions = Solutions(
            cities=loader.dimension,
            instances=config.genetic_population_size,
            init_method=config.genetic_init_method,
            matrix_representation=matrix_representation,
        )

        solutions.evaluate()

        selection = Selection(
            selection_method="tournament",
            tournaments_number=config.genetic_population_size,
            tournament_size=config.genetic_tournament_size,
            population_size=config.genetic_population_size,
        )

        mutation = Mutatation(
            mutation_method=config.genetic_mutation_method,
            mutation_rate=config.genetic_mutation_rate,
        )

        genetic_algorithm = GeneticAlgorithm(
            solutions=solutions, selection=selection, mutation=mutation, generations=config.genetic_generations
        )

        genetic_algorithm.execute()
        # solutions.evaluate()
        # population = solutions.solution_array  # init population
        # evaluation = solutions.total_length  # ratings

        # import ipdb

        # selected_solutions = selection.select(population, evaluation)
        # ipdb.set_trace()

        # mutation = Mutate(config.genetic_mutation_method, config.genetic_mutation_rate)
        # tmp = mutation.mutate(random_solutions.solution_array)


if __name__ == "__main__":
    main()
    # alt_main()
