# Code for counting number of A, T, C and G in a string
import warnings

def count_nucleotides(string):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    warning_issued = False
    
    # Count occurrences of each nucleotide
    for e in string:
        if e in counts:
            counts[e] += 1
        else:
            if not warning_issued:
                warnings.warn("Unexpected character(s) in string, should only contain A, T, C and G")
                warning_issued = True
    
    A_count = counts['A']
    C_count = counts['C']
    G_count = counts['G']
    T_count = counts['T']
    
    # Return the counts as a formatted string
    return f"{A_count} {C_count} {G_count} {T_count}"

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description= "Function to count the number of times A, C, G, T occur, and returns the occurances in order of A, C, G and T")
    parser.add_argument("string", type = str, help = "string containing the nucleotides A, C, G, T")
    args = parser.parse_args()

    print(count_nucleotides(args.string))