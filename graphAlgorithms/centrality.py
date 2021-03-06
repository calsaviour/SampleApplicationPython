__author__ = 'calvinlowyanming'

import csv
import random


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: make_link(G, node1, node2)
    return G


def read_biparted_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = {}
    movies = {}

    for (actor, movie_name, year) in tsv:
        movie = str(movie_name) + ", " + str(year)
        actors[actor] = 1
        movies[movie] = 1
        make_link(G, actor, movie)
    return (G, actors, movies)


# Read the marvel comics graph
## marvelG = read_graph('uniq_edges.tsv')

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2: return distance_from_start[v2]
                open_list.append(neighbor)
    return False


# path from start (after modification on distance())
def path(G, v1, v2):
    # distance_from_start = {}
    path_from_start = {}  # modification
    open_list = [v1]
    # distance_from_start[v1] = 0
    path_from_start[v1] = [v1]  # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            # if neighbor not in distance_from_start:
            if neighbor not in path_from_start:  # modification
                # distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current]
                + [neighbor]  # modification
            # if neighbor == v2: return distance_from_start[v2]
            if neighbor == v2: return path_from_start[v2]  # modification
            open_list.append(neighbor)

    return False


from_node = "A"
to_node = "ZZZAX"

##print distance(marvelG, from_node, to_node)
##print path(marvelG, from_node, to_node)

## Lesson 19: Centrality
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values())) / len(distance_from_start)


def rank(L, v):
    r = 0
    for l in L:
        if l < v: r += 1
    return r


def find_rank(L, i):
    lt = {}
    eq = {}
    gt = {}

    v = random.choice(L.keys())

    for l in L.keys():
        if L[l] < L[v]:
            lt[l] = L[l]
        elif L[l] == L[v]:
            eq[l] = L[l]
        elif L[l] > L[v]:
            gt[l] = L[l]

    if len(lt) >= 1:
        return find_rank(lt, i)

    elif len(lt) + len(eq) >= 1:
        return v

    else:
        return find_rank(gt, i - len(lt) - len(eq))


def test():
    (G, actors, movies) = read_biparted_graph('../files/file.tsv')
    centralities = {}

    for actor in actors.keys():
        centralities[actor] = centrality(G, actor)

    actor_index = find_rank(G, 20)
    print actor_index
    print centralities[actor_index]
    ##print movieGraph


if __name__ == "__main__":
    test()
