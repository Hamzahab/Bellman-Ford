# Name: Hamzah Abdullahi
# Description: This program implements the Bellman-Ford
# Shortes Path Graph Algorithm, as well as Graph Potentials



# This function updates the dist, meaning if
# a certain vertex was unreachable and had a value
# of infinity, pop it from the dist dictionary
def update_dist(dist, infinity, case):
    '''
    This function updates the dist, meaning if
    a certain vertex was unreachable and had a value
    of infinity, pop it from the dist dictionary

    dist: same dist from bellman_ford
    infinity: infinite value
    case: specifies whether running bellman_ford or find_potential
    '''
    new_dist = {}
    for k, v in dist.items():
        if v != infinity:
            if case == 0:
                new_dist[k] = v
            else:
                new_dist[k] = -v

    return new_dist


def bellman_ford(vertices, edges, start):

    '''
    Computes shortest paths to every reachable vertex from the vertex "start"
    in the given directed graph.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
    example - {('A', 'B'): -3} means the edge from vertex
    'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    Assumes the graph does not have negative cost cycles,
    that all edges have endpoints in "vertices", and that
    "start" is also in "vertices".

    returns dist, reached

    Here reached is the search tree to all reachable vertices along
    minimum-cost paths and dist[v] is the cost to v along
    this path. If v is not reachable, it should not be in the
    search tree nor an index in dist.

    >>> vertices = {1, 2, 3, 4, 5, 6}
    >>> edges = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
    >>> dist, reached = bellman_ford(vertices, edges, 1)
    >>> dist == {1: 0, 2: 5, 3: 4, 4: 2, 5: -2}
    True
    >>> reached == {1: 1, 2: 1, 3: 5, 4: 5, 5: 2}
    True
    >>> dist[3] == 4
    True
    >>> reached[2] == 1
    True
    '''
    infinity = float('inf')
    dist = {}
    reached = {}

    # trivial solution
    reached[start] = start

    for vert in vertices:
        # set the start vertex as 0 (no distance)
        if vert == start:
            dist[vert] = 0
        else:
            dist[vert] = infinity

    for i in range(len(vertices)-1):
        for key in edges.keys():
            if dist[key[1]] > (dist[key[0]] + edges[key]):
                dist[key[1]] = dist[key[0]] + edges[key]
                reached[key[1]] = key[0]

    new_dist = update_dist(dist, infinity, 0)
    return new_dist, reached


def find_potential(vertices, edges):
    '''
    Finds a potential for the gbelraph or determines the graph has
    a negative-cost cycle.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
    example - {('A', 'B'): -3}Uploading, please wait... means the edge from vertex
    'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    If the graph has a negative-cost cycle, this simply returns None.
    Otherwise, it returns a dictionary mapping each vertex to its value
    in a potential function.
    >>> vertices = {1, 2, 3, 4, 5, 6}
    >>> edges = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
    >>> find_potential(vertices, edges) == {1: 8, 2: 3, 3: 4, 4: 6, 5: 10, 6: 0}
    True
    >>> find_potential(vertices, edges)[2] == 3
    True
    '''

    infinity = float('inf')
    dist = {}

    for vert in vertices:
        dist[vert] = 0

    for i in range(len(vertices)-1):
        for key in edges.keys():
            if dist[key[1]] > (dist[key[0]] + edges[key]):
                dist[key[1]] = dist[key[0]] + edges[key]

    new_dist = update_dist(dist, infinity, 1)
    return new_dist
