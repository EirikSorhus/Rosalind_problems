def odd_line_file(file_path): # A function to read a file and then return the even numbered rows (every second row)
  file = open(file_path, "r")
  lines = file.readlines()
  for i in range(0, len(lines), 2):
    lines[i].strip()
    print(lines[i])



if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description="funtion to read a file and return the even numbered rows")

  parser.add_argument("file_path", type=str, help = "pathfile to document")

  args = parser.parse_args()

  print(odd_line_file(args.file_path)) 