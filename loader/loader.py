from functools import cached_property
import numpy as np

from tqdm import tqdm
# from instance import Representation, Node
from instance.representation import Repres


class InstanceLoader:
    SPLITTER = "NODE_COORD_SECTION"

    def __init__(self, filepath: str):
        self._info_dict = {}
        with open(filepath) as f:
            self.file_body = f.read()
            self.splitted_body = self.file_body.split(self.SPLITTER)
            self.raw_nodes = self.splitted_body[1]

    def load(self) -> Repres:
        # representation = Representation(self._get_verticies(self.raw_nodes))
        representation = Repres(self._get_verticies(self.raw_nodes))
        return representation

    def _get_verticies(self, raw_nodes: str) -> np.ndarray: #list[Node]:
        nodes = []

        for line in raw_nodes.split("\n"):
            if line == "EOF":
                break
            if not line:
                continue

            splitted_line = line.split(" ")
            node = (
                int(splitted_line[0]) - 1,
                float(splitted_line[1]),
                float(splitted_line[2]),
            )
            nodes.append(node)
        return np.array(nodes, dtype=float)

    @cached_property
    def info_dict(self) -> dict:
        info_part = self.splitted_body[0].strip()
        split_parts = info_part.split("\n")
        for x in split_parts:
            values = x.split(": ")
            self._info_dict[values[0]] = values[1]
        return self._info_dict

    @property
    def dimension(self) -> int:
        return int(self.info_dict.get("DIMENSION"))
