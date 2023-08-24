#essentially the same thing as what neetcode did, but instead of creating another class, this solution simply creates nested hashmap within Trie class. To determine end of the word, this solution uses "-" to store in hashmap
#96% speed 92% memory
class Trie(object):

    def __init__(self):
        self.trie = {} #root is a hashmap that can store up to 27 characters, extra one to indicate it is the end of a character
        #the end of a character will be indicated in the nested map of last character using "-"

    def insert(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {} 
            cur = cur[c] #increment to next word
        cur["-"] = True

    def search(self, word):
        cur = self.trie
        for c in word:
            if not c in cur:
                return False
            cur = cur[c]
        
        return "-" in cur #check if the word ends there
        

    def startsWith(self, prefix):
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False

            cur = cur[c]
        return True