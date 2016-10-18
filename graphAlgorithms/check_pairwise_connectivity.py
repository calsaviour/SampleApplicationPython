##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked, paths):
    marked[node] = True
    paths.append(node)
    for neighbor in G[node]:
        if neighbor not in marked:
            mark_component(G, neighbor, marked, paths)
    return paths


def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    paths = []
    marked = {}
    mark_component(G, v1, marked, paths)

    if v2 in paths:
        return True

    return False


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'),
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
