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
#Code to represent a graph as adjacency matrix

def graph_to_adjacency_matrix(graph):
    # Extract node names and create mapping between node names and indices
    node_names = list(graph.nodes())
    node_index_map = {node_names[i]: i for i in range(len(node_names))}
    
    # Initialize adjacency matrix
    adjacency_matrix = np.zeros((len(node_names), len(node_names)), dtype=int)
    
    # Fill in the adjacency matrix
    for edge in graph.edges():
        adjacency_matrix[node_index_map[edge[0]]][node_index_map[edge[1]]] = 1
    
    return adjacency_matrix, node_names

# Example directed graph using NetworkX


# Convert the directed graph to an adjacency matrix
adjacency_matrix, node_names = graph_to_adjacency_matrix(G)

# Print the adjacency matrix with row and column headings
'''print("Adjacency Matrix:")
print("\t", "\t".join(node_names))
for i in range(len(node_names)):
    print(node_names[i], "\t", "\t".join(str(x) for x in adjacency_matrix[i]))
'''
#----------------------------------------------------
#Missing Links 

from sklearn.linear_model import LinearRegression as LR
model=LR() #creating linear regression model

X=adjacency_matrix  #defined above

coeff=[]
for i in range(len(X)):
    tar=X[i] #ith row
    Others=X.copy()
    Others=np.delete(Others,(i),axis=0) # storing all others except ith row
    Others=Others.T
    model.fit(Others,tar)
    coeff.append(model.coef_)
coeff=np.array(coeff)
#for i in range(len(coeff)):
#    print(np.all(coeff[i]==0))
def linearcomb(i,j):
    targetcol=np.array(X)[:,j]
    targetcol=np.delete(targetcol,i)
    #print(coeff)
    if(np.all(coeff[i]==0)):
        #if all entries in a row are zero , then model.fit will return all coefficients corresponding to it to be zero
        #so , if we don't make a special case for this , and just find the linear combination score , then we will not be able to predict whether this is a missing link or not
        #so we need to assign some sort of score , so that we can identify whether this edge is worthy of being a missing link or not
        #one measure of popularity is the PageRank score
        score_jth=nx.pagerank(G)[str(list(G.nodes)[j])] #pagerank score of the jth node
        #set a threshold on this score , if its above some value , then we will reccomend it as a missing link
        averagescore=sum(list(nx.pagerank(G).values()))/len(nx.pagerank(G).values())
        if score_jth>=averagescore:
            return np.random.choice([1,1,1,-1])  #will be recommended as a missing link with 3/4 probability
        else:
            return np.random.choice([-1,-1,-1,1]) #will be recommended as a missing link with 1/4 probability
    else:
        return np.dot(coeff[i],targetcol)
def identifylinks(i,j):
    MissingLink=()
    predictionscore=linearcomb(i,j) #this will either be dependent on the pagerank score or the dot product of np.dot
    if predictionscore>=0.5: #after testing the code numerous , I found this threshold/tolerance to be most appropriate
        MissingLink=(list(G.nodes)[i],list(G.nodes)[j])
        return MissingLink 
    return None 

def recommend():
    MissingLinks=[]
    for i in range(0,len(G.nodes())):
        for j in range(0,len(G.nodes())):
            if(i!=j and (not G.has_edge(i,j)) and identifylinks(i,j)!=None): #also checking if the edge was missing to begin with
                #print(list(G.nodes)[i],'-',list(G.nodes)[j])
                MissingLinks.append(identifylinks(i,j))
    return MissingLinks
print('There are ',len(recommend()),'number of missing links (edges) after using the specified tolerance')
#print(recommend()) #prints all the edges that are missing