#Importing all the libraries
from flask import Flask, redirect, render_template, request
from IPython.display import SVG, display
import numpy as np
from sknetwork.path import shortest_path
from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import bipartite2undirected
from sknetwork.data import load_edge_list, load_graphml, load_netset, load_konect
from cairosvg import svg2png

#Loading the .graphml
def graphData(input1, input2):
    graph = load_graphml('Resources/AttMpls.graphml')

    #Pulling the adjacency, names, and latitude/longitude from the .graphml
    adjacency = graph.adjacency
    names = graph.names

    #Pulling the latitude and longitude and putting them into an array for coordinates
    lon = graph.node_attribute.Longitude
    lat = graph.node_attribute.Latitude
    position = np.stack((lon, lat), axis=1)

    #Dictionary of all the network nodes
    my_dict = {"NewYorkCity" : 0, "Cambridge" : 1, "Chicago" : 2, "Cleveland" : 3, "Raleigh" : 4, "Atlanta" : 5,
               "Philadelphia" : 6, "WashingtonDC" : 7, "Nashville" : 8, "SaintLouis" : 9, "NewOrleans" : 10, "Houston" : 11,
               "SanAntonio" : 12, "Dallas" : 13, "Orlando" : 14, "Denver" : 15, "KansasCity" : 16, "SanFrancisco" : 17,
               "Sacramento" : 18, "Portland" : 19, "Seattle" : 20, "SaltLakeCity" : 21, "LosAngeles" : 22, "SanDiego" : 23}
    starting = my_dict.get(input1)
    ending = my_dict.get(input2)

    #Running the network node postions in the ml to find the shortest path
    path = shortest_path(adjacency, sources = starting, targets = ending)
    edge_labels = [(path[k], path[k + 1], 0) for k in range(len(path) - 1)]
    image = svg_digraph(adjacency, position, names, edge_labels = edge_labels, edge_width = 3, scale = 2)
    SVG(image)
    print(SVG(image))
    svg2png(bytestring = SVG(image), write_to = "network_graph.png")
    return SVG(image)


