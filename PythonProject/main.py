"""
Traversal in Non-Linear Data Structures
Author: Cabalan

Nodes are labeled with the letters of the last name C-A-B-A-L-A-N
(replacing A-B-C-D-E-F-G). Letters repeat, so each node also has a
number (1-7) to tell the same letters apart.

    old label : A  B  C  D  E  F  G
    node no.  : 1  2  3  4  5  6  7
    new label : C  A  B  A  L  A  N
"""

from collections import deque

NAME = "CABALAN"


def label(node):
    """Text shown for a node, e.g. node 4 -> 'A(4)'."""
    return f"{NAME[node - 1]}({node})"


def letters(order):
    return " - ".join(NAME[n - 1] for n in order)


def with_numbers(order):
    return " - ".join(label(n) for n in order)


def add_edge(adj, a, b):
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)


# ---------- BFS: uses a queue ----------
def bfs(adj, start):
    order = []
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in adj[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return order


# ---------- DFS: uses recursion (the call stack) ----------
def dfs(adj, node, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)
    for nxt in adj[node]:
        if nxt not in visited:
            dfs(adj, nxt, visited, order)
    return order


def report(title, adj):
    b = bfs(adj, 1)
    d = dfs(adj, 1)
    print(f"=== {title} ===")
    print(f"BFS: {letters(b)}     [{with_numbers(b)}]")
    print(f"DFS: {letters(d)}     [{with_numbers(d)}]")
    print()


def main():
    # ===== Diagram 1: Tree (C is the root) =====
    tree = {}
    add_edge(tree, 1, 2)   # C - A
    add_edge(tree, 1, 3)   # C - B
    add_edge(tree, 2, 4)   # A - A
    add_edge(tree, 2, 5)   # A - L
    add_edge(tree, 3, 6)   # B - A
    add_edge(tree, 3, 7)   # B - N
    report("Diagram 1: Tree", tree)

    # ===== Diagram 2: Graph =====
    # Neighbor order affects the visiting order, so edges are added
    # in the order that follows the diagram's arrows.
    graph = {}
    add_edge(graph, 1, 2)  # C - A
    add_edge(graph, 1, 5)  # C - L
    add_edge(graph, 1, 3)  # C - B
    add_edge(graph, 2, 4)  # A - A
    add_edge(graph, 2, 5)  # A - L
    add_edge(graph, 3, 5)  # B - L
    add_edge(graph, 3, 6)  # B - A
    add_edge(graph, 4, 7)  # A - N
    add_edge(graph, 5, 7)  # L - N
    report("Diagram 2: Graph", graph)


if __name__ == "__main__":
    main()