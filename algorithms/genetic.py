import logging

from tqdm import tqdm
from instance.crosovers import BaseCrossover
from instance.solution import Solutions

import ipdb
from instance.selection import Selection
from instance.mutations import Mutatation


class GeneticAlgorithm:
    def __init__(
        self,
        solutions: Solutions,
        selection: Selection,
        mutation: Mutatation,
        crossover: BaseCrossover,
        generations: int,
    ):
        self.solutions = solutions
        self.mutation = mutation
        self.selection = selection
        self.crossover = crossover
        self.generations = generations

    def execute(self):
        logging.warning("Running genetic algorithm")
        for _ in tqdm(range(self.generations)):
            # ipdb.set_trace()
            new_population = self.selection.select(
                self.solutions.solution_array, self.solutions.total_length
            )

            ipdb.set_trace()


            crossover_population = self.crossover.execute(new_population)  # TODO: change!
            # ipdb.set_trace()

            mutated_population = self.mutation.mutate(crossover_population)
            # ipdb.set_trace()

            self.solutions.solution_array = mutated_population
            self.solutions.evaluate()

        ipdb.set_trace()
