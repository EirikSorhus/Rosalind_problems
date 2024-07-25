# Function for counting the occurrences of each word in the string, where words are separated by spaces.
def word_count(string):
  counts = dict()
  punctuation = '.,!?;:' # The signs that will be removed from the words
  words = string.split() # Splits the scentence by space and ads the words to a list
  cleaned_words = [word.rstrip(punctuation) for word in words] # This should get rid off punctuations from the words

  for word in cleaned_words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  return counts

print(word_count("AA A T, T T CCC GG GG."))
print(word_count("AA A T, T T CCC GG GG."))

