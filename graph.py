# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:24:05 2021

@author: Gebruiker
"""

#%% networkx

import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import pygraphviz as pgv

jump_systems = pd.read_csv('C:/Users/Gebruiker/Desktop/eve_scripts/fountain_map.csv')

G = nx.Graph()

for index, row in jump_systems.iterrows():
    if row['Type'] == 'Jump Bridge':
        color = 'green'
        weight = 0.5
        style = '--'
    else:
        color = 'black'
        weight = 0.5
        style = 'solid'
    G.add_edge(row['From'],row['To'], color = color, weight = weight, style = style)

#elarge=[(u,v) for (u,v,d) in G.edges(data=True)]

#pos=nx.spring_layout(G, scale = 100) # positions for all nodes

# nodes
#nx.draw_networkx_nodes(G,pos,node_size=20,node_shape='s')

# edges
#nx.draw_networkx_edges(G,pos,edgelist=elarge, width=0.1)

# labels
#nx.draw_networkx_labels(G,pos,font_size=1,font_family='sans-serif')

edges = G.edges()
colors = [G[u][v]['color']
   for u, v in edges
]
weights = [G[u][v]['weight']
   for u, v in edges
]
styles = [G[u][v]['style']
   for u, v in edges
]

externals = list(jump_systems[jump_systems.external_region == 'Yes']['To'])

keepstars = list(jump_systems[jump_systems.Keepstar == 'Yes']['From'])

color_map = ['darkorange' if node in keepstars else 'gray' if node in externals else 'turquoise' for node in G]        

nx.draw_kamada_kawai(G, 
                     edge_color = colors,
                     style = styles,
                     width = weights, 
                     with_labels = True, 
                     node_size = 50, 
                     font_size = 3, 
                     node_shape = 's',  
                     node_color=color_map)

#plt.axis('off')
plt.savefig("weighted_graph.svg")
plt.show() # display
