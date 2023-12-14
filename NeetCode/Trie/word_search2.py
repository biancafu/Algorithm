class Trie:
    def __init__(self, words = None):
		# The variable length stores the total number of children of this node.
        self.root = {"length": 0}
        for word in words:
            self.insert(word)
			
	# Having a len method helps debug.
    def __len__(self):
        return self.root["length"]

    # Insert a word into this trie object. O(1) because max word length is 10 chars.
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            # There is more complete word under this node.
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    # Remove a word from this trie object. O(1) because max word length is 10.
    def remove(self, word):
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    current.pop(c)
                    break #after we pop, we don't need to check the rest of word becuz we popped the ones connected above
                else:
                    current = current[c]
        # If we get to the word leaf but the trie node has children.
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    # Check if a given list of chars is in the trie, it returns 0 if
    # not found, 1 if found but not a full word and 2 if a full word.
	# O(1) because max word length is 10.
    def contains(self, word) :
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1

class Solution(object):
    def findWords(self, board, words):
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Remove words for which one of their two letter combinations
        # cannot be found in the board.
        seq_two = set()
        candidates = []
        reversed_words = set()
        # Find all sequences of two characters in the board. Only right
        # and down.
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS - 1):
                seq_two.add(board[i][j] + board[i][j + 1])
        for j in range(NUM_COLS):
            for i in range(NUM_ROWS - 1):
                seq_two.add(board[i][j] + board[i + 1][j])
        # Iterate over the words checking if they could be in the board.
        for word in words:
            in_board = True
            for i in range(len(word) - 1):
                # For each sequence of two characters in the word, check
                # if that sequence or its inverse are in the board.
                if (
                    word[i : i + 2] not in seq_two
                    and word[i + 1] + word[i] not in seq_two
                ):
                    in_board = False
                    break
            if not in_board:
                continue
            # Reverse words with the same character in the first
            # four positions.
            if word[:4] == word[0] * 4:
                word = word[::-1]
                reversed_words.add(word)
            candidates.append(word)

        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        # Store the words found.
        res = set()
        # Initialize a Trie with the words in the input that could be in
        # the board potentially, the candidates, some of them may have
        # been reversed to make finding them more efficient.
        trie = Trie(candidates)
        # Define a function that explores the board from a given start
        # position.
        def dfs(row, col, current):
            current.append(board[row][col])
            board[row][col] = "."
            found = trie.contains(current)
            # If the current branch is not in the trie, not point on
            # exploring any further.
            if not found:
                board[row][col] = current.pop()
                return
            # If this is an exact match, add it to the result set.
            if found == 2:
                w = "".join(current)
                if w in reversed_words:
                    res.add(w[::-1])
                    reversed_words.remove(w)
                else:
                    res.add(w)
                trie.remove(w)
            # The four directions where neighbors are found.
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for di, dj in dirs:
                i, j = row + di, col + dj
                if (
                    0 <= i < NUM_ROWS
                    and 0 <= j < NUM_COLS
                    and board[i][j] != "."
                ):
                    dfs(i, j, current)
            # Backtrack.
            board[row][col] = current.pop()

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                dfs(i, j, [])
        return res