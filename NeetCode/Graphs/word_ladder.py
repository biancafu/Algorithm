#BFS can be used to find a single source shortest path in an unweighted graph because in BFS, we reach a vertex with a minimum number of edges from a source vertex.
#In DFS, we might traverse through more edges to reach a destination vertex from a source.
#https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/


# 88% speed, 36% memory
# this is M*N^2 time complexity where M is word length and N is wordlist length
# N*M^2 for creating the word graph, N*M is easy to see, the extra *M is from slicing
# N^2 (going through all edges: this is because N(N-1) is the max edges of undirected graph) * M (checking each character) * M (slicing) 
# even tho, we are not going into repeating words, however, we check it after we run it (meaning we still ran that edge then check)
import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        - only change one letter at a time (every adjacent pair of words differs by a single letter)
        - begin word doesnt hv to be in wordlist

        steps:
        1. find patterns from all the words and link them eg: hit can be *it, h*t, hi* since we can transform one letter
        2. link the words that the pattern can transform into
        3. BFS (shortest path)
        """

        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        m = len(beginWord)
        wordList.append(beginWord)

        '''
        instead of setting up the graph, we can also check all alphabets during the q, which will be constant time (26) 
        '''
        #go through everry word and record its pattern
        for word in wordList:
            for i in range(m):
                pattern = word[:i] + '*' + word[i+1:] #this will cost m time complexity
                nei[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        #mistake: forgot how queue works, needs to use a for loop to set limit for each level
        while q:
            for w in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res

                for i in range(m):
                    pattern = curr[:i] + '*' + curr[i+1:]
                    for word in nei[pattern]:
                        if word not in visited:
                            q.append(word)
                            visited.add(word)
            res += 1

        return 0










        
       
        

        