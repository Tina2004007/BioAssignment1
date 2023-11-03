
db_path = "rosalind_dna.txt"
with open(db_path, 'r') as f:
    inpt = f.readline().strip()
    cA = inpt.count('A')
    cC = inpt.count('C')
    cG = inpt.count('G')
    cT = inpt.count('T')

    print(cA, cC, cG, cT)