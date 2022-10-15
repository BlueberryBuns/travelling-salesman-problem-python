from loader import InstanceLoader

loader = InstanceLoader()

representation = loader.load(".\\source\\berlin11_modified.tsp")

print(representation.nodes_array)