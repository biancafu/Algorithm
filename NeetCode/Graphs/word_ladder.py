#BFS can be used to find a single source shortest path in an unweighted graph because in BFS, we reach a vertex with a minimum number of edges from a source vertex.
#In DFS, we might traverse through more edges to reach a destination vertex from a source.
#https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/



'''
- only change one letter at a time (every adjacent pair of words differs by a single letter)
- begin word doesnt hv to be in wordlist

1. find patterns from all the words and link them eg: hit can be *it, h*t, hi* since we can transform one letter
2. link the words that the pattern can transform into
3. BFS (shortest path)
'''