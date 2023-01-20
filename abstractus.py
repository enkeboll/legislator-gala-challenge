import json
from collections import defaultdict

from typing import List, Dict

import networkx as nx
# requires metis to be installed - `brew install metis` on mac
import metis

def fully_connected_graph(node_list):
    G = nx.Graph()
    G.add_nodes_from(node_list)
    n = len(node_list)
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(node_list[i], node_list[j], weight=1)
    return G

def assign_guests_to_tables(num_tables: int,
                            guest_list: List[str],
                            planner_preferences: List[Dict[str, List[str]]]) -> Dict[str, List[str]]:
    # Create a fully connected graph where each guest is a vertex and all weights are equal to 1
    G = fully_connected_graph(guest_list)

    # our final graph will be represented by edges between all nodes with a weight of 1 for no preference,
    # weights of 0 (rather, lack of an edge) for avoidances, and weights of 2 for pairs
    for preference in planner_preferences:
        guests = preference["guests"]
        if preference["preference"] == "avoid":
            G.remove_edge(guests[0], guests[1])
        elif preference["preference"] == "pair":
            # first rename the first
            G[guests[0]][guests[1]]['weight'] = 2

    # we then use METIS to calculate the paritions (tables)
    # Note: METIS is very good at optimizing complex seating arrangements, 
    # but not very good at simple ones.
    G.graph['edge_weight_attr'] = 'weight'
    _, tables = metis.part_graph(G, num_tables)

    # Create the output dictionary in the specified format
    output = defaultdict(list)
    for i, table in enumerate(tables):
        table_num = f"table_{table + 1}"
        output[table_num].append(guest_list[i])

    #write the dictionary to json file
    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)

    return dict(output)

num_tables = 3
guest_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Gina", "Harry"]
planner_preferences = [
    {"preference": "avoid", "guests": ["Bob", "Charlie"]},
    {"preference": "pair", "guests": ["David", "Eve"]},
    {"preference": "pair", "guests": ["Gina", "Harry"]},
]
print(assign_guests_to_tables(num_tables, guest_list, planner_preferences))
