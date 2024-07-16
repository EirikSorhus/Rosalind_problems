def sep_str(strng, a, b, c,d): # function which returns parts of the string, position a-b and c-d with a space in between
  str_1 = strng[a:b]
  str_2 = strng[c:d]
  return str_1 + " " + str_2

if __name__ == "__main__":
  import argparse # impors argparse only when run directly

  # making a argument parser with a description
  parser = argparse.ArgumentParser(description = "function which returns parts of the string, position a-b and c-d with a space in between.")

  # Adding arguments for the program to accept
  parser.add_argument('string', type = str, help = "string which to split")
  parser.add_argument('start1', type = int, help = "starting point of the string to return")
  parser.add_argument('end1', type = int, help = "ending pont of the first part of the string to return")
  parser.add_argument('start2', type = int, help = "starting point of second part of string to be returned")
  parser.add_argument('end2', type = int, help = "ending point of second part of string to be returned")

  # Parse the arguments to the command line
  args = parser.parse_args()

  # Calling the function with the parsed arguments
  result = sep_str(args.string, args.start1, args.end1, args.start2, args.end2)

  print(result)
