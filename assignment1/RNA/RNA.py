db_path = "rosalind_rna.txt"
with open(db_path, 'r') as f:
    inpt = f.readline().strip()
    rna = inpt.replace('T','U')
    print(rna)