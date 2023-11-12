db_path = "rosalind_inod.txt"


def load_data(filepath: str):
    n = 0
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
    return n


def count_internal_nodes(n_leaves: int) -> int:
    return n_leaves - 2


n = load_data(db_path)
print(count_internal_nodes(n))