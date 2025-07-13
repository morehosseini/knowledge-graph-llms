import networkx as nx
from pyvis.network import Network
from pathlib import Path

INPUT_DIR = Path("data/graphs")
OUTPUT_DIR = Path("docs/graphs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for graph_file in INPUT_DIR.glob("*.graphml"):
    G = nx.read_graphml(graph_file)
    net = Network(height="800px", width="100%")
    net.from_nx(G)
    output_file = OUTPUT_DIR / (graph_file.stem + ".html")
    net.save_graph(str(output_file))
    print(f"Generated: {output_file}")
