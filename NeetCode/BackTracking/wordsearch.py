class Solution:
    #92% 35% too lazy to read
    def exist(self, board: List[List[str]], word: str) -> bool:
	# Count number of letters in board and store it in a dictionary
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        # Traverse through board and if word[0] == board[i][j], call the DFS function
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):
                        return True

        return False

    def dfs(self, i, j, k, board, word):
        # Recursion will return False if (i,j) is out of bounds or board[i][j] != word[k] which is current letter we need
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
        k >= len(word) or word[k] != board[i][j]:
            return False

        # If this statement is true then it means we have reach the last letter in the word so we can return True
        if k == len(word) - 1:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in directions:
            # Since we can't use the same letter twice, I'm changing current board[i][j] to -1 before traversing further
            tmp = board[i][j]
            board[i][j] = -1

            # If dfs returns True then return True so there will be no further dfs
            if self.dfs(i + x, j + y, k + 1, board, word): 
                return True

            board[i][j] = tmp


    #61% 35%
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c,idx):
        # if idx == len(word), then word has been found
            if idx == len(word):
                return True

        # out of bounds
        # OR current letter does not match letter on board
        # OR letter already visited
            if ( 
                r<0 or r>=ROWS 
                or c<0 or c>=COLS
                or word[idx] != board[r][c]
                or (r,c) in visited
            ):
                return False
  
        # to keep track of the letter already visited, add it's position to the set
        # after DFS we can remove it from the set.
            visited.add((r,c))

        # performing DFS 
            res = (
                dfs(r+1,c,idx+1) 
                or dfs(r-1,c,idx+1) 
                or dfs(r,c+1,idx+1) 
                or dfs(r,c-1,idx+1)
            )
        
            visited.remove((r,c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
    
