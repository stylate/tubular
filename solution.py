#!/usr/bin/python3
# Alan Nguyen - Tubular Labs Coding Challenge
import sys

def find_compounds(word, components):
    """
    For a select word WORD, determine if it is a composite word
    (i.e. it is composed of 2 or more words in set S).

    Parameters:
        word (string): input word
        components (set): set of component words
    """
    if not word:
        return True # base case
    for i in range(1, len(word) + 1):
        prefix = word[:i] # component 1
        suffix = word[i:] # components 2, ... n
        # perform recursion on the SUFFIX.
        if prefix in components and find_compounds(suffix, components):
            return True
    if word not in components:
        components.add(word)
    return False

def process_list(inputs):
    """
    Process through a list of inputs and return compound words.

    Parameters:
        inputs (set): set of unique input words
    """
    components = set()
    output = set()
    # sort our inputs since compound words are typically longer than component words
    sorted_words = sorted(inputs, key=lambda s: len(s))
    for word in sorted_words:
        if find_compounds(word, components): output.add(word)
    output = sorted(output) # outout expected to be sorted
    return output

if __name__ == '__main__':
    words = set()
    # clean stdin before processing algorithm
    for line in sys.stdin:
        w = line.strip() # strips newline and whitespace
        if len(w) > 0 and w not in words: # no empty strings
            words.add(w)
    compounds = process_list(words)

    # print results to stdout
    for c in compounds:
        print(c)
