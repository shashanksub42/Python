from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))

    return edges

my_graph = defaultdict(list)
add_edge(my_graph, 'a', 'b')
add_edge(my_graph, 'b', 'c')
add_edge(my_graph, 'c', 'd')
add_edge(my_graph, 'd', 'f')
add_edge(my_graph, 'c', 'g')
add_edge(my_graph, 'f', 'a')


def findPath(graph, start, end, path = []):
    #Add start node to path
    path = path + [start]

    #Check if end node is found
    if start == end:
        #If so, then return path
        return path

    #Otherwise, iterate over the neighboring nodes
    for node in graph[start]:
        if node not in path:
            #Recursive call to findPath to find the next neighboring node
            newpath = findPath(graph, node, end, path)
            if newpath:
                return newpath
            return None

#Same logic as previous function, except that
#We keep appending every path to the paths list
#Then return the paths list at the end
def findAllPaths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths

#Similar logic to previous two functions
#Create a shortest variable which is initialized to None
#Keep comparing path length to shortest variable
def findShortestPath(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if shortest is None:
                    shortest = newpath
                elif not shortest and len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

print("findPath:")
print(findPath(my_graph, 'c', 'b'))
print("findAllPaths:")
print(findAllPaths(my_graph, 'c', 'b'))
print("findShortestPath:")
print(findShortestPath(my_graph, 'c', 'b'))
