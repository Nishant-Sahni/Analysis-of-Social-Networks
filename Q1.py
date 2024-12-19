import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random
#importing all required libraries

G=nx.DiGraph()
Df=pd.read_csv(r'E:\Python Programs\Project 2\ImpressionNetwork.csv')
Df=Df.drop(columns=Df.columns[0])
Df['Email Address']=Df['Email Address'].str[0:11]
for column in Df.columns[1:]:
    Df[column] = Df[column].apply(lambda x: x[-11:].lower() if pd.notnull(x) else x)
Df.rename(columns={'Email Address':'Node'},inplace=True)
#Created a dataframe comprising only entry numbers to identify nodes

for node in Df.iloc[:, 0]:
    if pd.notnull(node):
        G.add_node(node)
#added all possible nodes to graoh

# Add edges from each node to non-empty cells in the same row
for index, row in Df.iterrows():
    node = row.iloc[0]
    for col_index, cell in enumerate(row):
        if pd.notnull(cell) and col_index != 0:
            G.add_edge(node, cell)
#Our directed graph is now made 
pos = nx.kamada_kawai_layout(G)  # Force-directed layout
nx.draw(G, pos, with_labels=True, font_size=5,node_size=20, edge_color='gray', alpha=0.5)
#plt.show()
#-----------------------------------------------------------------------
#Q1 - RANDOM WALK
#Creating a dictionary to keep track of number of coins for each node
node_dict={node:0 for node in G.nodes}
#starting from a random node
start=random.choice(list(G.nodes()))
node_dict[start]+=1
next=start
#performing the walk for 1 million steps
for a in range(1000000):
    if(len(list(G.successors(start)))!=0):
        next=random.choice(list(G.successors(start)))
    else:        
        #if no outgoing edges , teleport to a random node
        next=random.choice(list(G.nodes()))
    node_dict[next]+=1
    start=next
L1=list(node_dict.values())
L2=sorted(L1,reverse=True)
L3=list(node_dict.keys())
for a in range(10):
    ind=L1.index(L2[a])
    print(a+1,'. ',L3[ind])
#This will return the top 5 leaders of our impression network
#-------------------------------------------------------------
