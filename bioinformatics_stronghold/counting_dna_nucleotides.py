# Code for counting number of A, T, C and G in a string
# Could use a dictionary instead of adding to local numbers
import warnings

def count_nucleotides(string):
  A = 0
  T = 0
  C = 0
  G = 0

  warning_issued = False

  for e in string:
    if e == "A":
      A += 1
    elif e == "T":
      T += 1
    elif e == "C":
      C += 1
    elif e == "G":
      G += 1
    else: 
      if not warning_issued:
        warnings.warn("Unexpected charecter/s in string, should only contain A, T, C or G")
        warning_issued = True

  return print(A, T, C, G) # remove print if function is to be used in an other function.