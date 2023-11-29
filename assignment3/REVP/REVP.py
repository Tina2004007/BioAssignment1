db_path = "rosalind_revp.txt"


with open(db_path, 'r') as file:
    s = ''.join(x.strip() for x in file.readlines()[1:])
dic = {'G':'C','C':'G','A':'T','T':'A'}
for i in range(len(s)-3):
    for j in range(min(len(s), i+12), i+3, -1):
        current = s[i:j]
        revcomp = ''.join(dic[x] for x in current)[::-1]
        if current == revcomp:
            print(i+1, j-i)