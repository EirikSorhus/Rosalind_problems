
def gc_contetnt(seq):
    gc = round((seq.count("G") + seq.count("C")) / len(seq) * 100, 6)
    return gc


def FASTA_GC(filepath):
    FASTA_dict = {}
    FASTA_label = ""


    with open(filepath, "r") as f:
        file = [l.strip() for l in f.readlines()]
    
    for line in file:
        if '>' in line:
            FASTA_label = line
            FASTA_dict[FASTA_label] = ""
        else:
            FASTA_dict[FASTA_label] += line
    
    result = {key: gc_contetnt(value) for (key, value) in FASTA_dict.items()}
    max_key = max(result, key = result.get)
    print(f'{max_key}\n{result[max_key]}')

FASTA_GC("bioinformatics_stronghold/test_gc_content.txt")