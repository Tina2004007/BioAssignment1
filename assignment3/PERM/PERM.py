db_path = "rosalind_perm.txt"


import itertools

n = int(open(db_path, 'r').readline())
perm = list(itertools.permutations(range(1,n+1)))

print(len(perm))
for x in list(perm):
    print(str(x).strip("(").strip(")").replace(",", ""))