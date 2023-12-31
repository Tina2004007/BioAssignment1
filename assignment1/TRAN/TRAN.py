
db_path = "rosalind_tran.txt"

from Bio import SeqIO

transition = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]

seq_name, seq_string = [], []
with open (db_path,'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

transition_c, transversions_c = 0, 0
s1, s2 = seq_string

for i in range(len(s1)):
    if (s1[i], s2[i]) in transition:
        transition_c += 1
    if (s1[i], s2[i]) in transversions:
        transversions_c += 1
print(transition_c/transversions_c)