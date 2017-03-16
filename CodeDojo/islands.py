# islands.py
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

# need to isolate subgraphs
def connectedComponents(grph, debug=False):
    findSet = dict()
    connectedSets = dict()

    for v in graph.keys():
        findSet[v] = v
        connectedSets[v] = set([v])
        
    for u in graph.keys():
        for v in graph[u]:
            if findSet[u] != findSet[v]:
                connectedSets[findSet[u]] = connectedSets[findSet[u]].union(connectedSets[findSet[v]])
                oldKey = findSet[v]

                for vert in connectedSets[findSet[v]]:
                    findSet[vert] = findSet[u]

                del(connectedSets[oldKey])

                if debug:
                    print("Unioned:", findSet[u] ," & ", findSet[v])
                    print("Setting findSet[{0}] ({1})= findSet[{2}] ({3})".format(
                        v,findSet[v],u,findSet[u]))
                    for s in connectedSets.items():
                        print("\t", s[0],": ", s[1])
                    cols = 3
                    for i in range(ceil(len(findSet.keys())/cols)):
                        for j in range(cols):
                            if i*cols+j < len(findSet.keys()):
                                item = list(findSet.items())[i*cols+j]
                                print("findSet[",item[0],"]:", item[1],end=" ::")
                        print()
                    print()

    return list(connectedSets.values())

for r in plot:
    print("\t", r)

# for i in graph.items():
#     print(i)

cc = connectedComponents(graph)
# print()
# for r in cc:
#     print(r)
print(max(map(len,cc)))
