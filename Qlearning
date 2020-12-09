import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import pandas as pd
from networkx.generators.random_graphs import random_regular_graph

Graph = nx.Graph()
d = 2
n = 20
g = random_regular_graph(d,n,seed=None)
edgeList = list(g.edges)
res = list(map(list, edgeList))

start = 1
goal = 4





transitionList = []
for element in res:
		node1 = element[0]
		node2 = element[1]
		weight = round(random.uniform(0,-50.0),4)
		transition = [node1,node2,weight]
		transitionList.append(transition)
		Graph.add_edge(node1,node2, weight = weight)
print(transitionList)

pos = nx.spring_layout(Graph)
nx.draw_networkx_nodes(Graph,pos)
nx.draw_networkx_edges(Graph,pos)
nx.draw_networkx_labels(Graph,pos)
labels = nx.get_edge_attributes(Graph,'weight')
nx.draw_networkx_edge_labels(Graph,pos,edge_labels=labels)
#######################################
rewardMat = np.matrix(np.zeros(shape=(n,n)))
goalEdges = Graph.edges(goal)
print(goalEdges)
for edge in goalEdges:
	n1 = edge[0]
	n0 = edge[1]
	rewardMat[n0,n1]=100
rewardDF = pd.DataFrame(rewardMat)
print(rewardDF)
#######################################
Qmat = np.matrix(np.full((n,n),-100))
for node in transitionList:
	Qmat[node[0],node[1]]=node[2]
	Qmat[node[1],node[0]]=node[2]
		
QmatDF = pd.DataFrame(Qmat)	
print(QmatDF)
#######################################
def next_number(start,er):
	random_value = random.uniform(0,1)
	if random_value<er:
		sample=Graph[start]
	else:
		sample=np.where(Qmat[start,] == np.max(Qmat[start,]))[1]
	next_node = int(np.random.choice(sample,1))
	return next_node


def updateQ(node1,node2,lr,discount):
	max_index = np.where(Qmat[node2,]==np.max(Qmat[node2,]))[1]
	if max_index.shape[0] > 1:
		max_index = int(np.random.choice(max_index, size = 1))
	else:
		max_index = int(max_index)
	max_value = Qmat[node2,max_index]
	Qmat[node1,node2] = int((1-lr)*Qmat[node1,node2]+lr*(rewardMat[node1,node2]+discount*max_value))

def learn(er,lr,discount):
	for i in range(5000):
		if i%100 == 0:
			print(i)
		start = np.random.randint(0,n-1)
		next_node=next_number(start,er)
		updateQ(start,next_node,lr,discount)
learn(.5,.8,.8)

def shortest_path(begin,end):
	path=[begin]
	next_node=np.argmax(Qmat[begin,])
	path.append(next_node)
	while next_node != end:
		next_node = np.argmax(Qmat[next_node])
		path.append(next_node)
	return path

print(shortest_path(start,goal))
plt.show()
