# not going to make a dictionary of a codon table manualy so using Bio.Data package
from Bio.Data import CodonTable # type: ignore

def translation(rna):
    rna_codon_table = CodonTable.unambiguous_rna_by_name["Standard"]
    rna_codons = [rna[i:i+3] for i in range(0, len(rna), 3)]

    protein_list = []
    for codon in rna_codons:
        if codon in rna_codon_table.forward_table:
            protein_list.append(rna_codon_table.forward_table[codon])
        elif codon in rna_codon_table.stop_codons:
            protein_list.append("*") # * means stop
        else:
            protein_list.append("?") # symbol if it somehow is an unexpected codon
    
    protein_code = "".join(protein_list)
    return protein_code

print(translation("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
