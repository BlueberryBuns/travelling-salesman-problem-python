from abc import ABC, abstractmethod


class BaseTSPSolver(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError
