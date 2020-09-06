"""
Name: Christopher Ayre

Data - 620
HomeWork 1 - "Hello, Graph World"
"""


import matplotlib.pyplot as plt
import networkx as nx


# Non-Directional Graph

# Define empty graph
G = nx.Graph()

# Add Edges and Create 
G.add_edges_from([(0, 1), (0, 2), (0, 3), (2, 3), (3, 1)])
 

# Initializing new inferace for matplotlib to plot
plt.figure()
 
# show graph
nx.drawnetworkx(G)






# Directional Graph
# (order you enter edge number dictates direction)

"""
G1 = nx.DiGraph()
G1.add_edge(1, 2)
G1.add_edge(1, 3)
nx.draw_networkx(G1)
"""
