from pathlib import Path

import networkx as nx
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
yaml.default_flow_style = False

definition = yaml.load(Path("bucket-graph.yaml"))
graph = nx.node_link_graph(definition)
