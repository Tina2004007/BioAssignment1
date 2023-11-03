
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

db_path = "rosalind_revc.txt"
with open(db_path, 'r') as f:
    inpt = f.readline().strip()
    rvrsinpt = inpt[::-1]

    for i in range(len(rvrsinpt) - 1):
        if rvrsinpt[i] == 'A':
            rvrsinpt = replace_str_index(rvrsinpt, i, 'T')
        elif rvrsinpt[i] == 'T':
            rvrsinpt = replace_str_index(rvrsinpt, i, 'A')
        elif rvrsinpt[i] == 'G':
            rvrsinpt = replace_str_index(rvrsinpt, i, 'C')
        elif rvrsinpt[i] == 'C':
            rvrsinpt = replace_str_index(rvrsinpt, i, 'G')


    print(rvrsinpt)