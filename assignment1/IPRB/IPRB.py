db_path = "rosalind_iprb.txt"
with open(db_path, 'r') as f:
    inpt = f.readline().strip()
    k, m, n = inpt.split(' ')
    k, m, n = int(k), int(m), int(n)
    # k, m, n = 2, 2, 2
    iprb = 1 - ((m * m + 4 * n * n + 4 * m * n - 4 * n - m) / (4 * (k + m + n) * (k + m + n - 1)))
    print(iprb)