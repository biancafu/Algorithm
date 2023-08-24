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
        
        #lists, dictionsaries, sets are all mutable objects in python, when we say cur = self.trie, since self.trie is a mutable object, when we modify cur (the reference), it changes the original object (self.trie) as well.

    def search(self, word, tree=None):
        #we can search normally until we encounter a "."
        cur = self.trie if not tree else tree

        for i,c in enumerate(word):
            #special case
            if c == ".":
                for key in cur.keys():
                    if key == "-": #we are checkign this at the end
                        continue
                    x = word[i+1:] if i+1 < len(word) else ""

                    if self.search(x, cur[key]): #have to start from where the current key is, and pass in the part of words that is not checked yet
                        return True #only return True when we find a match, other wise keep checking
                    #didn't separate case when . is last character, this is because i realized that it will still be the same. It is extra here to check if "-" is in cur[key], becuz if we just leave the condition like above, it will recursively search("", cur[key]) again where the for loop will be skip since empty string and then go straight to returning "-" in cur

                #      if i < len(word) - 1:
                #         if self.search(word[i+1:], cur[key]): 
                #             return True                       
                #     else:
                #         if "-" in cur[key]:
                #             return True 
                # return False 

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