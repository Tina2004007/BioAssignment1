db_path = "rosalind_lexf.txt"

from itertools import product


with open(db_path, 'r') as f:
    s = f.readline().split()
    n = int(f.readline().strip())

    perm = ["".join(x) for x in product(s, repeat=n)]
    print(*sorted(perm), sep="\n")