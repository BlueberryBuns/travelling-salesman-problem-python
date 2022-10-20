import random
import time

import numpy as np
from numba import njit

from instance.representation import MatrixRepresentation
from instance.solution import Solutions

from instance.selection import Selection
from instance.mutations import Mutate


class GeneticAlgorithm:
    def __init__(
        self, matrix_representation: MatrixRepresentation, solutions: Solutions
    ):
        self.solutions = solutions
        self.matrix_representation = matrix_representation

    def execute(self):
        current_gen = 0
        best_specimen = None
        best_cost = np.Inf

        # to w pętli

        selected_solutions = Selection.select(
            self.solutions.solution_array, self.solutions.distance_array
        )

        # population = Crossovers.crossover(selected_solutions)

        population = Mutate.mutate(population)

        # evaluation

        current_gen += 1
        return best_cost, best_specimen
