#Importing all the libraries
from flask import Flask, redirect, render_template, request
from IPython.display import SVG, display
import numpy as np
from sknetwork.path import shortest_path
from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import bipartite2undirected
from sknetwork.data import load_edge_list, load_graphml, load_netset, load_konect
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

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
    my_dict = {"New York City" : 0, "Cambridge" : 1, "Chicago" : 2, "Cleveland" : 3, "Raleigh" : 4, "Atlanta" : 5,
               "Philadelphia" : 6, "Washington D.C." : 7, "Nashville" : 8, "Saint Louis" : 9, "New Orleans" : 10, "Houston" : 11,
               "San Antonio" : 12, "Dallas" : 13, "Orlando" : 14, "Denver" : 15, "Kansas City" : 16, "San Francisco" : 17,
               "Sacramento" : 18, "Portland" : 19, "Seattle" : 20, "Salt Lake City" : 21, "Los Angeles" : 22, "San Diego" : 23, "Phoenix" : 24}

    #Starting and Ending node points
    starting = my_dict.get(input1)
    ending = my_dict.get(input2)

    #Running the network node postions in the ml to find the shortest path and saving the image as a svg
    path = shortest_path(adjacency, sources = starting, targets = ending)
    edge_labels = [(path[k], path[k + 1], 0) for k in range(len(path) - 1)]
    image = svg_digraph(adjacency, position, names, edge_labels = edge_labels, edge_width = 3, scale = 2, filename = "images/networkGraph")
    SVG(image)


    #Converting the svg to png and saving it
    images = svg2rlg("images/networkGraph.svg")
    renderPM.drawToFile(images, "static/networkGraph.png", fmt="PNG")
    return SVG(image)

