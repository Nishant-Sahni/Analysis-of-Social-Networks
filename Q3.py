import networkx as nx
import pandas as pd
import numpy as np
#importing all required libraries

G=nx.DiGraph()
Df=pd.read_csv(r'E:\Python Programs\Project 2\ImpressionNetwork.csv')
Df=Df.drop(columns=Df.columns[0])
Df['Email Address']=Df['Email Address'].str[0:11]
for column in Df.columns[1:]:
    Df[column] = Df[column].apply(lambda x: x[-11:].lower() if pd.notnull(x) else x)
Df.rename(columns={'Email Address':'Node'},inplace=True)
#Created a dataframe comprising only entry numbers 
#Will identify nodes as entry numbers

for node in Df.iloc[:, 0]:
    if pd.notnull(node):
        G.add_node(node)
#added all possible nodes to graph

# Add edges from each node to non-empty cells in the same row
for index, row in Df.iterrows():
    node = row.iloc[0]
    for col_index, cell in enumerate(row):
        if pd.notnull(cell) and col_index != 0:
            G.add_edge(node, cell)
#Our directed graph is now made

#-------------------------------------------
#Assortativity

total=G.number_of_edges() #storing cardinality of edge-set
#print(G.has_edge(list(G.nodes)[4],list(G.nodes)[5]))
similar=0
dissimilar=0
selfedges=0
for i in list(G.nodes):
    for j in list(G.nodes):
            if (i!=j and G.has_edge(i,j)):
                if i[4:7]==j[4:7]:
                    similar+=1     #if same branch
                else:
                    dissimilar+=1    #if different branch
            if(i==j and G.has_edge(i,j)):
                selfedges+=1            #increment number of people impressed with themself
assortativity=similar/(total-selfedges) #this is the ratio of similar edges to total non-self edges
print("The percentage of edges between people of the same branch is",assortativity*100,'%')
print("")
#-----------------------------------------------
#Mutuality

double=0
container=set()  #initialized a set to keep track of the pairs of nodes already checked
for i in list(G.nodes):
    for j in list(G.nodes):
        if(i!=j and G.has_edge(i,j) and G.has_edge(j,i) and ((i,j) not in container) and ((j,i) not in container)):
            double+=1
            container.add((i,j))               
            container.add((j,i))
print("There are a total of",double,'mutual edges in the network.')
print("")
#-----------------------------------------------------
#Closeness Centrality 
store={}
for X in list(G.nodes):
    CX=0
    if (len(list(G.neighbors(X)))==0):          #if node is disconnected , disregard it
        continue
    else:
        for y in list(G.nodes):
            if y!=X:                            #to take care of shortestdistance=0 case
                if(len(list(G.neighbors(y)))==0):
                    continue                    #if node is disconnected , shortestdistance=infinity , so reciprocal =0 , so disregard it
                else:
                    CX+=1/(nx.shortest_path_length(G,source=y,target=X))
        CX=CX*(len(list(G.nodes))-1)
    store[X]=CX
sortedC=sorted(list(store.values()),reverse=True)       #storing the sorted list of closeness centralities
top10=[]
for a in sortedC[:10]:
    ind=list(store.values()).index(a)
    top10.append(list(store.keys())[ind])

print("The top 10 nodes ranked by closeness centrality are :",top10)        #printing top 10 keys by closeness centrality

#------------------------------