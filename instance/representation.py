from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    city_index: int
    x: float
    y: float


@dataclass(frozen=True)
class Representation:
    nodes_array: list[Node]
