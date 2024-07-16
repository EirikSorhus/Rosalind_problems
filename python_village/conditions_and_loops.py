def sum_int(a,b): # Function to add all integres between and included a and b
  sum = 0
  while a <= b:
    sum += a
    a += 1
  return sum

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description = "Adds all integers between and included given two numbers")
  
  parser.add_argument("start", type = int, help = "The number you want to start to sum from")
  parser.add_argument("end", type = int, help = "The last number  to sum")

  args = parser.parse_args()

  print(sum_int(args.start, args.end))
