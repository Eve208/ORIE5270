from heapq import *

def find_shortest_path(text_file, source, destination):
    """
    find the shortest path between source and destination using dijkstra algorithm
    :param text_file: (text file) contains the graph
    :param source: (key) the node to start
    :param destination: (key) the node to end
    :return: ((float,list)) (cost, path) if a path exists; None if there's no path between the two nodes
    """
    graph = getGraph(text_file)
    
    frontier = [(0,source,[])]
    visited = set()
    dist = {source: 0}
    
    while frontier:  
        (cost,v1,path) = heappop(frontier)
        if v1 not in visited:
            visited.add(v1)
        if v1 == destination: 
            return(cost, path + [float(v1)])

        for items in graph[v1].keys():
            if items not in visited and items not in [i[1] for i in frontier]:
                dist[items] = cost + graph[v1][items]
                heappush(frontier, (dist[items], items, path + [float(v1)])) 
            if cost + graph[v1][items] < dist[items]:
                dist[items] = cost + graph[v1][items]
                
    if destination not in visited:
        path = None

def find_negative_cycles(text_file):
    """
    find the negative cycles in a graph using Bellman Ford Algorithm
    :param text_file: (text file) contains the graph
    :return: (list) negtive cycle if exists; None if doesn't
    """
    graph = getGraph(text_file)
    num_node = len(graph)
    
    for source in graph:
        dist = {}  
        prev = {}  
        for node in graph:
            dist[node] = float("inf")
            prev[node] = None

        dist[source] = 0

        for i in range(num_node - 1):
            for node in graph:
                for neighbour in graph[node]:
                    if dist[neighbour] > dist[node] + graph[node][neighbour]:
                        dist[neighbour] = dist[node] + graph[node][neighbour]
                        prev[neighbour] = node

        for node in graph:
            for neighbour in graph[node]:
                if dist[neighbour] > dist[node] + graph[node][neighbour]:
                    neg_cycle = [node]
                    prev_path = prev[node]
                    while node != prev_path and prev_path:
                        neg_cycle.append(prev_path)
                        prev_path = prev[prev_path]
                    neg_cycle.append(prev_path)
                    return (neg_cycle[::-1])
    return None

def getGraph(text_file):
    """
    get the graph from text file
    :param text_file: (text file) contains the graph
    :return: (dictionary) graph
    """
    graph = dict()
    file = open(text_file, "r")
    line = file.readlines()
    for l in range(len(line)):
        if l % 2 == 1:
            graph[float(line[l-1])] = getEdges(line[l])
    return graph

def getEdges(line):
    """
    get the graph from text file
    :param text_file: (text file) contains the graph
    :return: (dictionary) edges
    """
    edges = {}
    start = "("
    count = 0
    for i in line:
        if i == '(': count = count + 1
        if count == 1: start = start + i
        if i == ')':
            count = count - 1
            start = start + ')'
            tup = eval(start)
            edges[float(tup[0])] = float(tup[1])
            start = '('
    return edges



