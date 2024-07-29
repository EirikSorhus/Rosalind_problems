
# take two strings as input and return the number of diviences


def hamming_distance(string1, string2):
    if len(string1) != len(string2):
        print("Warning: The strings are not the same length")
        return None
    
    divience = 0

    for i, char1 in enumerate(string1):
        if char1 != string2[i]:
            divience += 1

    return divience

print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))