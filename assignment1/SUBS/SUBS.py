def rep(string1, string2):
    loc = []
    for i in range(len(string1)):
        if string2 == string1[i: i+len(string2)]:
            loc.append(i+1)
    return loc

db_path = "rosalind_subs.txt"

with open(db_path, 'r') as f:
    string1 = f.readline().strip()
    string2 = f.readline().strip()
loc = rep(string1, string2)
for i in loc:
    print(i, end=" ")