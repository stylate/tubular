import time
import sys

def findCompounds(word, s):
    '''
    For a select word WORD, determine if it is a composite word
    (i.e. it is composed of 2 or more words in set S).
    '''
    if not word: return True # base case
    for i in range(1, len(word) + 1):
        prefix = word[:i] # component 1
        suffix = word[i:] # components 2, ... n
        # perform recursion on the SUFFIX.
        if prefix in s and findCompounds(suffix, s):
            return True
    if word not in s: # potentially problematic as suffix gets added to set 
        s.add(word)
    return False

def processList(words):
    '''
    Process through a list of inputs and return compound words.
    Time: O(min(nlogn, nk^2)) for k = word length
    Space: O(2n) => O(n) {both set and output can contain at most n words}.
    '''
    t = time.process_time()
    s = set()
    # compile a sorted list of words?
    output = set()
    for w in sorted(words, key=lambda s: len(s)):
        if findCompounds(w, s): output.add(w)
    output = sorted(output)
    elapsed = time.process_time() - t
    print("time taken: ", elapsed)
    return output

if __name__ == '__main__':
    words = set()
    # clean duplicates from input before processing algorithm
    for line in sys.stdin:
        w = line.strip() # strips newline and whitespace
        if len(w) > 0 and w not in words: # no empty strings
            words.add(w)
    compounds = processList(words)
    # print results to stdout
    for c in compounds:
        print(c)
