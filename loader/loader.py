from instance import Representation, Node

SPLITTER = "NODE_COORD_SECTION"

class InstanceLoader:

    def load(self, file: str) -> Representation:
        with open(file) as f:
            file_body = f.read()
            splitted_body = file_body.split(SPLITTER)
            raw_nodes = splitted_body[1]

            representation = Representation(
                nodes_array = self._get_verticies(raw_nodes)
            )

            return representation

    def _get_verticies(self, raw_nodes: str) -> list[Node]:
        nodes = []

        for line in raw_nodes.split("\n"):
            if line == "EOF":
                break
            if not line:
                continue

            splitted_line = line.split(" ")

            node = Node(
                city_index = int(splitted_line[0]),
                x = float(splitted_line[1]),
                y = float(splitted_line[2])
            )
            nodes.append(node)
            
        return nodes
