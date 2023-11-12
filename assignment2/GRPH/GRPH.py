db_path = "rosalind_grph.txt"

def load_fasta(filepath: str, is_dict: bool = False):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.strip()
    if is_dict:
        fasta_dict = {}
        # name_list, seq_list = load_fasta(filepath)
        for i, name in enumerate(name_list):
            fasta_dict[name] = seq_list[i]
        return fasta_dict
    else:
        return name_list, seq_list


import itertools


def is_overlap(s1: str, s2: str, k: int):
    return s1[-k:] == s2[:k]


def overlap_graph_edges(data: dict, overlap_k: int):
    edges = []
    for s1_name, s2_name in itertools.combinations(data, 2):
        s1, s2 = data[s1_name], data[s2_name]
        if is_overlap(s1, s2, overlap_k):
            edges.append((s1_name, s2_name))
        if is_overlap(s2, s1, overlap_k):
            edges.append((s2_name, s1_name))
    return edges

fasta_dict = load_fasta(db_path, is_dict=True)
edges = overlap_graph_edges(fasta_dict, 3)

for u, v in edges:
    print(f"{u} {v}")

# with open(db_path, "r") as file:
#     data = file.readlines()

# headers = []
# DNA = []
# result = []
# temp = ""

# for line in data:
#     if line[0] != '>':
#         temp += line.rstrip()
#     else:
#         headers.append(line.rstrip())
#         DNA.append(temp)
#         temp = ""

# DNA.append(temp)
# DNA.pop(0)

# for i in range(len(DNA)):
#     for j in range(len(DNA)):
#         if DNA[i] == DNA[j]:
#             continue
#         elif DNA[i][-3:] == DNA[j][:3]:
#             result.append(headers[i][1:] + " " + headers[j][1:])


# for item in result:
#     print(item)

