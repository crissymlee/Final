#Importing all the libraries
from IPython.display import SVG
import numpy as np
from sknetwork.path import shortest_path
from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import bipartite2undirected
from sknetwork.data import load_edge_list, load_graphml, load_netset, load_konect

#Loading the .graphml
def data():
    graph = load_graphml('Resources/AttMpls.graphml')

    #Pulling the adjacency, names, and latitude/longitude from the .graphml
    adjacency = graph.adjacency
    names = graph.names

    #Pulling the latitude and longitude and putting them into an array for coordinates
    lon = graph.node_attribute.Longitude
    lat = graph.node_attribute.Latitude
    position = np.stack((lon, lat), axis=1)
    return graph, adjacency, names, position

#Dictionary of all the network nodes
def dictionary():
    my_dict = {"NewYorkCity" : 0, "Cambridge" : 1, "Chicago" : 2, "Cleveland" : 3, "Raleigh" : 4, "Atlanta" : 5,
               "Philadelphia" : 6, "WashingtonDC" : 7, "Nashville" : 8, "SaintLouis" : 9, "NewOrleans" : 10, "Houston" : 11,
               "SanAntonio" : 12, "Dallas" : 13, "Orlando" : 14, "Denver" : 15, "KansasCity" : 16, "SanFrancisco" : 17,
               "Sacramento" : 18, "Portland" : 19, "Seattle" : 20, "SaltLakeCity" : 21, "LosAngeles" : 22, "SanDiego" : 23}
    return my_dict

#Collecting information on what the starting and ending destinations are
start = input("What is the start destination? ")
lowercased = start.lower()
titlecased = lowercased.title()
def remove(titlecased): 
    return titlecased.replace(" ", "") 
start = titlecased
begin = remove(start)
start = my_dict[begin]

end = input("What is the end destination? ")
lowercased = end.lower()
titlecased = lowercased.title()
def remove(titlecased): 
    return titlecased.replace(" ", "") 
end = titlecased
end1 = remove(end)
end = my_dict[end1]

#Running the network node postions in the ml to find the shortest path
path = shortest_path(adjacency, sources = start, targets = end)
edge_labels = [(path[k], path[k + 1], 0) for k in range(len(path) - 1)]
image = svg_digraph(adjacency, position, names, edge_labels=edge_labels, edge_width=3, scale = 2)
SVG(image)




