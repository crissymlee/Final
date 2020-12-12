#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import SVG


# In[2]:


import numpy as np


# In[3]:


from sknetwork.path import shortest_path
from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import bipartite2undirected
from sknetwork.data import load_edge_list, load_graphml, load_netset, load_konect


# In[5]:


import pandas as pd
import plotly.express as px


# In[6]:


graph = load_graphml('Resources/Sprint.graphml')
adjacency = graph.adjacency
names = graph.names


arr1 = graph.node_attribute.Longitude
arr2 = graph.node_attribute.Latitude
position = np.stack((arr1, arr2), axis=1)


# In[7]:


print(graph)


# In[28]:


Seattle = 3
New_York = 7


# In[29]:


path = shortest_path(adjacency, sources=Seattle, targets=New_York)


# In[30]:


edge_labels = [(path[k], path[k + 1], 0) for k in range(len(path) - 1)]


# In[34]:


image = svg_digraph(adjacency, position, names, edge_labels=edge_labels, edge_width=3)


# In[32]:


SVG(image)


# In[14]:


print(names)


# In[13]:


print(adjacency)


# In[15]:


print(position)


# In[ ]:




