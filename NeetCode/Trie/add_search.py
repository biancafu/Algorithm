#took an hour because there were some error and couldnt find, but the logic i have is correct
#have to be faster when finding errors

#94% speed 92%memory, very good
#since the performance is better than neetcode solution, i won't write the neetcode solution
#I think because he created a trienode class, it slowed down the process, or else we basically have same logic
#instead of calling itself recursively, neetcode created a function inside and recursively called that
class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["-"] = True
        

    def search(self, word, tree = None):
        cur = self.trie if not tree else tree

        for i,c in enumerate(word):
            if c == '.':
                for key in cur.keys():
                    if key == "-":
                        continue
                    #if . is in middle
                    if i < len(word) - 1:
                        #this will recursively check every single possible word 
                        if self.search(word[i+1:], cur[key]): #only return when its True (when we find a match), if False, we will continue with for loop and check other keys.
                            return True                       
                    else: #if . is last character, we need to check if there is an end for any character
                        if "-" in cur[key]:
                            return True #only return True if we found an end, if not, we will continue to see if the other key has an end to it, until we run out of keys, then we return False at the very end
                return False
            
            #normal checking when its a normal character
            # else: #we can do this or not, it didn't change much
            if c not in cur:
                return False
            cur = cur[c]
        return "-" in cur
        

def loop(arr , arr2):
    for i,a in enumerate(arr):
        if a == "WordDictionary":
            wordDictionary = WordDictionary()
        if a == "addWord":
            wordDictionary.addWord(arr2[i])
        if a == "search":
            
            print(arr2[i] , wordDictionary.search(arr2[i]))

loop(["WordDictionary","addWord","addWord","search","search","search","search","search","search"], 
     [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]])