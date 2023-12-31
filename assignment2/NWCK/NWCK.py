db_path = "rosalind_nwck.txt"

# https://rosalind.info/problems/nwck/
# Distances in Trees

from Bio import Phylo
from io import StringIO

def list_2_str(x: list, sep: str = ' '):
    return sep.join([str(item) for item in x])

def load_data(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [item.replace('\n', '') for item in f.readlines()]
    tree_node_dict = {}
    for i in range(int(len(lines) / 3) + 1):
        tree_str = lines[3 * i]
        u, v = lines[3 * i + 1].split()
        tree_node_dict[tree_str] = (u, v)

    return tree_node_dict


def distance_in_tree(tree_str: str, start_node, end_node):
    # parse tree
    tree = Phylo.read(StringIO(tree_str), 'newick')
    # init branch length
    for clade in tree.find_clades():
        clade.branch_length = 1
    # distance
    return tree.distance(start_node, end_node)


data = load_data(db_path)
distances = [distance_in_tree(tree, data[tree][0], data[tree][1])for tree in data.keys()]
print(list_2_str(distances))