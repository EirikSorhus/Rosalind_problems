import numpy as np

#Read fasta function
def read_FASTA(filepath):
    FASTA_seq = []

    with open(filepath, "r") as f:
        file = [l.strip() for l in f.readlines()]
    
    for line in file:
        if '>' in line:
            None
        else:
            FASTA_seq.append(line)
    return FASTA_seq #returns a list with the sequences from the fasta file


def consensus_profile(fasta_file_path):
    FASTA_seq = read_FASTA(fasta_file_path)
    it = iter(FASTA_seq)
    the_len = len(next(it))
    if not all(len(l) == the_len for l in it): # all stops when something is not True
        raise ValueError('not all sequences have same length!')
    profile_matrix = np.zeros((4, len(FASTA_seq[0])), dtype=int) 

    """A = []
    C = []
    G = []
    T = []"""
    for i in range(len(FASTA_seq)): #loop to go through all elements in seq in all seqs to count the number of nuclotides at each position
        for j in range(len(FASTA_seq[0])):
            if FASTA_seq[i][j] == "A":
                profile_matrix[0,j] += 1
            if FASTA_seq[i][j] == "C":
                profile_matrix[1,j] += 1
            if FASTA_seq[i][j] == "G":
                profile_matrix[2,j] += 1
            if FASTA_seq[i][j] == "T":
                profile_matrix[3,j] += 1
    
    nucleotides_dict = {0:"A", 1:"C", 2:"G", 3:"T"}
    biggest_nucleotide_index = np.argmax(profile_matrix, axis=0)
    consensus = [nucleotides_dict[e] for e in biggest_nucleotide_index]
    consensus_string = "".join(consensus)

    return f"{profile_matrix} \n{consensus_string}" 
#profile matrix should maybe not be returned as an array, but I dont know how to make it look good

print(consensus_profile("bioinformatics_stronghold/test_consensus_and_profile.txt"))