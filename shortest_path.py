#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install scikit-network


# In[2]:


from IPython.display import SVG


# In[3]:


import numpy as np


# In[4]:


from sknetwork.data import miserables, painters, movie_actor
from sknetwork.path import shortest_path
from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import bipartite2undirected


# In[5]:


graph = painters(metadata=True)
adjacency = graph.adjacency
names = graph.names
position = graph.position


# In[6]:


klimt = 6
vinci = 9


# In[7]:


path = shortest_path(adjacency, sources=klimt, targets=vinci)


# In[8]:


edge_labels = [(path[k], path[k + 1], 0) for k in range(len(path) - 1)]


# In[9]:


image = svg_digraph(adjacency, position, names, edge_labels=edge_labels, edge_width=2)


# In[10]:


SVG(image)


# In[11]:


print(graph)


# In[12]:


type(graph)


# In[ ]:




