def compositeWord(word,s):  
    if not word:
        return True  
    print("word: ", word)
    for prefix in (word[:i] for i in range(1, len(word) + 1)):
        print("prefix: ", prefix)
        if prefix in s:
            if compositeWord(word[len(prefix):], s) == True:
                return True         
    s.add(word)    
    print("set: ", s)
    return False       

def simpleWords(words):    
    s = set()
    return [w for w in words if compositeWord(w,s)]

if __name__ == '__main__': 
    print(simpleWords(sorted(["man", "woman", "manhandle", "handle", "race", "drag", "car", "racecar", "computer", "bag", "dragon", "manbag"],key=lambda s: len(s))))
