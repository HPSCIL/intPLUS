import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
# Build data
plt.rc('font', family='Times New Roman')
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
df = pd.read_csv("Analyze_Contribution_value1.csv",sep = ',')
label=pd.DataFrame(df["Factor"])

category=7
showThreshold=0.03

for i in range(category):
    path="Analyze_Contribution_value"+str(i+1)+".csv"
    df = pd.read_csv(path,sep = ',')
    data=pd.DataFrame(df["Contribution"])
    data.rename(columns={'Contribution': "land_use"+str(i+1)+"_growth"}, inplace=True)
    label = pd.concat([label, data], axis=1)
print(label.values)


# left, right, bottom, top, layer_sizes = .1, .9, .1, .9, [4, 7, 7, 2]
left, right, bottom, top, layer_sizes = .1, .9, .1, .9, [category,category,category+1]
# The distance between the network and up, down, left, and right.
# Users can adjust the layter_sizes by themselves.
G = nx.DiGraph()
v_spacing = (top - bottom)/float(max(layer_sizes))
h_spacing = (right - left)/float(len(layer_sizes) - 1)

node_count = 0
for i, v in enumerate(layer_sizes):
    layer_top = v_spacing*(v-1)/2. + (top + bottom)/2.
    for j in range(v):
        if(node_count<category):
            G.add_node(node_count, pos=(left + i*h_spacing, layer_top - j*v_spacing),desc=label["Factor"][node_count])
        elif(node_count>=category and node_count<category*2):
            G.add_node(node_count, pos=(left + i*h_spacing, layer_top - j*v_spacing),desc=label.columns.values[node_count-len(label)+1])
        else:
            G.add_node(node_count, pos=(left + i*h_spacing, layer_top - j*v_spacing),desc=label["Factor"][node_count-category])
        node_count += 1


for x, (left_nodes, right_nodes) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
    for i in range(left_nodes):
        for j in range(right_nodes):
            if(x==0):
                if(label.values[i][j+1]!=0.5 and abs(label.values[i][j+1])>showThreshold):
                    G.add_edge(i+sum(layer_sizes[:x]), j+sum(layer_sizes[:x+1]),
                               weight=(label.values[i][j+1]), name=str(label.values[i][j+1])
                               )
            else:
                if(label.values[j+category][i+1]!=0.5 and abs(label.values[j+category][i+1])>showThreshold):
                    G.add_edge(j+sum(layer_sizes[:x+1]), i+sum(layer_sizes[:x]),
                               weight=(label.values[j+category][i+1]), name=str(label.values[j+category][i+1])
                               )

eposi = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0]
enega = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] < 0]
            

pos=nx.get_node_attributes(G, 'pos')
# Extract the position information (pos) from each node.
nx.draw(G, pos, 
        node_color=range(node_count), 
        with_labels=False,
        node_size=500, 
        # edge_color=[random.random() for i in range(len(G.edges))],
        # width=2,
        cmap=plt.cm.Dark2 # matplotlib color palette
       )

nx.draw_networkx_edges(G, pos, edgelist=eposi, width=1, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=enega, width=1, edge_color='b')

node_labels = nx.get_node_attributes(G, 'desc')
nx.draw_networkx_labels(G, pos, labels=node_labels)
edge_labels = nx.get_edge_attributes(G, 'name')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
