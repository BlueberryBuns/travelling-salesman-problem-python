from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    city_index: int


@dataclass(frozen=True)
class Representation:
    verticies_array: list[list[Node]]
