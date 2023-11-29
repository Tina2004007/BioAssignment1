db_path = "rosalind_sset.txt"

n = int(open(db_path, 'r').readline())

print(2**n % 1000000)