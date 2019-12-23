import string

with open('inputs/big-convert.txt', 'w') as w:
    with open('inputs/bible.txt', 'r') as f:
        for line in f:
            for word in line.split():
                stripped_word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                w.write(stripped_word + "\n")

