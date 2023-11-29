db_path = "rosalind_kmp.txt"


from Bio import SeqIO

def _get_failure_array(s):
    failure_array = [0] * len(s)
    longest_motif_length = 0
    for i in range(1, len(s)):
        print(i)
        for j in range(1, len(s)-i+1):
            if s[:i] == s[j:j+i]:
                failure_array[j+i-1] = len(s[:i])
                longest_motif_length = len(s[:i])


        
        if longest_motif_length < len(s[:i]):
            break
    print(failure_array)



with open (db_path,'r') as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        s = seq_record.seq
_get_failure_array(s)

