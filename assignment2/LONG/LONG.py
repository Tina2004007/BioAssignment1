db_path = "rosalind_long.txt"

def load_fasta(filepath: str, is_dict: bool = False):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.strip()
    if is_dict:
        fasta_dict = {}
        for i, name in enumerate(name_list):
            fasta_dict[name] = seq_list[i]
        return fasta_dict
    else:
        return name_list, seq_list


def get_superstring(reads_list, superstring=''):
    if len(reads_list) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = reads_list.pop(0)
        return get_superstring(reads_list, superstring)

    else:
        for current_read_index in range(len(reads_list)):
            current_read = reads_list[current_read_index]
            current_read_length = len(current_read)

            for trial in range(current_read_length // 2):
                overlap_length = current_read_length - trial

                if superstring.startswith(current_read[trial:]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, current_read[:trial] + superstring)

                if superstring.endswith(current_read[:overlap_length]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, superstring + current_read[overlap_length:])



seqs = load_fasta(db_path)[1]
super_string = get_superstring(seqs)
print(f"{super_string}")