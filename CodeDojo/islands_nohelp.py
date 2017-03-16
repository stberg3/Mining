# islands_nohelp.py
from math import ceil

plot = ["xxx.x.",
        "x.xxx.",
        "..xx.x"]

def findNeighbors(row,col,area):
    # print("Finding neighbors for", (row,col))
    neighbors = []
    if row > 0 and area[row-1][col] == "x":
        # print("\t",(row-1,col))
        neighbors.append((row-1,col))
    if row+1 < len(area) and area[row+1][col] == "x":
        # print("\t",(row+1,col))
        neighbors.append((row+1,col))
    if col > 0 and area[row][col-1] == "x":
        # print("\t",(row,col-1))
        neighbors.append((row,col-1))
    if col+1 < len(area[0]) and area[row][col+1] == "x":
        # print("\t",(row,col+1))
        neighbors.append((row,col+1))

    return neighbors

graph = dict()

for i in range(len(plot)):
    for j in range(len(plot[0])):
        if plot[i][j] == "x":
            graph[(i,j)] = findNeighbors(i,j, plot)

def connectedComponents(grph, debug=False):
    findSet = dict()
    components = dict()
    # make disjoint sets
    for v in graph.keys():
        findSet[v] = v
        components[v] = set([v])

    for u in graph.keys(): # iterate over each vertex IN THE GRAPH
        for v in graph[u]: # iterate over vertex's neighbors IN THE GRAPH
            if findSet[u] != findSet[v]:
                # combine the sets
                components[findSet[v]] = components[findSet[v]].union(components[findSet[u]])
                oldKey = findSet[u]
                for vert in components[oldKey]:
                    findSet[vert] = findSet[v]

                del(components[oldKey])

                if debug:
                    print("Unioned:", findSet[u] ," & ", findSet[v])
                    print("Setting findSet[{0}] ({1})= findSet[{2}] ({3})".format(
                        v,findSet[v],u,findSet[u]))
                    for s in components.items():
                        print("\t", s[0],": ", s[1])
                    cols = 3
                    for i in range(ceil(len(findSet.keys())/cols)):
                        for j in range(cols):
                            if i*cols+j < len(findSet.keys()):
                                item = list(findSet.items())[i*cols+j]
                                print("findSet[",item[0],"]:", item[1],end=" ::")
                        print()
                    print()

    return list(components.values())

print(max(map(len, list(connectedComponents(graph, debug=False)))))
