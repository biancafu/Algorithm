from collections import defaultdict
class Solution:
    def findWords(self, board, words):
        """
        to go through the matrix using backtracking
        nested for loop, dfs on each element to check if the word exists from the list

        if check through each word one by one, m*n*4^len(word)*len(wordlist) not sure
        using a trie will help us optimize the checking word process by its fast prefix search

        create Trie for the wordlist
        iterate through matrix
        dfs
        check if word exists in Trie
        """

        class Trie:
            def __init__(self):
                self.trie = {'ref':defaultdict(int)}
            
            def insert(self, word: str):
                curr = self.trie #pointer
                for i, char in enumerate(word):
                    if i == 0:
                        curr['ref'][char] += 1
                    if char not in curr:
                        curr[char] = {}
                    curr = curr[char] #increment
                curr["-"] = True     

            def search(self, word:str) -> bool:
                curr = self.trie   
                
                for c in word:
                    if c not in curr:
                        return False
                    curr = curr[c]
                return "-" in curr
            
            def startsWith(self, word:str) -> bool:
                curr = self.trie   
                
                for c in word:
                    if c not in curr:
                        return False
                    curr = curr[c]
                return True
            
            def remove(self, word:str):
                curr = self.trie
                if len(word)>0:
                    curr['ref'][word[0]] -= 1
                
        
        visited = set()
        output = set()
        m = len(board)
        n = len(board[0])

        root = Trie()
        for word in words:
            root.insert(word)

        def dfs(i,j, node, word, root):
            # curr = node.trie
            if( i < 0 or i >= (m) or
                j < 0 or j >= (n) or 
                (i,j) in visited or
                board[i][j] not in node):
                return False
            
            visited.add((i,j))
            word += board[i][j]
            node = node[board[i][j]]
            if "-" in node and word not in output:
                output.add(word)
                root.remove(word)

            res = ( dfs(i+1, j, node, word, root) or 
                    dfs(i, j+1, node, word, root) or 
                    dfs(i-1, j, node, word, root) or 
                    dfs(i, j-1, node, word, root) 
                )
            visited.remove((i,j))

        for i in range(m):
            for j in range(n):
                if root.trie['ref'][board[i][j]] > 0:
                    dfs(i,j, root.trie, "", root)
        
        return output
            
            
s = Solution()
a = s.findWords([["a","a","b"],["b","b","a"],["a","a","a"]], ["aaa","ba","a"])    
print(a)
