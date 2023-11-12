import re
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

db_path = "rosalind_nkew.txt"

def nodes(graph):
    s = list(graph.keys())
    e = [y["n"] for v in graph.values() for y in v]
    return set(s) | set(e)

def dij(graph, start=1):
    dist = {n: inf for n in nodes(graph)}
    dist[start] = 0
    q = []
    heappush(q, (0, start))
    processed = set()

    while q:
        u = heappop(q)[1]
        processed.add(u)
        for v in graph[u]:
            if v["n"] not in processed:
                dist[v["n"]] = min(dist[u] + v["w"], dist[v["n"]])
                heappush(q, (dist[v["n"]], v["n"]))

    return dist



def parse_newick(newick, directed=True):
    newick = re.sub(",,", ",.,", newick)
    newick = re.sub(r"\(,", "(.,", newick)
    newick = re.sub(r",\)", ",.)", newick)
    newick = re.sub(r"\(\)", "(.)", newick)
    newick = re.sub(r"^\((.+)\);", r"\1", newick)
    m = re.finditer(r"(\(|([A-z_.]*:\d+)|,|\))", newick)
    tokens = [x.groups()[0] for x in m]

    count = 0
    node_stack = ["0"]
    g = defaultdict(list)
    i = len(tokens) - 1
    while i >= 0:
        if tokens[i] == "(":
            node_stack = node_stack[:-1]
        elif tokens[i] == ")":
            if i + 1 < len(tokens) and tokens[i + 1] not in ",)":
                if tokens[i + 1][0] == ":":
                    weight = tokens[i + 1][1:]
                    count += 1
                    node = str(count)
                else:
                    node, weight = tokens[i + 1].split(":")
            g[node_stack[-1]].append({"n": node, "w": int(weight)})
            if not directed:
                g[node].append({"n": node_stack[-1], "w": int(weight)})
            node_stack += [node]
        elif tokens[i] != "," and (i == 0 or tokens[i - 1] != ")"):
            if tokens[i] == ".":
                count += 1
                tokens[i] = str(count)
            node, weight = tokens[i].split(":")
            g[node_stack[-1]].append({"n": node, "w": int(weight)})
            if not directed:
                g[node].append({"n": node_stack[-1], "w": int(weight)})
        i -= 1
    return g


def newick_dist(tree, nodes):
    return dij(parse_newick(tree, directed=False), nodes[0])[nodes[1]]



contents = open(db_path).read().split("\n\n")
if contents[-1] == "":
    contents = contents[:-1]
trees = [x.split("\n") for x in contents]
print(*[newick_dist(tree[0], tree[1].split()) for tree in trees])