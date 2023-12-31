from Bio import SeqIO
import numpy as np


np.set_printoptions(threshold=np.inf)

seq_name, seq_string = [], []


db_path = "rosalind_cons.txt"

with open (db_path,'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

seq_len = len(seq_string)
str_len = len(seq_string[0])

symbol = ["A", "C", "G", "T"]
consensus_string = ""
profile_matrix = np.zeros(shape=(4, str_len), dtype=int)

for c in range(str_len):
    position_symbol = [s[c] for s in seq_string]
    most_common_symbol = max(position_symbol, key=position_symbol.count)
    consensus_string += most_common_symbol
    for r in range(len(symbol)):
        profile_matrix[r][c] = position_symbol.count(symbol[r])
    
print(consensus_string)
for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join([str(j) for j in profile_matrix[i]])))