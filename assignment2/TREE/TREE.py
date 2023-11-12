db_path = "rosalind_tree.txt"

with open(db_path) as f:
	n = int(f.readline().strip())
	adj_list = [[] for _ in range(n+1)]
	for u, v in [map(int, line.strip().split(' ')) for line in f.readlines()]:
		adj_list[u].append(v)
		adj_list[v].append(u)

markd = [False for _ in range(n+1)]
num_components = 0
for i in range(1, n+1):
	if markd[i]:
		continue
	markd[i] = True
	num_components += 1
	open_front = [i]
	while len(open_front) > 0:
		u = open_front.pop()
		unmarked_neighbours = [v for v in adj_list[u] if not markd[v]]
		open_front += unmarked_neighbours
		for v in unmarked_neighbours:
			markd[v] = True

print(num_components - 1)
