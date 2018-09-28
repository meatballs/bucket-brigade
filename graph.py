from pathlib import Path

import networkx as nx
import yaml

with Path("bucket-graph.yaml").open("r") as file:
    definition = yaml.load(file)
graph = nx.node_link_graph(definition)
