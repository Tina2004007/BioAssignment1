
def calc_fib(n, k):
    return 1 if n <= 2 else calc_fib(n-1,k)+k*calc_fib(n-2,k)



db_path = "rosalind_fib.txt"
with open(db_path, 'r') as f:
    inpt = f.readline().strip()
    n, k = inpt.split(' ')
    n, k = int(n), int(k)
    # n, k = 5, 3
    tt = calc_fib(n ,k)

    print(tt)
