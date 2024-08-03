# an atemt to do it recursivly
# output is a list containing the start position of the motif, where 0 is the first element.
def motif_finder(string, motif, start = 0):
    motif_found = []
    if len(string) - start < len(motif):
        return motif_found
    string_found = string.find(motif, start)
    lengt_string = len(string)
    if string_found != -1:
        start = string_found + 1 # +1, otherwise it will start at the same place over and over again
        motif_found.append(string_found)
        motif_found.extend(motif_finder(string, motif, start)) #extend iterates through and adds the elements and then removes layers of lists
        return motif_found
        
    if string_found == -1:
        return motif_found

print(motif_finder("GATATATGCATATACTT", "ATAT"))